; installer.nsi — NSIS installer for ARTi PDF
; Build with: makensis installer.nsi
; Requires dist\ArtiPDF\ to already exist (run build.bat first).

!include "MUI2.nsh"
!include "nsDialogs.nsh"
!include "FileFunc.nsh"

; ---------------------------------------------------------------------------
; Constants — bump APP_VERSION alongside app/tab_about.py::VERSION
; ---------------------------------------------------------------------------
!define APP_NAME        "ARTi PDF"
!define APP_VERSION      "1.0.7"
!define APP_PUBLISHER    "okik4zuya"
!define APP_EXE          "ArtiPDF.exe"
!define APP_CLI_EXE      "ArtiPDFConvert.exe"
!define APP_SUMMARY_EXE  "ArtiPDFSummarize.exe"
!define APP_COMPRESS_EXE "ArtiPDFCompress.exe"
!define APP_URL          "https://github.com/okik4zuya/artipdf"
!define UNINSTALL_KEY    "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}"

Name "${APP_NAME}"
OutFile "dist\ArtiPDFSetup-${APP_VERSION}.exe"
InstallDir "$PROGRAMFILES64\${APP_NAME}"
InstallDirRegKey HKLM "Software\${APP_NAME}" "InstallDir"
RequestExecutionLevel admin

!define MUI_ABORTWARNING
!define MUI_ICON "icon.ico"
!define MUI_UNICON "icon.ico"

; ---------------------------------------------------------------------------
; Pages
; ---------------------------------------------------------------------------
!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
Page custom DesktopShortcutPageCreate DesktopShortcutPageLeave
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_LANGUAGE "English"

; ---------------------------------------------------------------------------
; Desktop shortcut checkbox (simple custom page)
; ---------------------------------------------------------------------------
Var Dialog
Var DesktopCheckbox
Var CreateDesktopShortcut

Function DesktopShortcutPageCreate
    !insertmacro MUI_HEADER_TEXT "Additional Shortcuts" "Choose additional shortcuts to create."
    nsDialogs::Create 1018
    Pop $Dialog
    ${If} $Dialog == error
        Abort
    ${EndIf}

    ${NSD_CreateCheckbox} 0 0 100% 12u "Create a Desktop shortcut"
    Pop $DesktopCheckbox
    ${NSD_SetState} $DesktopCheckbox ${BST_CHECKED}

    nsDialogs::Show
FunctionEnd

Function DesktopShortcutPageLeave
    ${NSD_GetState} $DesktopCheckbox $CreateDesktopShortcut
FunctionEnd

