# RearCircuitBoard_10 – Bestellliste der Stecker

Platine RearCircuitBoard_10, Entwurf 0.12 (seit 09.11.2026 mit J23, Reset der Synchronsteuerungen; J15 fünfpolig, Raster 3,81 mm, seit 3.11.2026). JLCPCB liefert keine Teile lose mit. Die Stecker deshalb **bei LCSC**
bestellen und die Bestellung mit dem JLCPCB-Auftrag zusammenlegen (ein Paket), oder bei einem Händler mit Lieferung an
Privatkunden. Vor einer Bestellung der Platine gelten die offenen Punkte der README (Messplan P9, knappe Bauteile wie
TPS259470).

Bestand und Preise bei LCSC abgefragt am **13.10.2026 um 22:17 MESZ**; Preise der Alternativen vom 7.10.2026 (brutto,
DigiKey netto als **Annahme**), siehe README „Von Hand bestückte Teile und Bezugsquellen“. Seit 03.11.2026 ist J15 fünfpolig
im Raster 3,81 mm (Windsensoren mit Versorgung; Verwechslungsschutz); Mengen dafür angepasst, LCSC-Preise nicht neu
abgefragt, Preise der neuen Zeilen von JLCPCB (Bestand bei JLCPCB am 03.11.2026: C440848 8 363, C440850 1 332,
C441172 12 835, C441174 3 168, C441185 5 408, C440861 5 122). Zeilen J23 (Entwurf 0.12): LCSC und JLCPCB abgefragt am
09.11.2026 um 17:59 MEZ. Vor der Bestellung erneut prüfen.

## Bestellung bei LCSC (empfohlen) – Mengen für 2 Platinen

„bestellen“ = gebraucht, aufgerundet auf die Mindestmenge von LCSC.

| Klemme | Stecker (Kefa) | LCSC | je Platine | für 2 | **bestellen** | Preis je Stück | Bestand |
|---|---|---|---:|---:|---:|---:|---:|
| J7–J10 Endschalter | KF2EDGK-3.5-2P | C440847 | 4 | 8 | **8** | 0,2149 USD | 16 355 |
| J22 Hall | KF2EDGK-3.5-3P | C440848 | 1 | 2 | **5** | 0,2914 USD | 10 715 |
| J23 RST (seit 0.12) | KF2EDGK-3.5-4P | C440849 | 1 | 2 | **2** | 0,4128 USD | 14 175 |
| J14 Leuchten | KF2EDGK-3.5-5P | C440850 | 1 | 2 | **2** | 0,4697 USD | 2 174 |
| J15 Windsensoren (Raster 3,81 mm) | KF2EDGK-3.81-5P | C440861 | 1 | 2 | **2** | 0,3469 USD (JLCPCB) | 5 122 (JLCPCB) |
| J2 Sonnensensor | KF2EDGK-3.5-6P | C440851 | 1 | 2 | **2** | 0,5376 USD | 1 615 |
| J11 24 V | KF2EDGK-5.08-2P-AA | C440880 | 1 | 2 | **5** | 0,1568 USD | 74 440 |
| J3/J4 Elevation (zweireihig) | KF2EDGKS-3.5-2*2P (Federanschluss) | C2923215 | 2 | 4 | **4** | 0,7877 USD | 764 |
| J5/J6 Azimut (zweireihig) | KF2EDGKS-3.5-2*3P (Federanschluss) | C2923216 | 2 | 4 | **4** | 1,1954 USD | 680 |
| J16/J21 Steckbrücken 2,54 mm | – | C5305 | 2 | 4 | **50** | 0,0099 USD | 891 350 |

Summe der Stecker und Brücken: etwa 15,10 USD netto (seit 03.11.2026; vorher 14,40 USD; Schätzung), mit J23 (seit 09.11.2026)
etwa 15,93 USD netto (Schätzung).

Der Stecker für **J22** (C440848) ist das Gegenstück zum Kabel vom HallTapBoard (dort J3). Braucht eine Platine keinen
Hall-Abgriff, bleibt J22 frei. Den Stecker für **J23** (C440849) braucht nur, wer den Reset der Synchronsteuerung über J23
anschließt; bei „nur vertikal“ geht der Reset auch über J5, dann bleibt J23 frei.

**Nur bei der Bestückungsvariante „smd“** (Grundleisten lötest du selbst ein) zusätzlich:

