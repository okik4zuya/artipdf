# Extracted PDF Content

Materials Today Sustainability 22 (2023) 100386

Contents lists available at ScienceDirect

Materials Today Sustainability

j o u r n a l h o m e p a g e : h t t p s : / / w w w . j o u r n a l s . e l s e v i e r . c o m /
m a t e r i a l s - t o d a y - s u s t a i n a b i l i t y

Photocatalytic reduction of CO2 at (SnO2, Fe3O4)/TiO2 composite
Kamil Urbanek a, b, Kaja Spilarewicz a, Jiaguo Yu c, Wojciech Macyk a, *
a Faculty of Chemistry, Jagiellonian University, ul. Gronostajowa 2, 30-387, Krak(cid:1)ow, Poland
b Doctoral School of Exact and Natural Sciences, Jagiellonian University, ul. Łojasiewicza 11, 30-348, Krak(cid:1)ow, Poland
c Laboratory of Solar Fuel, Faculty of Materials Science and Chemistry, China University of Geosciences, Wuhan, 430074, PR China

a r t i c l e i n f o

a b s t r a c t

Article history:
Received 18 January 2023
Received in revised form
1 March 2023
Accepted 16 March 2023
Available online 21 March 2023

Keywords:
S-scheme
heterojunction
CO2 reduction
spinel

In this work, the advanced photocatalytic system composed of titanium dioxide (P25) and mSFO (Sn-
doped magnetite with Fe-doped cassiterite) was designed for the gas phase CO2 reduction process. We
have proposed the synthesis route of mSFO composite involving a clean inorganic hydrothermal method
supported by the full characteristics of the obtained material by X-ray diffraction, X-ray photoelectron
spectroscopy, X-ray ﬂuorescence, Mӧssbauer spectroscopy, scanning electron microscopy, transmission
electron microscopy, dynamic light scattering, diffuse reﬂectance spectroscopy, and porosimetry. The
mSFO/P25 system indicates a photocatalytic reduction of CO2 to CO. The activity of the examined pho-
tocatalytic system was also conﬁrmed with the use of 13C labeled carbon dioxide. It was established that
the formed carbon monoxide is a product of CO2 reduction. The surface photovoltage, electrochemical
(linear sweep voltammetry) and photoelectrochemical measurements substantiate the S-scheme
mechanism.

© 2023 Elsevier Ltd. All rights reserved.

1. Introduction

Nowadays, the reduction of CO2 is one of the most challenging
research ﬁelds in photocatalysis among photocatalytic water
splitting, CH4 activation, nitrogen ﬁxation, and photocatalytic ﬁne
chemicals synthesis. The main difﬁculty of this particular process is
the consequence of the high thermodynamical stability of the CO2
molecule (DG0
formation ¼ (cid:2)394 kJ/mol) [1]. One electron CO2
reduction process requires a potential of (cid:2)1.9 V vs. normal
hydrogen electrode (NHE) narrowing the list of potential photo-
catalysts to only a few since the photocatalytic reactions rely on the
potentials of band edges of semiconductors. Multielectron pro-
cesses, which do not require such high energy, exhibit low charge
transfer rates preventing the efﬁcient production of CO, oxygenates
(HCOOH or CH3OH), or hydrocarbons (CH4, CxH2x-2). In addition to
that, there are more concerns with the yields of these processes.
The most unfavorable of them is the weak adsorption of CO2 over
the majority of inorganic materials. Moreover, many photocatalysts
often require sacriﬁcial hole acceptors to guarantee considerable
efﬁciency. Therefore, a strong effort should be placed on the design
of new materials, effective in photocatalytic CO2 reduction.

* Corresponding author.

E-mail address: macyk@chemia.uj.edu.pl (W. Macyk).

https://doi.org/10.1016/j.mtsust.2023.100386
2589-2347/© 2023 Elsevier Ltd. All rights reserved.

Among photocatalysts, titania (TiO2) is one of the most widely
studied photocatalytic semiconductor materials. The photocatalytic
activity of P25 (composite of titania phases with a typical content of
78% anatase, 14% rutile, and up to 8% amorphous phase) results
from synergistic interactions between its components [2].
It
became a benchmark for numerous photocatalytic systems [2].
However, this material is not an ideal solution for all applications,
especially CO2 reduction. Although the potential of the conduction
band (CB) edge of TiO2 is comparable to the potentials of CO2
reduction (e.g., (cid:2)0.24 V vs. NHE for reduction of CO2 toward CH4 in
8 electron process), a photocatalyst should offer signiﬁcantly more
negative CB edge energy (ECB) to perform efﬁciently [3]. Therefore,
titanium dioxide can be used in combination with other semi-
conductors (with better reducing properties) to enable photo-
catalytic CO2 reduction. There are several possible ways of creating
such hybrid systems, depending on the charge carrier separation
mechanism: the conventional type-II heterojunction, a direct Z-
scheme, and an S-scheme [4e8]. The strategy based on combining
different semiconductors is highly promising also due to the efﬁ-
cient separation of the e(cid:2)/hþ pairs, and consequently, their
diminished recombination [9].

Several semiconductors exhibit ECB more suitable for the pho-
tocatalytic reduction of carbon dioxide than P25. So far, the main
efforts have been pushed into the investigation of such materials as
g-C3N4 ((cid:2)1.23 V vs. NHE) [10], CdS ((cid:2)0.6 V vs. NHE) [11], ZnS

K. Urbanek, K. Spilarewicz, J. Yu et al.

Materials Today Sustainability 22 (2023) 100386

((cid:2)1.65 V vs. NHE) [12], and CuI ((cid:2)2.28 V vs. NHE) [13], whereas an
interesting and still insufﬁciently studied group of materials for
application in photocatalytic reduction of CO2 is spinel ferrites
(MFe2O4, M ¼ divalent metal ion) [14]. The main challenge in the
application of this group of materials is the fact that their properties
heavily depend on their phase, size, shape, and structure, thus
many recent works focused on their controlled synthesis [15].
Additionally, the electronic properties of spinel ferrites can be
tuned, and therefore, photocatalytic activity enhanced by doping.
For example, Guo et al. presented that doping of ZnFe2O4 with Ce
accelerates the production rates of H2, CO, and CH4 [16]. Another
premise of the potential for the application of iron materials in the
design of systems for CO2 photocatalytic reduction is the high af-
ﬁnity of iron-bearing minerals, especially Fe3O4, to adsorption of
CO2 molecules at (001) and (111) surfaces [17].

Furthermore, SnO2 is an interesting candidate to design the
photocatalytic system for CO2 reduction, due to its low CB position
[18]. The most outstanding feature of this material is, however, its
high electron mobility (ca. 100e200 cm2/V/S) [19]. Moreover, it
presents high chemical stability and relatively easy synthesis routes
resulting in stable nanoparticles [20]. Currently, limited data indi-
cate that SnO2 nanoparticles can exhibit photocatalytic activity
toward CO2 reduction. For example, Chowdhury et al. reported the
photocatalytic reduction of CO2 to HCOOH in the water phase using
mesoporous SnO2 nanoparticles under white LED light [21].
Moreover, Torres et al. showed that SnO2 nanoparticles decorated
with surface eOH groups are prone to photocatalytically reduce
CO2 to CH4, CO, CH3OH, and C2H4 in CO2/water atmosphere [20].
The increase in photocatalytic activity of SnO2 can be improved by
the introduction of impurities by doping, which can reduce the
incident photon energy and inhibit the recombination of e(cid:2)/hþ
pairs [22].

