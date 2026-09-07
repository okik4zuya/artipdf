2026-08-08T22:03:28.6891680Z Current runner version: '2.336.0'
2026-08-08T22:03:28.6905980Z ##[group]Runner Image Provisioner
2026-08-08T22:03:28.6906490Z Hosted Compute Agent
2026-08-08T22:03:28.6906860Z Version: 20260707.563
2026-08-08T22:03:28.6907280Z Commit: 02667638d2b423fbc733a8e32a88b44996a3ba6e
2026-08-08T22:03:28.6907760Z Build Date: 2026-07-07T19:33:50Z
2026-08-08T22:03:28.6908200Z Worker ID: {c0329edc-8d11-4022-aea2-aaf871accdc8}
2026-08-08T22:03:28.6908640Z Azure Region: westus
2026-08-08T22:03:28.6909000Z ##[endgroup]
2026-08-08T22:03:28.6909890Z ##[group]Operating System
2026-08-08T22:03:28.6910350Z macOS
2026-08-08T22:03:28.6910740Z 26.5.2
2026-08-08T22:03:28.6911070Z 25F84
2026-08-08T22:03:28.6911450Z ##[endgroup]
2026-08-08T22:03:28.6911840Z ##[group]Runner Image
2026-08-08T22:03:28.6912210Z Image: macos-26-arm64
2026-08-08T22:03:28.6912580Z Version: 20260728.0273.1
2026-08-08T22:03:28.6913360Z Included Software: https://github.com/actions/runner-images/blob/macos-26-arm64/20260728.0273/images/macos/macos-26-arm64-Readme.md
2026-08-08T22:03:28.6914390Z Image Release: https://github.com/actions/runner-images/releases/tag/macos-26-arm64%2F20260728.0273
2026-08-08T22:03:28.6915030Z ##[endgroup]
2026-08-08T22:03:28.6915780Z ##[group]GITHUB_TOKEN Permissions
2026-08-08T22:03:28.6916770Z Contents: read
2026-08-08T22:03:28.6917130Z Metadata: read
2026-08-08T22:03:28.6917470Z Packages: read
2026-08-08T22:03:28.6917820Z ##[endgroup]
2026-08-08T22:03:28.6919100Z Secret source: Actions
2026-08-08T22:03:28.6919720Z Prepare workflow directory
2026-08-08T22:03:28.7145240Z Prepare all required actions
2026-08-08T22:03:28.7191800Z Getting action download info
2026-08-08T22:03:28.9529090Z Download action repository 'actions/checkout@v4' (SHA:11d5960a326750d5838078e36cf38b85af677262)
2026-08-08T22:03:29.2574450Z Download action repository 'actions/setup-python@v5' (SHA:a26af69be951a213d495a4c3e4e4022e16d87065)
2026-08-08T22:03:29.4506860Z Download action repository 'actions/upload-artifact@v4' (SHA:ea165f8d65b6e75b540449e92b4886f43607fa02)
2026-08-08T22:03:29.7131230Z Complete job name: macos-build
2026-08-08T22:03:29.7624360Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
2026-08-08T22:03:29.7631690Z ##[group]Run actions/checkout@v4
2026-08-08T22:03:29.7632200Z with:
2026-08-08T22:03:29.7632510Z   repository: okik4zuya/uglypdf
2026-08-08T22:03:29.7635260Z   token: ***
2026-08-08T22:03:29.7635560Z   ssh-strict: true
2026-08-08T22:03:29.7635860Z   ssh-user: git
2026-08-08T22:03:29.7636170Z   persist-credentials: true
2026-08-08T22:03:29.7636570Z   clean: true
2026-08-08T22:03:29.7636920Z   sparse-checkout-cone-mode: true
2026-08-08T22:03:29.7637280Z   fetch-depth: 1
2026-08-08T22:03:29.7637580Z   fetch-tags: false
2026-08-08T22:03:29.7637900Z   show-progress: true
2026-08-08T22:03:29.7638360Z   lfs: false
2026-08-08T22:03:29.7638680Z   submodules: false
2026-08-08T22:03:29.7639000Z   set-safe-directory: true
2026-08-08T22:03:29.7639350Z   allow-unsafe-pr-checkout: false
2026-08-08T22:03:29.7639890Z ##[endgroup]
2026-08-08T22:03:30.2070880Z Syncing repository: okik4zuya/uglypdf
2026-08-08T22:03:30.2072380Z ##[group]Getting Git version info
2026-08-08T22:03:30.2072880Z Working directory is '/Users/runner/work/uglypdf/uglypdf'
2026-08-08T22:03:30.2076090Z [command]/opt/homebrew/bin/git version
2026-08-08T22:03:30.2392170Z git version 2.55.0
2026-08-08T22:03:30.2414210Z ##[endgroup]
2026-08-08T22:03:30.2422300Z Copying '/Users/runner/.gitconfig' to '/Users/runner/work/_temp/e546533b-7726-4100-a116-8b17db49c233/.gitconfig'
2026-08-08T22:03:30.2428660Z Temporarily overriding HOME='/Users/runner/work/_temp/e546533b-7726-4100-a116-8b17db49c233' before making global git config changes
2026-08-08T22:03:30.2429700Z Adding repository directory to the temporary git global config as a safe directory
2026-08-08T22:03:30.2431950Z [command]/opt/homebrew/bin/git config --global --add safe.directory /Users/runner/work/uglypdf/uglypdf
2026-08-08T22:03:30.2562730Z Deleting the contents of '/Users/runner/work/uglypdf/uglypdf'
2026-08-08T22:03:30.2568520Z ##[group]Initializing the repository
2026-08-08T22:03:30.2571200Z [command]/opt/homebrew/bin/git init /Users/runner/work/uglypdf/uglypdf
2026-08-08T22:03:30.2865430Z hint: Using 'master' as the name for the initial branch. This default branch name
2026-08-08T22:03:30.2867980Z hint: will change to "main" in Git 3.0. To configure the initial branch name
2026-08-08T22:03:30.2871300Z hint: to use in all of your new repositories, which will suppress this warning,
2026-08-08T22:03:30.2873400Z hint: call:
2026-08-08T22:03:30.2873880Z hint:
2026-08-08T22:03:30.2874460Z hint: 	git config --global init.defaultBranch <name>
2026-08-08T22:03:30.2875600Z hint:
2026-08-08T22:03:30.2876190Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2026-08-08T22:03:30.2877040Z hint: 'development'. The just-created branch can be renamed via this command:
2026-08-08T22:03:30.2877800Z hint:
2026-08-08T22:03:30.2879940Z hint: 	git branch -m <name>
2026-08-08T22:03:30.2880490Z hint:
2026-08-08T22:03:30.2881170Z hint: Disable this message with "git config set advice.defaultBranchName false"
2026-08-08T22:03:30.2882060Z Initialized empty Git repository in /Users/runner/work/uglypdf/uglypdf/.git/
2026-08-08T22:03:30.2885140Z [command]/opt/homebrew/bin/git remote add origin https://github.com/okik4zuya/uglypdf
2026-08-08T22:03:30.2983460Z ##[endgroup]
2026-08-08T22:03:30.2984080Z ##[group]Disabling automatic garbage collection
2026-08-08T22:03:30.2987710Z [command]/opt/homebrew/bin/git config --local gc.auto 0
2026-08-08T22:03:30.3071850Z ##[endgroup]
2026-08-08T22:03:30.3072660Z ##[group]Setting up auth
2026-08-08T22:03:30.3079000Z [command]/opt/homebrew/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-08-08T22:03:30.3157100Z [command]/opt/homebrew/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-08-08T22:03:30.4297890Z [command]/opt/homebrew/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-08-08T22:03:30.4362570Z [command]/opt/homebrew/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-08-08T22:03:30.5205560Z [command]/opt/homebrew/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-08-08T22:03:30.5507770Z [command]/opt/homebrew/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-08-08T22:03:30.7467150Z [command]/opt/homebrew/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2026-08-08T22:03:30.7652510Z ##[endgroup]
2026-08-08T22:03:30.7653810Z ##[group]Fetching the repository
2026-08-08T22:03:30.7656000Z [command]/opt/homebrew/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +34985ab2b04d679be20a0ebe947aa1eccd53d452:refs/remotes/origin/main
2026-08-08T22:03:31.4368710Z From https://github.com/okik4zuya/uglypdf
2026-08-08T22:03:31.4369980Z  * [new ref]         34985ab2b04d679be20a0ebe947aa1eccd53d452 -> origin/main
2026-08-08T22:03:31.4371260Z ##[endgroup]
2026-08-08T22:03:31.4371660Z ##[group]Determining the checkout info
2026-08-08T22:03:31.4372120Z ##[endgroup]
2026-08-08T22:03:31.4375780Z [command]/opt/homebrew/bin/git sparse-checkout disable
2026-08-08T22:03:31.4453570Z [command]/opt/homebrew/bin/git config --local --unset-all extensions.worktreeConfig
2026-08-08T22:03:31.4511880Z ##[group]Checking out the ref
2026-08-08T22:03:31.4512380Z [command]/opt/homebrew/bin/git checkout --progress --force -B main refs/remotes/origin/main
2026-08-08T22:03:31.4673560Z Switched to a new branch 'main'
2026-08-08T22:03:31.4749710Z branch 'main' set up to track 'origin/main'.
2026-08-08T22:03:31.4751380Z ##[endgroup]
2026-08-08T22:03:31.4792150Z [command]/opt/homebrew/bin/git log -1 --format=%H
2026-08-08T22:03:31.4855040Z 34985ab2b04d679be20a0ebe947aa1eccd53d452
2026-08-08T22:03:31.5118040Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
2026-08-08T22:03:31.5119840Z ##[group]Run actions/setup-python@v5
2026-08-08T22:03:31.5120180Z with:
2026-08-08T22:03:31.5120590Z   python-version: 3.11
2026-08-08T22:03:31.5120870Z   check-latest: false
2026-08-08T22:03:31.5123000Z   token: ***
2026-08-08T22:03:31.5123350Z   update-environment: true
2026-08-08T22:03:31.5123630Z   allow-prereleases: false
2026-08-08T22:03:31.5123910Z   freethreaded: false
2026-08-08T22:03:31.5124200Z ##[endgroup]
2026-08-08T22:03:31.6575190Z ##[group]Installed versions
2026-08-08T22:03:31.6664090Z (node:3156) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-08-08T22:03:31.6666190Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-08-08T22:03:31.6666820Z Successfully set up CPython (3.11.9)
2026-08-08T22:03:31.6672350Z ##[endgroup]
2026-08-08T22:03:31.6824060Z ##[group]Run python -m venv venv
2026-08-08T22:03:31.6824630Z [36;1mpython -m venv venv[0m
2026-08-08T22:03:31.6824890Z [36;1msource venv/bin/activate[0m
2026-08-08T22:03:31.6825240Z [36;1mpip install -r requirements.txt[0m
202…