| Klemme | Grundleiste (Kefa) | LCSC | je Platine | für 2 | **bestellen** | Preis je Stück | Bestand |
|---|---|---|---:|---:|---:|---:|---:|
| J7–J10 | KF2EDGR-3.5-2P | C441171 | 4 | 8 | **10** | 0,0503 USD | 12 310 |
| J22 | KF2EDGR-3.5-3P | C441172 | 1 | 2 | **5** | 0,0751 USD | 1 705 |
| J23 (seit 0.12) | KF2EDGR-3.5-4P | C441173 | 1 | 2 | **5** | 0,1110 USD | 9 055 |
| J14 | KF2EDGR-3.5-5P | C441174 | 1 | 2 | **5** | 0,1268 USD | 4 790 |
| J15 (Raster 3,81 mm) | KF2EDGR-3.81-5P | C441185 | 1 | 2 | **2** | 0,1473 USD (JLCPCB) | 5 408 (JLCPCB) |
| J2 | KF2EDGR-3.5-6P | C441175 | 1 | 2 | **5** | 0,1619 USD | 3 970 |
| J11 (mit Stirnwänden) | KF2EDGRC-5.08-2P | C441236 | 1 | 2 | **10** | 0,0598 USD | 14 280 |
| J3/J4 | KF2EDGSR-3.5-2*2P | C2923260 | 2 | 4 | **4** | 0,5818 USD | 1 181 |
| J5/J6 | KF2EDGSR-3.5-2*3P | C2923261 | 2 | 4 | **4** | 0,8418 USD | 1 419 |
| J16/J21 Stiftleiste 1 × 3 | PZ254V-11-03P | C2937625 | 2 | 4 | **50** | 0,0199 USD | 825 150 |

Summe der Grundleisten: etwa 9,90 USD netto (seit 03.11.2026, Schätzung), mit J23 (seit 09.11.2026) etwa 10,46 USD netto
(Schätzung). Bei der Variante **„voll“** lötet JLCPCB die Grundleisten selbst ein.

Die übrigen Handteile (Stiftleiste J1 zum Board, Distanzbolzen, Wärmeleitpads, Abstandsbolzen, Schrauben) stehen in
der README unter „Von Hand bestückte Teile und Bezugsquellen“.

## Alternative mit Lieferung an Privatkunden (Phoenix Contact)

| Stecker für | Händler und Typ | Preis je Stück |
|---|---|---:|
| J7–J10 | Reichelt MC 2 ST 3,5 (Phoenix 1840366) | 1,40 € |
| J22 | Reichelt MC 3 ST 3,5 (Phoenix 1840379) | 1,99 € |
| J23 | Reichelt MC 4 ST 3,5 (Phoenix 1840382), Grundleiste MC 4 G 3,5 (Phoenix 1844236, 0,99 €) | 2,65 € (abgerufen 09.11.2026) |
| J14 | Reichelt MC 5 ST 3,5 (Phoenix 1840395) | 3,45 € |
| J15 | Reichelt MC 5 ST 3,81 (Phoenix MC 1,5/ 5-ST-3,81), Grundleiste MC 5 G 3,81 | Preis nicht abgerufen (03.11.2026) |
| J2 | Reichelt MC 6 ST 3,5 (Phoenix 1840405) | 3,99 € |
| J11 | Reichelt MSTB 2-ST 5,08 (Phoenix 1757019) | 1,40 € |
| J3/J4 | DigiKey DFMC 1,5/2-ST-3,5 (Phoenix 1790108), **Annahme** netto; Bürklin 62P6731 | 2,68 € / 3,43 € |
| J5/J6 | DigiKey DFMC 1,5/3-ST-3,5 (Phoenix 1790111), **Annahme** netto; Bürklin 62P6743 | 4,18 € / 5,13 € |
| Steckbrücken | Reichelt JUMPER 2,54 SW | 0,02 € |

Grundleisten als Alternative (nur „smd“) stehen in derselben README-Tabelle.

**Wichtig – nicht mischen:** Am sichersten passen Stecker und Grundleiste **desselben Herstellers**. Bei der Variante
„voll“ sitzen Kefa-Grundleisten auf der Platine, dann Kefa-Stecker von LCSC nehmen. Dass Phoenix-Stecker in
Kefa-Grundleisten passen, ist eine **Annahme** (für J11 ist nur der Footprint geprüft, E35). Die zweireihigen
Klemmen J3–J6 haben eine eigene Belegung (README, „Verwechslungsschutz der Stecker“).

## Nach dem Erhalt prüfen

1. Jeden Stecker einmal in seine Grundleiste stecken. *Erwartet:* Er rastet ohne Kraft ein, sitzt bündig, kein Pin bleibt frei.
2. Die Stecker beschriften (z. B. „J7 oben“, „J22 HALL“), bevor die Kabel angeschlossen werden.

---

© Silvio Sternitzke, 10/2026 · Samba Solar Track · Lizenz CC BY-NC-SA 4.0 (keine kommerzielle Verwendung,
Nachbau für private Zwecke erlaubt), siehe [LIZENZ.md](../../LIZENZ.md)