; ---------------------------------------------------------------------------
; Install
; ---------------------------------------------------------------------------
Section "Install" SEC01
    SetOutPath "$INSTDIR"
    File /r "dist\ArtiPDF\*.*"

    CreateDirectory "$SMPROGRAMS\${APP_NAME}"
    CreateShortcut "$SMPROGRAMS\${APP_NAME}\${APP_NAME}.lnk" "$INSTDIR\${APP_EXE}"
    CreateShortcut "$SMPROGRAMS\${APP_NAME}\Uninstall ${APP_NAME}.lnk" "$INSTDIR\Uninstall.exe"

    ${If} $CreateDesktopShortcut == ${BST_CHECKED}
        CreateShortcut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${APP_EXE}"
    ${EndIf}

    WriteRegStr HKLM "Software\${APP_NAME}" "InstallDir" "$INSTDIR"

    WriteRegStr HKLM "${UNINSTALL_KEY}" "DisplayName" "${APP_NAME}"
    WriteRegStr HKLM "${UNINSTALL_KEY}" "DisplayVersion" "${APP_VERSION}"
    WriteRegStr HKLM "${UNINSTALL_KEY}" "Publisher" "${APP_PUBLISHER}"
    WriteRegStr HKLM "${UNINSTALL_KEY}" "DisplayIcon" "$INSTDIR\${APP_EXE}"
    WriteRegStr HKLM "${UNINSTALL_KEY}" "UninstallString" "$INSTDIR\Uninstall.exe"
    WriteRegStr HKLM "${UNINSTALL_KEY}" "QuietUninstallString" '"$INSTDIR\Uninstall.exe" /S'
    WriteRegStr HKLM "${UNINSTALL_KEY}" "InstallLocation" "$INSTDIR"
    WriteRegDWORD HKLM "${UNINSTALL_KEY}" "NoModify" 1
    WriteRegDWORD HKLM "${UNINSTALL_KEY}" "NoRepair" 1

    ; EstimatedSize wants KB
    ${GetSize} "$INSTDIR" "/S=0K" $0 $1 $2
    IntFmt $0 "0x%08X" $0
    WriteRegDWORD HKLM "${UNINSTALL_KEY}" "EstimatedSize" "$0"

    ; Explorer file context menu: "Convert to Markdown" on .pdf files.
    ; MultiSelectModel=Player only controls whether/how many items this verb
    ; is offered for on a multi-selection; for a plain registry command verb
    ; like this one, Explorer still launches one ArtiPDFConvert.exe process
    ; per selected file (substituting "%1" each time), not one process for
    ; the whole selection. ArtiPDFConvert.exe itself coalesces those sibling
    ; processes into a single visible console (leader/follower election via
    ; a named mutex, see pdf2md.py) so a bulk selection doesn't pop up N
    ; console windows.
    WriteRegStr HKCR "SystemFileAssociations\.pdf\shell\ConvertToMarkdown" "" "Convert to Markdown"
    WriteRegStr HKCR "SystemFileAssociations\.pdf\shell\ConvertToMarkdown" "Icon" "$INSTDIR\${APP_EXE},0"
    WriteRegStr HKCR "SystemFileAssociations\.pdf\shell\ConvertToMarkdown" "MultiSelectModel" "Player"
    WriteRegStr HKCR "SystemFileAssociations\.pdf\shell\ConvertToMarkdown\command" "" '"$INSTDIR\${APP_CLI_EXE}" "%1"'

    ; "Summarize with AI" — same per-process-per-file leader/follower coalescing
    ; as ConvertToMarkdown (see pdf2summary.py), under its own mutex/manifest
    ; names so a concurrent Convert-to-Markdown batch never collides with it.
    ; Requires the ARTi dashboard running locally (calls its /api/pdf-summarize).
    WriteRegStr HKCR "SystemFileAssociations\.pdf\shell\SummarizeWithAI" "" "Summarize with AI"
    WriteRegStr HKCR "SystemFileAssociations\.pdf\shell\SummarizeWithAI" "Icon" "$INSTDIR\${APP_EXE},0"
    WriteRegStr HKCR "SystemFileAssociations\.pdf\shell\SummarizeWithAI" "MultiSelectModel" "Player"
    WriteRegStr HKCR "SystemFileAssociations\.pdf\shell\SummarizeWithAI\command" "" '"$INSTDIR\${APP_SUMMARY_EXE}" "%1"'

    ; "Compress PDF" — same leader/follower coalescing (see pdf2compress.py),
    ; own mutex/manifest names. One-click, fixed "medium" preset.
    WriteRegStr HKCR "SystemFileAssociations\.pdf\shell\CompressPDF" "" "Compress PDF"
    WriteRegStr HKCR "SystemFileAssociations\.pdf\shell\CompressPDF" "Icon" "$INSTDIR\${APP_EXE},0"
    WriteRegStr HKCR "SystemFileAssociations\.pdf\shell\CompressPDF" "MultiSelectModel" "Player"
    WriteRegStr HKCR "SystemFileAssociations\.pdf\shell\CompressPDF\command" "" '"$INSTDIR\${APP_COMPRESS_EXE}" "%1"'

    WriteUninstaller "$INSTDIR\Uninstall.exe"
SectionEnd

; ---------------------------------------------------------------------------
; Uninstall
; ---------------------------------------------------------------------------
Section "Uninstall"
    RMDir /r "$INSTDIR"

    Delete "$SMPROGRAMS\${APP_NAME}\${APP_NAME}.lnk"
    Delete "$SMPROGRAMS\${APP_NAME}\Uninstall ${APP_NAME}.lnk"
    RMDir "$SMPROGRAMS\${APP_NAME}"
    Delete "$DESKTOP\${APP_NAME}.lnk"

    DeleteRegKey HKLM "${UNINSTALL_KEY}"
    DeleteRegKey HKLM "Software\${APP_NAME}"
    DeleteRegKey HKCR "SystemFileAssociations\.pdf\shell\ConvertToMarkdown"
    DeleteRegKey HKCR "SystemFileAssociations\.pdf\shell\SummarizeWithAI"
    DeleteRegKey HKCR "SystemFileAssociations\.pdf\shell\CompressPDF"
SectionEnd