Herein, we propose for the ﬁrst time the photocatalytic system
composed of TiO2 (P25) and composite (mSFO) of Sn-doped
magnetite (Fe3O4) with Fe-doped cassiterite (SnO2) for the appli-
cation in photocatalytic reduction of CO2, with water as a hole
scavenger instead of other typically used sacriﬁcial agents.

2. Experimental

2.1. Materials

Commercial analytical grade reagents: SnCl2$2H2O, FeCl3$6H2O,
and NaOH were used in the synthesis of materials. The reagents
were used as obtained without further puriﬁcation. AEROXIDE®
TiO2 P25 (Evonik) was also used as obtained.

2.2. Synthesis of studied materials

2.2.1. Preparation of mSFO

A sample of 0.722 g of SnCl2$2H2O was dissolved in 30 ml of
deionized (DI) water. Then, pH was adjusted to 10 by adding
concentrated NaOH solution, and the mixture was stirred for 1 h.
Next 1.728 g of FeCl3$6H2O dissolved in 15 ml of DI water was
added, which was followed by the rapid addition of NaOH solution
(15 ml of DI water with 1.0 g NaOH). The reaction mixture was
stirred for 40 min. Afterward, it was diluted subsequently with two
portions of water (40 and 30 ml), while adjusting pH at 10e10.5
with NaOH solution. Finally, the mixture was transferred to a steel
autoclave equipped with a PTFE insert (200 ml), heated to 200 (cid:3)C
for 24 h, and left to cool down to room temperature.

2.2.2. Preparation of mSFO/P25 mixture

The mSFO and P25 powders were manually ground in an agate
mortar with a 2-to-1 weight ratio. The mSFO/P25 composite ratio

2

was selected by adjusting the mass of components to optimal
photocatalytic performance (Fig. SI1).

2.3.

Instruments

Details about used free software and appropriate references are

in the supporting information.

2.3.1. Dynamic light scattering

To determine the hydrodynamic diameter of mSFO, Malvern
Zeta Sizer Nano (Malvern Instrument) was used for dynamic light
scattering (DLS) measurements. The scattering angle was 173(cid:3), and
the wavelength of the scattered light was 633 nm.

2.3.2. Diffuse reﬂectance spectroscopy

Diffuse reﬂectance spectra of materials were obtained with the
use of Shimadzu UV-3600 UVeViseNIR spectrophotometer
equipped with a 10 cm diameter integrating sphere. Samples mixed
with BaSO4 (white standard; proportions determined based on the
reﬂectance signal) in the form of a tablet were placed in front of the
integrating sphere. A pure BaSO4 tablet was used as a reference.
Collected spectra were recalculated to Kubelka-Munk function, and
then to determine the bandgap energies of the studied samples, the
Tauc transformation was applied with a baseline subtraction pro-
cedure described by Makuła et al. [23].

2.3.3. Mӧssbauer spectroscopy

The 119Sn and 57Fe Mӧssbauer spectra were collected at room
temperature using a Polon-type spectrometer equipped with a
multichannel analyzer and a linear arrangement of a119Sn source in
Ca119SnO3 matrix (10 mCi) and 57Co:Rh (35 mCi) source, respec-
tively. Calibration was conducted at room temperature using a
30 mm thick a-Fe foil. The 119Sn isomer shifts were referenced to
BaSnO3.

2.3.4. Porosimetry

Nitrogen adsorption-desorption isotherms were obtained at
77 K with Autosorb IQ, Quantachrome Instruments. All prepared
samples were thoroughly degassed at 200 (cid:3)C, 50 mTorr before
measurement. The speciﬁc surface areas were calculated by the
multipoint BrunauereEmmeteTeller method using the adsorption
data in the relative pressure (p/p0) range of 0.05e0.3.

2.3.5. Scanning electron microscopy

Scanning electron microscopy (SEM) analysis was performed
using Tescan Vega 3 microscope with the LaB6gun equipped with
SE and BSE detectors. SiliCarbon tape was used as a substrate for
imaging.

2.3.6. Transmission electron microscopy

The morphology of the mSFO sample was studied using FEI
Tecnai Osiris transmission electron microscope (TEM) equipped
with an X-FEG Schottky ﬁeld emitter operating at the voltage of
200 kV. Before TEM observations, the mSFO sample was placed on a
copper grid covered with a holey carbon ﬁlm.

2.3.7. Kelvin probe

Contact potential difference (CPD) was measured using the
Kelvin probe (Insytytut Fotonowy) in the air atmosphere. Surface
photovoltage was measured as a variation of the surface potential
on pulsed illumination (xenon lamp) vs. gold grid reference elec-
trode (Au mesh, diameter 2.5 mm). The background baseline was
subtracted from the data.

K. Urbanek, K. Spilarewicz, J. Yu et al.

Materials Today Sustainability 22 (2023) 100386

2.3.8. Photoelectrochemical measurements

The transient photocurrent measurements of the studied ma-
terials were performed in the three-electrode cell using the elec-
trochemical analyzer equipped with the xenon lamp 150 W
(Instytut Fotonowy). A thin layer of material was deposited on a
transparent ITO foil (60 U/sq, Sigma-Aldrich) and placed as the
working electrode. Simultaneously, a platinum wire and Ag/AgCl in
a 3 M KCl solution, as the counter and reference electrodes,
respectively, were used. The cell was ﬁlled with the acetonitrile
electrolyte (1 M KNO3 solution) and purged with Ar before (for
30 min) and during the measurement. The back side of the working
electrode was illuminated by intermittent on-off illumination in
the wavelength range of 330e450 nm and the applied potential
range of (cid:2)0.2 to 1.0 V vs. Ag/Agþ.

2.3.9. XPS

X-ray photoelectron spectroscopy (XPS) measurements were
carried out in a Prevac photoelectron spectrometer equipped with a
hemispherical VG Scienta R3000 analyzer, using the Al Ka
(l ¼ 1,486.6 eV) radiation. The background pressure in the analysis
chamber was maintained at 10(cid:2)8 mbar, and the pass energy was set
at 100 eV. Due to the static charging of the samples, correction of
the binding energy scale was adjusted by setting the C 1s peak at
284.8 eV of adventitious carbon.

2.3.10. XRD

The crystalline structure of materials was studied by powder X-
ray diffractometer (XRD) Rigaku MiniFlex (PANalytical) with nickel-
ﬁltered copper Ka radiation (l ¼ 0.15406 nm, 40 kV, 15 mA).
Scanning was carried out in the range of 2q ¼ 10e90(cid:3) with 0.02(cid:3)
steps at a scan rate of 2(cid:3) per minute.

2.3.11. XRF

The relative bulk content of tin and iron in the studied samples
was determined with the use of an energy-dispersive X-ray ﬂuo-
rescence (XRF) spectrometer (ARL QUANT'X, Thermo Scientiﬁc).
The used X-rays were in the range of 4e50 kV (1 kV step) with a
beam size of 1 mm and were generated by the rhodium anode. A
3.5 mm Si(Li) drifted crystal with a Peltier cooling (~185 K) detector
was used. For quantitative analysis, the calibration with a series of
metallic standards and UniQuant software was used.

2.3.12. Linear sweep voltammetry

The experiments were carried out in a three-electrode setup. An
Ag/Agþ electrode as the reference electrode, platinum wire as the
counter electrode, and platinum foil covered with the analyzed
material as the working electrode were used. LiClO4 acetonitrile
electrolyte purged with Ar was used. Biologic SP-200 served as a
potentiostat.

2.4. Photocatalytic tests (with GC/MS veriﬁcation protocol)

Photocatalytic tests (Fig. SI2) were performed in a reactor con-
sisting of glass test tubes with silicone septum caps. Their internal
volume is 13 ml; 15 mg of a photocatalyst was evenly spread on the
area of 6 cm2 of a glass plate, which was placed inside the test tube
containing 340 ml of DI and argon-purged water as a moisture
reservoir. Next, the reactor was purged with argon and then 1.8 ml
of CO2 was injected into the reactor, while the excess pressure was
released through an outlet made of a narrow needle placed shal-
lowly into the septum. Then, the reactor was irradiated with a
xenon lamp 150 W (Instytut Fotonowy) through a water ﬁlter. The
absorbance of the reactor glass was measured using a UVeVis
spectrophotometer. Its material functioned as a 340 nm cutoff ﬁl-
ter. The light intensity was measured at the sample position, and its

3

value was found to be 1 W/cm2. The temperature was measured
and never exceeded 36 (cid:3)C. Samples of gas were taken at various
times during the irradiation. Gas sampling was performed by
drawing gas, using a gas-tight syringe (50 ml) with a sample lock
valve, through the septum and the samples were immediately
analyzed using GC-Agilent Technologies 6890N gas chromatograph
(GC) outﬁtted with FID and TCD. The columns used were Molsieve
and HP Poraplot Q for methane, ethane, carbon monoxide, carbon
dioxide, oxygen, and nitrogen analysis. The carrier gas was ultra-
pure argon (impurities levels in the single ppm range) obtained
from Air Products. After the irradiation process, liquid samples
were drawn from the water reservoir from the bottom of the
reactor and analyzed with the Total Organic Carbon analyzer (TOC-
Vcsh, Shimadzu) to establish the possibility of CO2 reduction to the
products other than CH4 and CO in the liquid phase.

To verify that C1 products originated from the photoreduction of
CO2, three blank experiments were carried out. One was done in the
absence of a photocatalyst, the second one was done without CO2,
and the third one was done in the dark. No products were detected
in these three experiments. Furthermore, photocatalytic reduction
of 13CO2 was carried out. Shimadzu QP2020 GC/MS was used to
analyze photocatalytic reduction products to determine the source
of carbon in produced CO. In this experiment, the photocatalytic
reduction procedure was used as described above with the differ-
ence in carbon dioxide substrate. The N4,9 13CO2 from Sigma-
Aldrich was used in these experiments. Several measurements
were carried out, and the results were normalized and averaged to
ensure a high degree of conﬁdence, as peaks from carbon ion (m/
z ¼ 12 and 13) were used for analysis since in the experimental
setup the column did not separate CO and N2 which both produce
ions with the same m/z ¼ 28 (CO2 was separated from CO on GC
column).

3. Results and discussion

3.1. Synthesis and characterization of mSFO

In the synthesis of mixed Sn/Fe oxides described in the Exper-
imental section, no organic species or solvents, which could serve
as a carbon source, were applied. The developed procedure was
relatively complex and extremely sensitive to pH. The relative
concentration of iron and tin ions inﬂuences the formation of either
the Sn-substituted Fe3O4 phase and/or the Fe-substituted SnO2
phase [24]. During the synthesis, the redox reaction occurs spon-
taneously between Sn2þ and Fe3þ ions:

Sn2þ þ 2 Fe3þ þ 6 Cl

e $ ½SnCl6(cid:4)2e

þ 2 Fe2þ

(1)

because the potential of the Sn4þ/Sn2þ redox pair (E(cid:3) ¼ 0.151 V at
298.15 K) is lower than that of the Fe3þ/Fe2þ pair (E(cid:3) ¼ 0.771 V) [25].
Therein, Sn2þ ions act as a sole reducing agent in the reaction
environment, which allows for the further formation of the mixed
valence Fe3O4. At the reaction pH of 10.0e10.5, metal hydroxides
are formed. During the consecutive hydrothermal treatment,
oxidation of the primarily formed hydroxides occurs. Essentially,
tin oxides are less stable in basic solutions than iron oxides, which
is a consequence of the amphoteric properties of tin. Therefore, the
formation of [Sn(OH)6]2e
anions is observed, reaching an equilib-
rium between tin in solution and solid phases [26]. The excess of Sn
remaining in the solution was conﬁrmed experimentally. Moreover,
due to the lower solubility of iron oxides, the growth of SnO2 may
occur at Fe3O4 crystals. The resulting composite of mixed tin/iron
oxides is abbreviated herein as mSFO.

The XRD analysis of mSFO (Fig. 1) reveals diffraction lines at 2q
values of 18.3(cid:3), 30.1(cid:3), 35.4(cid:3), 37.0(cid:3), 43.0(cid:3), 53.4(cid:3), 56.9(cid:3), and 62.5(cid:3),

K. Urbanek, K. Spilarewicz, J. Yu et al.

Materials Today Sustainability 22 (2023) 100386

Table 1. The model consisting of ﬁve components was ﬁtted to the
data and revealed a doublet and four sextets. This type of spectrum
is typical for polycrystalline substituted magnetites obtained via
the hydrothermal method with the Fe3(cid:2)xMxO4 formula [33]. The
sextet marked as S1 corresponds to the tetrahedral (type A) site in
magnetite, with characteristic values of
isomer shift, electric
quadrupole splitting, and hyperﬁne magnetic ﬁeld, being in good
agreement with the literature values for the magnetite [34]. It
should be noted that substitution does not affect the parameters of
this sextet. Subsequently, the superposition of remaining sextets is
interpreted as the average signal from Fe3þ and Fe2þ ions at the
octahedral (type B) sites, noted as Fe2.5þ ions due to the electron
hopping. The S2 sextet presents values of isomer shift, electric
quadrupole splitting, and hyperﬁne magnetic ﬁeld also character-
istic of magnetite [35]. It points to the presence of Fe3þ ions and the
absence of Sn4þ ions in nearby lattice sites, as the highest recorded
spin density is represented by the maximum hyperﬁne ﬁeld value
[36]. The sextets marked as S3 and S4 exhibit deviations of the
ﬁtting parameters, which is a result of the impact of different
numbers of nearest doping atoms [33]. Especially for S4, the
disappearance of magnetic hyperﬁne structure (decrease of H
value) and broadening of the experimental line are observed, which
is consistent with the results of the magnetite doping with Sn4þ
[37]. Concluding, the 57Fe spectrum conﬁrms a partial substitution
of Fe with Sn atoms in octahedral sites in magnetite. Meanwhile,
the D1 doublet originates from Fe3þ in the octahedral site, as the
result of replacing Sn4þ in the tetragonal SnO2 structure with Fe3þ
ions [38]. The obtained parameters are comparable to those re-
ported in the literature for Fe-doped SnO2 [39].

Moreover, the valence state of Sn in mSFO was determined by
119Sn Mӧssbauer spectroscopy (Fig. 2 and Table 2). The spectrum
consists of only one doublet with electric quadrupole interaction,
characteristic of Sn4þ [40]. The results show that there is no tin at
other oxidation states than Sn(IV). A relatively large value of
quadrupole splitting indicates the presence of defects and oxygen
vacancies in the surrounding of the Sn nucleus, which are stabilized
by Fe3þ dopants, as reported by Nomura et al. [41]. Meanwhile, the
observed 0.85 mm/s experimental line width is associated with the
magnetic properties of Fe3O4 in the composite.

The surface chemical composition of mSFO was examined using
XPS. The survey spectrum of the material reveals a complex
structure with the predominant presence of Sn, Fe, and O atoms
(Fig. SI3). To conduct the detailed analysis, deconvolution was
performed (Fig. 3). The deconvoluted spectrum of mSFO in the Fe
2p region shows characteristic peaks for Fe in both oxidation states
and the peak attributed to Sn 3p3/2 core-level electrons of Sn4þ at

Fig. 1. X-ray diffraction of mSFO. Signals marked with asterisks (*) depict the SnO2
phase (cassiterite), while the others are attributed to Fe3O4 (magnetite).

which are assigned, respectively, to (111), (220), (311), (222), (400),
(422), (511), and (440) reﬂections of the Fe3O4 magnetite structure
(COD entry 1,011,084). Magnetite belongs to the class of inverse
spinels. Its crystallographic structure is made of two types of unit
cells involving tetrahedral (A sites: Fe3þ surrounded by four oxygen
atoms) and octahedral (B sites: Fe2þ or Fe3þ surrounded by six
oxygen atoms) sites. However, octahedral sites can be occupied also
by Sn4þ ions [27], the presence of which was conﬁrmed by
M€ossbauer spectroscopy (vide infra). Partial substitution of other
metal cations does not alter the structure of magnetite; therefore,
no signiﬁcant indicators of substitution can be observed in the
diffractogram [28]. Herein, weak peaks marked with asterisks on
the graph at 26.5(cid:3), 33.8(cid:3), and 51.7(cid:3) were attributed to SnO2 with a
rutile type tetragonal structure (cassiterite; COD entry 00-152-
6637) and correspond to (110), (110), and (211) planes, respectively
[29]. Slight shifts of lines to larger values compared to the reference
data point at Fe doping of SnO2 [30,31]. This conclusion is also
supported by Bagheri-Mohagheghi et al. who found that for SnO2
ﬁlms doped up to 7.8% with Fe3þ, the mean crystal size increases in
(110), (101), and (211) directions [32].

To elucidate the chemical composition of mSFO, 57Fe and 119Sn
Mӧssbauer spectroscopy measurements at room temperature were
applied. The 57Fe M€ossbauer spectrum of the composite is pre-
sented in Fig. 2, and the resulting ﬁtting parameters are collected in

Fig. 2. 57Fe M€ossbauer spectrum (left) and 119Sn M€ossbauer spectrum (right) of mSFO at 298 K.

4

K. Urbanek, K. Spilarewicz, J. Yu et al.

Materials Today Sustainability 22 (2023) 100386

Table 1
Fitting parameters of the 57Fe M€ossbauer spectroscopic measurements of mSFO at
room temperature: IS, isomer shift; QS, electric quadrupole splitting; H, hyperﬁne
magnetic ﬁeld; G, experimental line width; A, abundance of the ﬁtted component.

Component

IS (mm/s) QS (mm/s) H (T) G (mm/s) A (%) Oxidation state

S1
S2
S3
S4
D1

0.30
0.62
0.67
0.71
0.32

(cid:2)0.02
(cid:2)0.07
0.00
0.02
0.77

48.6
45.9
44.0
40.4
e

0.45
0.55
0.55
0.85
0.52

39
25
18
12
6

(Tet) Fe3þ
(Oct) Fe2.5þ
(Oct) Fe2.5þ
(Oct) Fe2.5þ
(Oct) Fe3þ

the binding energy of 716.6 eV, which is in good agreement with
parameters observed for composites containing Fe3O4 and SnO2
[29]. The Fe 2p region was ﬁtted with peaks corresponding to Fe2þ
and Fe3þ in Fe3O4 [42] and Sn 3p3/2 (Fig. 3). Moreover, the ﬁtted
peaks indicate signiﬁcantly more Fe3þ than Fe2þ, which supports a
magnetite structure, in agreement with XRD results. Subsequently,
the high-resolution spectra in the Sn 3d region show a spin-orbit
coupling doublet at
the binding energy of 486.85 eV and
495.25 eV, which originate from Sn 3d5/2 and Sn 3d3/2 core-level
electrons of Sn4þ in tetragonal SnO2, respectively [43]. The spin-
orbit splitting separation between these peaks is equal to 8.4 eV,
which is characteristic of Sn4þ [44]. The absence of shoulder peaks
corroborates the lack of Sn2þ in the composite [45]. However, due
to the lack of prominent binding energy shifts for different oxida-
tion states of Sn, which is a consequence of the Madelung effects,
further investigation is necessary to fully exclude the presence of
Sn2þ [46]. It is known that the chemical environment of tin is not
signiﬁcantly affected by iron, which reﬂects in the absence of
characteristic changes in the Sn 3d region [47]. Therefore, on this
basis, the probability of Fe doping of SnO2 cannot be excluded.

From the survey spectrum (Fig. SI3), the Sn:Fe:O ratio of
1:2.5:4.3 was calculated (the organic oxygen was subtracted from
the total oxygen value based on Payne et al.; Figs. SI4-SI5) [48]. The
overabundance of oxygen atoms at the surface in form of possible
hydroxyl groups or defects is well visible in the O 1s region of the
XPS spectrum (Fig. SI4). The XRF analysis indicates a 1:3.4 ratio of
Sn to Fe in the bulk. This discrepancy in the Sn to Fe ratios, obtained
from XPS and XRF, reﬂects the changes in the composition of the
surface and bulk of the material. More Sn atoms are present at the
surface than in bulk, which indicates that SnO2 decorates the sur-
face of Fe3O4 doped with Sn. The SnO2 content is also responsible
for the elevated amount of oxygen in mSFO.

The morphology of the obtained mSFO composite is presented
in Fig. 4. The SEM micrograph (Fig. 4A) reveals the octahedral mi-
crostructures of Fe3O4 with attached nanoparticles of SnO2. This is
corroborated by TEM microscopy (Fig. 4B), which reveals a particle
size of about 0.5 mm with smaller, roughly 50 nm features. This
ﬁnding is conﬁrmed by the DLS measurementsdmSFO particles
with the hydrodynamic diameter of 530 nm predominate, accom-
panied by a small fraction of 70 nm particles (Fig. SI6). The for-
mation of similar octahedral Fe3O4 in solvothermal synthesis was
reported by F. Ooi et al. [49]. The development of such structures is
preferred at higher pH values since OH
acts as a capping agent
[50]. SnO2 nanoparticles decorate Fe3O4 evenly. The relatively small
size of nanoparticles could be a consequence of the restricted

e

Table 2
Fitting parameters of the 119Sn M€ossbauer spectroscopic measurements of mSFO at
room temperature: IS, isomer shift; QS, electric quadrupole splitting; G, experi-
mental line width; A, abundance of the ﬁtted component.

Component

IS (mm/s)

QS (mm/s)

G (mm/s)

A (%)

Oxidation state

D1

0.01

0.56

0.85

100

Sn4þ

5

Fig. 3. XPS spectrum of Fe 2p and Sn 3p regions.

Ostwald ripening mechanism of growth under 200 (cid:3)C in hydro-
thermal synthesis [51]. Moreover, it has been reported that doping
with metals decreases the size of SnO2 crystals [52]. Therefore, this
phenomenon can also affect the size of obtained nanoparticles of
SnO2. The described morphology of mSFO is consistent with XRD
results. High-angle annular dark-ﬁeld scanning TEM (HAADF-
STEM) and electron energy loss spectroscopy (EELS) STEM mapping
images (Fig. 4CeF) show that Fe, Sn, and O elements are distributed
almost uniformly throughout the material. The micrograph reveals
some small areas with a slight predominance of Fe or Sn. The
described results are consistent with XRD, XPS, XRF and M€ossbauer
spectroscopy measurements.

3.2. Composite preparation

The mSFO sample reveals a speciﬁc surface area of 11.6 m2/g,
while the mixture of mSFO/P25 (2e1 wt ratio) shows a speciﬁc
surface area of 27.1 m2/g, which ﬁts a weighted average of speciﬁc
surface areas of mSFO and P25 (54 m2/g [53]). This would indicate
that the mixing procedure does not inﬂuence the structure of
components and does not result in detrimental surface changes
(Fig. SI7). This is further supported by repeated N2 adsorption
measurementsdafter grinding mSFO alone in a mortar no change
in speciﬁc surface area was observed.

3.3. Photoelectrochemical properties

The photoelectrochemical and surface photovoltage measure-
ments were conducted to elucidate the mechanisms of photoin-
duced charge separation and migration. Fig. 5A presents the
material photoresponse to the irradiation at 0.5 V bias. The mSFO
material exhibits photoresponse in the same spectral range as P25,
which probably corresponds to the light absorption by SnO2 in the
composite [54]. The photocurrent density for mSFO is an order of
magnitude lower than for P25, which indicates that bare mSFO is
less photoactive. However, after mixing these two materials, the
photoactivity increases in the full range of probed light, which re-
veals the efﬁcient electron transfer between components and the
effective inhibition of the charge carriers' recombination. Bare P25
exhibits a rapid increase of photocurrent, which quickly reaches the
plateau, whereas the photocurrent development in the case of
mSFO/P25 is slower. This phenomenon can be assigned to electron
trapping by mSFO [55].

K. Urbanek, K. Spilarewicz, J. Yu et al.

Materials Today Sustainability 22 (2023) 100386

Fig. 4. SEM (A), TEM: bright ﬁeld (B), HAADF (C) and EELS (DeF) micrograph of mSFO.

For a deeper understanding of the direction of charge transfer in
the mSFO/P25 system, the surface photovoltage (SPV) measure-
ments were performed (Fig. 5B). The photoresponse was measured
for bare and layered materials, which were prepared by spreading
thin layers of one material on top of the other one, enabling the
higher light intensity to reach only the outermost one. The positive
photovoltage response was observed for mSFO and P25 tested
separately, which indicates that both exhibit n-type conductivity.
Similar results were observed also in the case of P25 spread on top
of mSFO. The photoactivity of both materials appears at 260 nm and
continues to 400 and 440 nm for SFO and P25, respectively. This
difference can be rationalized by the bandgap energy differ-
encedthe analysis of Tauc plots (Fig. SI8) reveals the bandgap en-
ergy of mSFO equal to 3.7 or 4.1 eV for direct and indirect bandgap

estimations, respectively, while the bandgap energy of P25 is lower
(ca. 3.2 eV), as reported in numerous papers [2]. In the case of mSFO
covering P25, a negative CPD signal at wavelengths that are
absorbed by mSFO is observed. For values higher than 400 nm, CPD
is still positive due to light absorption only by P25 in that region,
which is corroborated by the Tauc analysis of mSFO mixed with P25
(Fig. SI9). These results reveal that mSFO could act as an efficient
electron collector to enhance the separation of photo-induced
electron-hole pairs, which is in good agreement with the photo-
current measurements. Fig. 6 depicts the schemes showing the
direction of the electron transfer during the experiments described
above. It is apparent that under irradiation, the excited electrons
were transferred from P25 to mSFO. Observed interactions suggest
that the mSFO-P25 system operates according to the S-scheme with

Fig. 5. Photocurrent measurements of mSFO and P25 samples (A). Surface photovoltage measurementsdcontact potential difference (CPD) of mSFO and P25 samples measured by
Kelvin probe (B).

6

K. Urbanek, K. Spilarewicz, J. Yu et al.

Materials Today Sustainability 22 (2023) 100386

Fig. 6. Principle of SPV measurements for P25 on mSFO (A) and mSFO on P25 (C). Proposed mechanisms of charge separation in the corresponding setups (B, D).

the mSFO component offering higher energy of the CB. Therein,
photoexcited TiO2 generates
the electrons, which probably
recombine with VB holes of the mSFO valence band. Light ab-
sorption by mSFO results in the electron excitation to the CB, from
where it may be capable of CO2 reduction (vide infra). This scheme
may be corroborated by linear sweep voltammetry (Fig. SI10). The
mSFO material can be reduced at lower potentials (higher energies)
than P25, which indicates the higher energy of the CB minimum for
mSFO.

3.4. Photocatalytic activity

Photocatalytic tests were carried out to check the photocatalytic
activity of the mSFO and P25 composites in photocatalytic reduc-
tion of CO2 in water (hole scavenger) saturated argon atmosphere.

Fig. 7A depicts the formation proﬁles of CO in the experiments with
mSFO, P25, and mSFO/P25 in three consecutive runs. Expectedly,
the amount of CO increases with the irradiation time. The mSFO/
P25 composite photocatalyzed CO production, whereas mSFO and
P25 alone did not yield any detectable CO. Speciﬁcally, the CO for-
mation rates for mSFO/P25 in the ﬁrst, second, and third runs were
0.297, 0.181, and 0.096 mmol/g/h, respectively. A decreasing pho-
tocatalytic CO2 conversion in consecutive reaction runs may sug-
gest poisoning of the surface by the reduction product. Fig. 7B and
SI11 depict GC/MS chromatograms recorded for fragmentation of
m/z ¼ 13 and 12. The integrated peak area for m/z ¼ 13 was more
than three times higher than the area for m/z ¼ 12. The test was
validated by carrying out an identical experiment with the use of
normal 12CO2 (Fig. SI12). In this case, the ratio of the peak areas was
inversed and amounted to ca. 0.5. Thus, we conclude that the

Fig. 7. Yield vs. time of photocatalytic CO2 reduction on mSFO and P25 samples in consecutive runs (A). Gas chromatogram (GC/MS) of the gaseous sample collected after 27 h of the
photocatalytic 13CO2 reduction in the presence of mSFO/P25. The presented peak refers to the retention time characteristic of CO (B).

7

K. Urbanek, K. Spilarewicz, J. Yu et al.

Materials Today Sustainability 22 (2023) 100386

resultant CO in photocatalytic tests is the product of photocatalytic
CO2 reduction. Furthermore, total organic carbon (TOC) measure-
ments carried out for the gaseous and aqueous samples (compare
Fig. SI2) revealed an absence of organic carbon within the detection
limit.

The authors would like to thank Mr Marek Drozdek for per-
forming XPS measurements, Dr Mariola Ka˛ dzia˛ łka-Gaweł for per-
forming Mӧssbauer spectrometry measurements and ﬁtting data
with models, and Dr Michał Pacia for performing TEM
measurements.

4. Conclusions

A new advanced mSFO/P25 system of semiconductors consist-
ing of titanium dioxide and mSFO was designed for photocatalytic
CO2 reduction. The synthesis route for obtaining the mSFO com-
posite, consisting of Sn(IV)-doped Fe3O4 microcrystals decorated
with Fe(III)-doped SnO2 nanoparticles, was proposed. The precipi-
tation of hydroxides was followed by hydrothermal treatment.
Since it is crucial to avoid any carbon sources in the synthesized
material that might decompose inter alia to CO during CO2 reduc-
tion experiments, the synthesis was carried out in the absence of
any organic compounds. It was found that pH control constitutes a
vital prerequisite for successful composite fabrication. Applied
spectroscopic and microscopic studies revealed the composition,
structure, and morphology of mSFO, which was further ground
with titanium dioxide.

The photocatalytic performance of mSFO/P25 in the gas phase
reduction of CO2 was conﬁrmed by GC. Carbon monoxide was the
only detectable product. Its origin was veriﬁed by GC-MS analysis,
which conﬁrmed that formed 13CO is a product of the photo-
catalytic reduction of 13CO2.

Linear sweep voltammetry revealed that the energy of the CB
edge of mSFO is higher than the energy of the CB edge of TiO2. In
mSFO/P25, the excited electrons from TiO2 recombine with holes
photogenerated within mSFO. This electron transfer, together with
CO2 reduction taking place at mSFO and oxidation reactions
occurring at TiO2, constitute the so-called S-scheme. Correspond-
ingly, SPV measurements conﬁrm the photoinduced charge sepa-
ration in mSFO/P25, resulting in negative and positive charging of
mSFO and P25, respectively. In such a system, water oxidation with
holes from VB of TiO2 is accomplished; thus, this abundant resource
can act as a hole scavenger.

Credit author statement

Kamil Urbanek: Conceptualization, Data curation, Formal
analysis,
Investigation, Methodology, Validation, Visualization,
Writing e original draft Kaja Spilarewicz: Conceptualization, Data
curation, Formal analysis, Investigation, Methodology, Visualiza-
tion, Writing e original draft Jiaguo Yu: Conceptualization, Writing
e review and editing Wojciech Macyk: Conceptualization, Funding
acquisition, Methodology, Supervision, Writing e original draft,
Writing e review and editing.

Declaration of competing interest

The authors declare that they have no known competing
interests or personal relationships that could have

ﬁnancial
appeared to inﬂuence the work reported in this paper.

Data availability

Data will be made available on request.

Acknowledgments

Appendix A. Supplementary data

Supplementary data to this article can be found online at

https://doi.org/10.1016/j.mtsust.2023.100386.

References

[1] Z. Jiang, T. Xiao, V.L. Kuznetsov, P.P. Edwards, Turning carbon dioxide into fuel,
Phil. Trans. R. Soc. A 368 (2010) 3343e3364, https://doi.org/10.1098/
rsta.2010.0119.

[2] B. Ohtani, O.O. Prieto-Mahaney, D. Li, R. Abe, What is Degussa (Evonik) P25?
Crystalline composition analysis, reconstruction from isolated pure particles
and photocatalytic activity test, J. Photochem. Photobiol. C: Rev. 216 (2010)
179e182, https://doi.org/10.1016/j.jphotochem.2010.07.024.

[3] J. Schneider (Ed.), Photocatalysis: Fundamentals and Perspectives, Royal So-

ciety of Chemistry, Cambridge, UK, 2016.

[4] J. Low, B. Cheng, J. Yu, Surface modiﬁcation and enhanced photocatalytic CO2
reduction performance of TiO2: a review, Appl. Surf. Sci. 392 (2017) 658e686,
https://doi.org/10.1016/j.apsusc.2016.09.093.

[5] L. Wang, C. Bie, J. Yu, Challenges of Z-scheme photocatalytic mechanisms,
https://doi.org/10.1016/

973e983,

(2022)

Chem

4

Trends
j.trechm.2022.08.008.

[6] L. Wang, B. Cheng, L. Zhang, J. Yu, In situ irradiated XPS investigation on S-
scheme TiO2 @ZnIn2S4 photocatalyst for efﬁcient photocatalytic CO2 reduc-
tion, Small 17 (2021), 2103447, https://doi.org/10.1002/smll.202103447.
[7] Q. Xu, L. Zhang, B. Cheng, J. Fan, J. Yu, S-scheme heterojunction photocatalyst,
Chem 6 (2020) 1543e1559, https://doi.org/10.1016/j.chempr.2020.06.010.
[8] L. Zhang, J. Zhang, H. Yu, J. Yu, Emerging S-scheme photocatalyst, Adv. Mater.

34 (2022), 2107668, https://doi.org/10.1002/adma.202107668.

[9] B.T. Barrocas, N. Ambro(cid:3)zov(cid:1)a, K. Ko(cid:3)cí, Photocatalytic reduction of carbon di-
oxide on TiO2 heterojunction photocatalysts d a review, Materials 15 (2022)
967, https://doi.org/10.3390/ma15030967.

[10] K. Wang, Q. Li, B. Liu, B. Cheng, W. Ho, J. Yu, Sulfur-doped g-C3N4 with
enhanced photocatalytic CO2-reduction performance, Appl. Catal. B 176e177
(2015) 44e52, https://doi.org/10.1016/j.apcatb.2015.03.045.

[11] Z.-H. Wei, Y.-F. Wang, Y.-Y. Li, L. Zhang, H.-C. Yao, Z.-J. Li, Enhanced photo-
catalytic CO2 reduction activity of Z-scheme CdS/BiVO4 nanocomposite with
thinner BiVO4 nanosheets, J. CO2 Util. 28 (2018) 15e25, https://doi.org/
10.1016/j.jcou.2018.09.008.

[12] H. Yoneyama, Photoreduction of carbon dioxide on quantized semiconductor
nanoparticles in solution, Catal. Today 39 (1997) 169e175, https://doi.org/
10.1016/S0920-5861(97)00098-9.

[13] T. Baran, S. Wojtyła, A. Dibenedetto, M. Aresta, W. Macyk, Photocatalytic
carbon dioxide reduction at p-type copper(I) iodide, ChemSusChem 9 (2016)
2933e2938, https://doi.org/10.1002/cssc.201600289.

[14] H. Qin, Y. He, P. Xu, D. Huang, Z. Wang, H. Wang, Z. Wang, Y. Zhao, Q. Tian,
C. Wang, Spinel ferrites (MFe2O4): synthesis,
improvement and catalytic
application in environment and energy ﬁeld, Adv. Colloid Interface Sci. 294
(2021), 102486, https://doi.org/10.1016/j.cis.2021.102486.

[15] H. Han, Y. Luo, Y. Jia, N. Hasan, C. Liu, A review on SnFe2O4 and their com-
posites: synthesis, properties, and emerging applications, Prog. Nat. Sci.:
Mater. Int. (2022), https://doi.org/10.1016/j.pnsc.2022.09.005.

[16] J. Guo, K. Wang, X. Wang, Photocatalytic reduction of CO2 with H2O vapor
under visible light over Ce doped ZnFe2O4, Catal. Sci. Technol. 7 (2017)
6013e6025, https://doi.org/10.1039/C7CY01869J.

[17] D. Santos-Carballal, A. Roldan, N.Y. Dzade, N.H. de Leeuw, Reactivity of CO2 on
the surfaces of magnetite (Fe3O4), greigite (Fe3S4) and mackinawite (FeS), Phil.
Trans. R. Soc. A 376 (2018), 20170065, https://doi.org/10.1098/rsta.2017.0065.
[18] Y. He, L. Zhang, M. Fan, X. Wang, M.L. Walbridge, Q. Nong, Y. Wu, L. Zhao, Z-
scheme SnO2(cid:2)x/g-C3N4 composite as an efﬁcient photocatalyst for dye
degradation and photocatalytic CO2 reduction, Sol. Energy Mater. Sol. Cells
137 (2015) 175e184, https://doi.org/10.1016/j.solmat.2015.01.037.

[19] C.G. Fonstad, R.H. Rediker, Electrical properties of high-quality stannic oxide
J. Appl. Phys. 42 (1971) 2911e2918, https://doi.org/10.1063/

crystals,
1.1660648.

[20] J.A. Torres, G.T.S.T. Da Silva, F. Barbosa de Freitas Silva, C. Ribeiro, Experi-
mental evidence of CO2 photoreduction activity of SnO2 nanoparticles,
ChemPhysChem
https://doi.org/10.1002/
cphc.202000786.

2392e2396,

(2020)

21

This work was supported by the National Science Center, Poland,

within Sheng program (grant no. 2018/30/Q/ST5/00776).

[21] A.H. Chowdhury, A. Das, S. Riyajuddin, K. Ghosh, S.M. Islam, Reduction of
carbon dioxide with mesoporous SnO2 nanoparticles as active photocatalysts
under visible light in water, Catal. Sci. Technol. 9 (2019) 6566e6569, https://
doi.org/10.1039/C9CY01568J.

8

K. Urbanek, K. Spilarewicz, J. Yu et al.

Materials Today Sustainability 22 (2023) 100386

[22] D. Zhang, High-performance Photoelectrocatalytic Reduction of CO2 by the
hydrophilicehydrophobic composite Cu-SnO2/ZIF-8, Int. J. Electrochem. Sci.
(2021), 150951, https://doi.org/10.20964/2021.01.08.

[23] P. Makuła, M. Pacia, W. Macyk, How to correctly determine the band gap
energy of modiﬁed semiconductor photocatalysts based on UVevis spectra,
Lett. 9 (2018) 6814e6817, https://doi.org/10.1021/
J. Phys. Chem.
acs.jpclett.8b02892.

[24] R. Adhikari, A.K. Das, D. Karmakar, T.V.C. Rao,

J. Ghatak, Structure and
magnetism of Fe-doped nanoparticles, Phys. Rev. B 78 (2008), 024404, https://
doi.org/10.1103/PhysRevB.78.024404.

[25] D. Sherwood, P. Dalby (Eds.), Modern Thermodynamics for Chemists and
Biochemists, Oxford University Press, 2018, https://doi.org/10.1093/oso/
9780198782957.003.0002.

[26] L. Tan, L. Wang, Y. Wang, Hydrothermal synthesis of SnO2 nanostructures
with different morphologies and their optical properties, J. Nanomater. 2011
(2011), e529874, https://doi.org/10.1155/2011/529874.

[27] W.-W. Wang,

J.-L. Yao, Synthesis of magnetically separable Sn doped
magnetite/silica coreeshell structure and photocatalytic property, Mater. Res.
Bull. 45 (2010) 710e716, https://doi.org/10.1016/j.materresbull.2010.02.017.
[28] X. Liang, Y. Zhong, S. Zhu, H. He, P. Yuan, J. Zhu, Z. Jiang, The valence and site
occupancy of substituting metals in magnetite spinel structure Fe3(cid:2)xMxO4
(M ¼ Cr, Mn, Co and Ni) and their inﬂuence on thermal stability: an XANES
and TG-DSC investigation, Solid State Sci. 15 (2013) 115e122, https://doi.org/
10.1016/j.solidstatesciences.2012.10.005.

[29] C. Leostean, O. Pana, M. Stefan, A. Popa, D. Toloman, M. Senila, S. Gutoiu,
S. Macavei, New properties of Fe3O4@SnO2 core shell nanoparticles following
interface charge/spin transfer, Appl. Surf. Sci. 427 (2018) 192e201, https://
doi.org/10.1016/j.apsusc.2017.07.267.

[30] J. Hu, Y. Wang, W. Wang, Y. Xue, P. Li, K. Lian, L. Chen, W. Zhang, S. Zhuiykov,
Enhancement of the acetone sensing capabilities to ppb detection level by Fe-
doped three-dimensional SnO2 hierarchical microstructures fabricated via a
hydrothermal method, J. Mater. Sci. 52 (2017) 11554e11568, https://doi.org/
10.1007/s10853-017-1319-8.

[31] X. Zheng, J. Cai, W. Zhao, S. Liang, Y. Zheng, Y. Cao, L. Shen, Y. Xiao, L. Jiang,
Porous a-Fe2O3/SnO2 nanoﬂower with enhanced sulfur selectivity and sta-
bility for H2S selective oxidation, Chin. Chem. Lett. 32 (2021) 2143e2150,
https://doi.org/10.1016/j.cclet.2020.11.017.

[32] M.-M. Bagheri-Mohagheghi, N. Shahtahmasebi, M.R. Alinejad, A. Yousseﬁ,
M. Shokooh-Saremi, Fe-doped SnO2 transparent semi-conducting thin ﬁlms
deposited by spray pyrolysis technique: thermoelectric and p-type conduc-
tivity properties, Solid State Sci. 11 (2009) 233e239, https://doi.org/10.1016/
j.solidstatesciences.2008.05.005.

[33] L. Diamandescu, D. Mihǎilǎ-Tǎrǎbǎs¸ anu, V. Teodorescu, N. Popescu-Pogrion,
Hydrothermal synthesis and structural characterization of some substituted
magnetites, Mater. Lett. 37 (1998) 340e348, https://doi.org/10.1016/
S0167e577X(98)00117-7.

[34] M.A. Shipilin, I.N. Zakharova, A.M. Shipilin, V.I. Bachurin, M€ossbauer studies of
magnetite nanoparticles, J. Synch. Investig. 8 (2014) 557e561, https://doi.org/
10.1134/S1027451014030343.

[35] I.S. Lyubutin, C.R. Lin, YuV. Korzhetskiy, T.V. Dmitrieva, R.K. Chiang,
M€ossbauer spectroscopy and magnetic properties of hematite/magnetite
nanocomposites, J. Appl. Phys. 106 (2009), 034311, https://doi.org/10.1063/
1.3194316.

[36] M. Sorescu, L. Diamandescu, D. Tarabasanu-Mihaila, V.S. Teodorescu,
B.H. Howard, Hydrothermal synthesis and structural characterization of (1(cid:2)x)
a-Fe2O3exSnO2 nanoparticles, Solids 65 (2004) 1021e1029, https://doi.org/
10.1016/j.jpcs.2003.10.062.

[37] A.M. Gismelseed, A.A. Yousif, A.D. Al-Rawas, M.E. Elzain,

I. Ayub,
H.M. Widatallah, F.J. Berry, in: M.F. Thomas, J.M. Williams, T.C. Gibb (Eds.),
M€ossbauer Studies of
the Tetravalent Doped Magnetite, Hyperﬁne In-
teractions (C), Springer Netherlands, Dordrecht, 2002, pp. 49e52, https://
doi.org/10.1007/978-94-010-0281-3_13.

[38] M.S. Pereira, F.A.S. Lima, T.S. Ribeiro, M.R. da Silva, R.Q. Almeida, E.B. Barros,
I.F. Vasconcelos, Application of Fe-doped SnO2 nanoparticles in organic solar

cells with enhanced stability, Opt. Mater. 64 (2017) 548e556, https://doi.org/
10.1016/j.optmat.2017.01.023.

[39] C.E.R. Torres, A. Fabiana Cabrera, F.H. S(cid:1)anchez, Magnetic behavior of nano-
clusters of Fe-doped SnO2, Physica B 389 (2007) 176e179, https://doi.org/
10.1016/j.physb.2006.07.051.

[40] V. Bilovol, S. Ferrari, F.D. Saccone, L.G. Pampillo, Effect of the dopant on the
structural and hyperﬁne parameters of Sn0.95M0.05O2 nanoparticles (M: V, Mn,
Fe, Co), Mater. Res. Express 6 (2019), 0850h6, https://doi.org/10.1088/2053-
1591/ab29cc.

[41] K. Nomura, E. Kuzmann, C.A. Barrero, S. Stichleutner, Z. Homonnay, 119Sn
M€ossbauer study of solegel synthetized FexSbySn1(cid:2)x(cid:2)yO2(cid:2)d powders, Hyper-
ﬁne Interact. 184 (2008) 57e62, https://doi.org/10.1007/s10751-008-9766-x.
[42] M.C. Biesinger, B.P. Payne, A.P. Grosvenor, L.W.M. Lau, A.R. Gerson, R. St,
C. Smart, Resolving surface chemical states in XPS analysis of ﬁrst row tran-
sition metals, oxides and hydroxides: Cr, Mn, Fe, Co and Ni, Appl. Surf. Sci. 257
(2011) 2717e2730, https://doi.org/10.1016/j.apsusc.2010.10.051.

[43] C. Gu, W. Guan, J.-J. Shim, Z. Fang, J. Huang, Size-controlled synthesis and
electrochemical performance of porous Fe2O3/SnO2 nanocubes as an anode
material for lithium ion batteries, CrystEngComm 19 (2017) 708e715, https://
doi.org/10.1039/C6CE02288J.

[44] J. Moulder, W. Stickle, W. Sobol, K.D. Bomben, Handbook of X-Ray Photo-
electron Spectroscopy, Undeﬁned, 1992. https://www.semanticscholar.org/
paper/Handbook-of-X-Ray-Photoelectron-Spectroscopy-Moulder-Stickle/
6165d59e158c88267b1154c167da68bfca644f4a. (Accessed 10 August 2021).
[45] Y. Fu, N. Sun, L. Feng, S. Wen, Y. An, J. Liu, Local structure and magnetic
properties of Fe-doped SnO2 ﬁlms, J. Alloys Compd. 698 (2017) 863e867,
https://doi.org/10.1016/j.jallcom.2016.12.297.

[46] V.B.R. Boppana, R.F. Lobo, Photocatalytic degradation of organic molecules on
J. Catal. 281 (2011)

mesoporous visible-light-active Sn(II)-doped titania,
156e168, https://doi.org/10.1016/j.jcat.2011.04.014.

[47] W. Ben Haj Othmen, A. Hamdi, A. Addad, B. Sieber, H. Elhouichet, S. Szunerits,
R. Boukherroub, Fe-doped SnO2 decorated reduced graphene oxide nano-
composite with enhanced visible light photocatalytic activity, J. Photochem.
145e155, https://doi.org/10.1016/
Photobiol. A: Chem. 367
j.jphotochem.2018.08.016.

(2018)

[48] B.P. Payne, M.C. Biesinger, N.S. McIntyre, X-ray photoelectron spectroscopy
studies of reactions on chromium metal and chromium oxide surfaces,
J. Electron. Spectrosc. Relat. Phenom. 184 (2011) 29e37, https://doi.org/
10.1016/j.elspec.2010.12.001.

[49] F. Ooi, J.S. DuChene, J. Qiu, J.O. Graham, M.H. Engelhard, G. Cao, Z. Gai,
W.D. Wei, A facile solvothermal synthesis of octahedral Fe3O4 nanoparticles,
Small 11 (2015) 2649e2653, https://doi.org/10.1002/smll.201401954.
[50] H. Fatima, D.-W. Lee, H.J. Yun, K.-S. Kim, Shape-controlled synthesis of mag-
netic Fe3O4 nanoparticles with different iron precursors and capping agents,
RSC Adv. 8 (2018) 22917e22923, https://doi.org/10.1039/C8RA02909A.
[51] K.M.Ø. Jensen, M. Christensen, P. Juhas, C. Tyrsted, E.D. Bøjesen, N. Lock,
S.J.L. Billinge, B.B. Iversen, Revealing the mechanisms behind SnO2 nano-
particle formation and growth during hydrothermal synthesis: an in situ total
scattering study, J. Am. Chem. Soc. 134 (2012) 6785e6792, https://doi.org/
10.1021/ja300978f.

[52] B. Cojocaru, D. Avram, V. Kessler, V. Parvulescu, G. Seisenbaeva, C. Tiseanu,
Nanoscale insights into doping behavior, particle size and surface effects in
trivalent metal doped SnO2, Sci. Rep. 7 (2017) 9598, https://doi.org/10.1038/
s41598-017-09026-2.

[53] X. Wang, S.O. Pehkonen, J. R€am€o, M. V€a€an€anen, J.G. Highﬁeld, K. Laasonen,
Experimental and computational studies of nitrogen doped Degussa P25 TiO2:
application to visible-light driven photo-oxidation of As(III), Catal. Sci. Tech-
nol. 2 (2012) 784, https://doi.org/10.1039/c2cy00486k.

[54] M. Tang, Y. Xia, D. Yang, S. Lu, X. Zhu, R. Tang, W. Zhang, Ag decoration and SnO2
coupling modiﬁed anatase/rutile mixed crystal TiO2 composite photocatalyst for
enhancement of photocatalytic degradation towards tetracycline hydrochloride,
Nanomaterials 12 (2022) 873, https://doi.org/10.3390/nano12050873.

[55] L.M. Peter, Dynamic aspects of semiconductor photoelectrochemistry, Chem.

Rev. 90 (1990) 753e769, https://doi.org/10.1021/cr00103a005.

9

