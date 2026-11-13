# Gehäuse HallTapBoard (Stand 0.6, passt zur Platine Entwurf 0.6)

3D-Druck-Gehäuse für die Platine HallTapBoard (70 × 40 mm). **Stand 0.6 vom 12.11.2026: nur am Rechner geändert,
nicht gedruckt, nicht gemessen, nicht erprobt.** Es passt unverändert zur Platine Entwurf 0.6 (Bohrungen, Klemmen und
Leuchten liegen gleich). Das gedruckte Muster vom 15.10.2026 ist die ältere Fassung 0.4; die Fassung 0.5 hat der
Nutzer probegedruckt.

**Geändert am 12.11.2026 (0.5 → 0.6, Rückmeldung des Nutzers zum Probedruck):** Die Schrift auf der Rückwand lief über
die Ecken, die Schnur fiel aus der Nut, und an den Ecken musste die Schnur zu oft und zu eng um Kurven.

- **Form eines Industriegehäuses** (zweite Rückmeldung des Nutzers vom 12.11.2026: die zuerst außen angesetzten
  Säulen und Deckelohren sahen aus wie Spielzeug): außen ein Rechteck mit **gleichmäßig gerundeten Kanten**
  (senkrechte Kanten R 5,5 mm, obere Deckelkante R 1 mm, an der Trennfuge je eine Fase 0,5 mm, unten am Boden 0,8 mm),
  **Deckel deckungsgleich** mit dem Unterteil, keine angesetzten Säulen oder Ohren.
- Die vier **Schraubpunkte liegen in den Ecken innerhalb der Außenkontur**: Der Innenraum hat senkrecht mit 18,5 mm
  gerundete Ecken, das Material dazwischen ist die Eckverstärkung (volle Höhe). Jede Schraube sitzt im Mittelpunkt
  der äußeren Eckrundung, 5,5 mm von beiden Außenflächen; Wand um den Gewindeeinsatz nach außen 3,5 mm, zur Nut bzw.
  zum Innenraum 2,13 mm. Die Senkkopfschrauben liegen bündig im Deckel.
- Die Nut läuft als **glatter Umlauf innen an den Schrauben vorbei**, mit nur vier weiten Ecken (Mittellinie R 17,55 mm)
  und hält die Schnur mit einem **Hinterschnitt** (unten). Die Schrauben liegen außerhalb der Dichtung.
- Wo die Eckverstärkung neben die äußeren Verschraubungen reicht, ist eine **ebene Auflage für die Gegenmutter**
  freigeschnitten (Montagemaß 27,3 mm + 0,8 mm, 6 mm tief); das Werkzeug prüft, dass nichts die Muttern berührt.
- Folge: Die Platine lässt sich **senkrecht einlegen** (Kragen nur 3,5 mm breit, Ecken gerundet; an den Ecken der
  Platine bleiben 1,4 mm Luft); das versetzte Ansetzen und Schieben bis 0.5 entfällt.
- Rückwandschrift ohne das Wort „Entwurf“, keine Zeile reicht über die gerade Fläche der Rückwand.
- Innen 6 mm breiter (92 → 98 mm), damit die Gegenmuttern neben den Eckverstärkungen Platz haben.
- Zusätzlich je ein Druckprojekt nur mit dem Unterteil und nur mit dem Deckel.

**Geändert am 13.11.2026 (Rückwandschrift gedreht, Vorgabe des Nutzers):** Die Schrift auf der Rückwand ist um 180° gedreht und die Reihenfolge der Zeilen umgekehrt: Im Steuerkasten zeigt diese Wand nach oben, und die Schrift ist jetzt von vorn (Deckelseite) in Draufsicht auf die Wand lesbar, Oberkante der Buchstaben zum Boden, erste Zeile am Boden. Bisher las man sie nur von der Bodenseite her. Tiefe, Größen und Zeilenabstände unverändert.

**Geändert am 13.11.2026 (Druckprojekte):** Stützen leichter lösbar (Werte unten bei „Druckprojekte“), Rückmeldung des Nutzers zum Probedruck. Zusätzlich die drei Druckprojekte in einer zweiten Variante mit Schrift in einer zweiten Farbe (`…_Schrift-zweifarbig.3mf`, Wunsch des Nutzers); die Form der Teile ist unverändert.

**Geändert am 11.11.2026 (0.5, nach der Prüfung):** zwei ungewollte geschlossene Hohlräume in den hinteren Ecken des
Unterteils (zwischen den damals innen liegenden Säulen, Stegen und Wänden) gefüllt; im Druckprojekt 30 % Füllung am
Objekt (vorher galt der Profilwert 15 %); die Angaben zu den Stützen berichtigt (bisher verdreht).
Maße, die nicht aus einer Herstellerangabe stammen, sind in `tools/halltap_gehaeuse.py` als ANNAHME markiert.

| Datei | Inhalt |
|---|---|
| `HallTapBoard-gehaeuse_K2Plus_HyperPETG-CF_0.4mm.3mf` | Druckprojekt für Creality Print: Creality K2 Plus, Düse 0,4 mm, Hyper PETG-CF, „0.20mm High Quality“, beide Teile auf einer Platte |
| `HallTapBoard-gehaeuse-unterteil_K2Plus_HyperPETG-CF_0.4mm.3mf` | dasselbe nur mit dem Unterteil, in der Mitte der Platte (seit 0.6) |
| `HallTapBoard-gehaeuse-deckel_K2Plus_HyperPETG-CF_0.4mm.3mf` | dasselbe nur mit dem Deckel, in der Mitte der Platte (seit 0.6) |
| `…_Schrift-zweifarbig.3mf` (drei Dateien) | dieselben drei Druckprojekte, Schrift mit Filament 2 (zweite Farbe über das CFS), seit 13.11.2026 |
| `HallTapBoard-gehaeuse-unterteil.step` / `.stl` | Grundgehäuse (Boden auf dem Druckbett) |
| `HallTapBoard-gehaeuse-deckel.step` / `.stl` | Deckel, schon in Druckrichtung (**Außenseite oben**, Innenseite auf Stützen) |
| `vorschau-*.png` | offen mit Platine, geschlossen, Deckel von oben, Schnitt durch D9 „24V“ und durch die mittlere Verschraubung |

Erzeugt mit (CadQuery 2.8.0 in einer eigenen Umgebung):

```
python3 -m venv ~/.local/share/samba-solar-track/cad-venv
~/.local/share/samba-solar-track/cad-venv/bin/pip install cadquery==2.8.0 cairosvg trimesh
~/.local/share/samba-solar-track/cad-venv/bin/python tools/halltap_gehaeuse.py
```

Maße: außen ohne Laschen 104 × 82 × 44 mm (bis 0.5 und im ersten Stand von 0.6: 98 × 82 × 44 mm, mit den Säulen
107 × 91 mm); Unterteil mit Laschen 128,0 × 82,0 × 41,0 mm (vorher 122,0 × 91,0 × 41,0 mm), Deckel mit Rand und
Lichtschacht 104,0 × 82,0 × 30,8 mm (vorher mit Ohren 107,0 × 91,0 × 30,8 mm); innen 98 × 76 × 38 mm (vorher
92 × 76 × 38 mm), Wände, Boden und Deckel 3 mm.
Drei runde Bohrungen 18,9 mm (beim Druck mit Stützmaterial) für Kabelverschraubungen PG 11 in der vorderen Wand, acht Bohrungen 4,0 mm für
Gewindeeinsätze ruthex M3 (RX-M3x5,7) – vier in den Domen der Platine, vier in den Eckverstärkungen –, je ein Lichtschacht
über den Meldeleuchten D9 „24V“ (gelb) und D4 „5V OK“ (grün), 8 mm auseinander.

**Dichtung (seit 0.5, Nut seit 0.6 neu):** Innen am oberen Rand des Unterteils ein Kragen (3,5 mm breit, 2,4 mm dick,
überall gleich breit, Ecken wie der Innenraum gerundet) mit einer Nut für eine **Rundschnur Ø 1,5 mm** (EPDM oder Silikon). Die Nut läuft als glatter
Umlauf mit vier weiten Ecken (Mittellinie R 17,55 mm, 11,7 × Schnurdurchmesser), ist **1,2 mm tief und unten 1,9 mm breit** und hat oben eine
schmale Öffnung in zwei Stufen zu 0,2 mm: **1,6 mm und 1,35 mm**. Die Schnur wird durch die Öffnung gedrückt und hält
sich dahinter (Hinterschnitt). Gedruckte Schlitze werden oft 0,1–0,2 mm enger (**Annahme**) – am Probedruck prüfen.
Die Schrauben liegen in den Eckverstärkungen außen neben der Nut, also außerhalb der Dichtung (mindestens 2,1 mm
Wand zwischen Einsatz und Nut). Länge der Schnur auf der Mittellinie **310 mm** (gebraucht etwa 31 cm), Verpressung 20 %, Füllung der Nut 84 % (das Werkzeug prüft 15–30 % und höchstens
85 %). Unter dem Kragen eine Schräge in Stufen von 0,2 mm (höchstens 45°) über 3,5 mm, damit er ohne Stützen druckbar ist. Der Deckel hat innen einen Führungsrand (1,6 × 2,0 mm, 0,3 mm Spiel), der innen am Kragen liegt.
Bis 0.5: Nut 2,0 × 1,1 mm ohne Hinterschnitt, innen an den Säulen vorbei, Schnur 357 mm; erster Stand von 0.6:
Säulen außen, Mittellinie R 7,05 mm, Schnur 316 mm.

**Deckel:** deckungsgleich mit dem Unterteil, vier **Senkkopfschrauben M3 × 10 ISO 10642** in den Ecken (seit 0.6
innerhalb der Kontur), Senkung 7,0 mm, Kopf bündig; 7 mm der Schraube stecken im Unterteil (Einsatz 5,7 mm, Bohrung
8 mm). Schrift **erhaben 0,8 mm**, fett (DejaVu Sans Bold):
„HallTapBoard“ 10 mm, „Samba Solar Track“ 6,5 mm, „24V“/„HALL“/„J22“ 7 mm, an den Leuchten 6,5 mm („24V“ unter dem
linken, „5V OK“ rechts neben dem rechten Schacht). Strichbreite mindestens 2,5 Düsenbahnen (das Werkzeug prüft).
Gedruckt wird der Deckel mit der Außenseite nach oben, die Schrift entsteht also frei als oberste Schichten.
Tipp: an der Oberseite der Deckplatte einen Farbwechsel einstellen, dann ist die Schrift zweifarbig.
Die Prägung auf der Rückwand des Unterteils bleibt vertieft (1,0 mm): „Samba Solar Track - HallTapBoard 0.6“ 4,0 mm,
„© Silvio Sternitzke, 10/2026“ 3,5 mm, „CC BY-NC-SA 4.0 - keine kommerzielle Verwendung“ 3,0 mm, alle innerhalb der
geraden Fläche zwischen den Eckrundungen (3 mm Rand; das Werkzeug setzt zu lange Zeilen kleiner).

**Lichtleiter:** In jeden Schacht kommt ein **PMMA-Rundstab (Acrylglas) Ø 3,0 mm, Länge 30,0 mm** (seit Entwurf 0.5;
vorher 26 mm), Enden geschliffen und poliert. Er wird von oben eingedrückt, schließt bündig mit der Deckeloberseite ab
und endet 1,55 mm über der Leuchte (Schacht bis 2,4 mm über der Platine, Leuchte 0,85 mm hoch). Die Bohrung ist mit
3,2 mm gezeichnet: Senkrechte Löcher werden im FDM-Druck meist 0,1–0,2 mm kleiner (**Annahme**), der Stab sitzt dann
mit leichtem Presssitz bis Schiebesitz. Zu stramm: mit einem Bohrer 3,1 mm von Hand nacharbeiten; zu lose: oben ein
Tropfen klarer Kleber (kein Sekundenkleber, er trübt PMMA; **Annahme**).

**Druckprojekte (3MF):** Profile aus Creality Print 7.3.0. Am Objekt gesetzt (in allen drei Projekten gleich):
5 Wandlinien, je 6 Boden- und Deckschichten, 30 % Füllung Gyroid, Stützen (Baum, automatisch). **Unterteil: Stützen
auch auf dem Modell** (`support_on_build_plate_only = 0`); sie entstehen nur in den drei PG-Bohrungen, weil die Stütze
dort auf dem unteren Bogen der Bohrung steht – mit „nur vom Druckbett“ bekämen die Bohrungen keine. **Deckel: Stützen
nur vom Druckbett** (`= 1`); die Innenseite steht auf Baumstützen, nur die beiden Lichtschächte berühren das Bett.
**Stützen leichter lösbar (seit 13.11.2026):** Spalt zwischen Stütze und Teil oben und unten 0,25 mm (Profil 0,2), je 1 Kontaktlage oben und unten (Profil 2), seitlicher Abstand 0,6 mm (Profil 0,35), Kontaktlagen rectilinear mit 50 mm/s (Profil auto, 80 mm/s), unabhängige Stützschichthöhe an. Am Filament: Düse 245 °C (Profil 250, erste Schicht bleibt 250), Lüfter bei den Kontaktlagen 100 %. Nach dem Slicen in der Schichtvorschau prüfen, dass zwischen Stütze und Teil eine Lage frei bleibt; rundet Creality Print die 0,25 auf 0,2 ab, auf 0,4 stellen. Filament vorher trocknen (60 °C, 8–12 h). Startwerte aus einer Recherche, für PETG belegt, für PETG-CF nicht erprobt (**Annahme**).
**Glattere Oberfläche (seit 13.11.2026):** Prozessprofil „0.20mm High Quality“ statt „0.20mm Standard“ (Außenwand 80 statt 200 mm/s, Linienbreite 0,40, Oberseite mit 2000 statt 5000 mm/s²), Wandreihenfolge innen/außen/innen. Schichthöhe bleibt 0,2 mm (Schräge unter dem Kragen in 0,2-mm-Stufen, Schrift 4 Schichten). Weitere Möglichkeiten (Bügeln, VFA-Test, Trocknen) im Bericht „Glatte Oberflächen K2 Plus PETG CF“; nicht erprobt (**Annahme**).
**Schrift zweifarbig (seit 13.11.2026):** Beide Filamente Hyper PETG-CF über das CFS; Filament 1 Gehäuse, Filament 2 Schrift. Hyper PETG-CF steht nicht in der Freigabeliste von Creality für das CFS (freigegeben ist Hyper PLA-CF; PET-CF gilt als „nicht empfohlen“, Verschleiß des PTFE-Schlauchs) – Einsatz auf eigenes Risiko. Die Farben im Projekt (dunkel/hell) sind Platzhalter: in Creality Print den CFS-Plätzen zuordnen. Auf dem Deckel ist die erhabene Schrift (0,8 mm) ein eigener Körper; da sie ganz oben liegt, gibt es nur einen Farbwechsel. In der Rückwand des Unterteils füllt eine Einlage die 1,0 mm tiefe Prägung bündig aus; sie reicht über z = 10,3 bis 27,7 mm, das sind etwa 87 Schichten mit je einem Farbwechsel (deutlich längere Druckzeit und Abfall im Schacht, die kleinste Zeile 3 mm hat Striche von etwa 0,5 mm, also nur eine Linie: **Annahme**, dass sie sauber wird). Wer das nicht will, druckt das Unterteil einfarbig und nur den Deckel zweifarbig. Prime Tower aus: Die K2 Plus spült beim Wechsel in den Abfallschacht; mit Prime Tower wirkt die unabhängige Stützschichthöhe nicht und der Stützspalt würde gerundet. Spülmengen dunkel → hell 400 mm³, hell → dunkel 150 mm³ (oberer Rand der Forenwerte 280–400 / 100–150 mm³, **Annahme**; bei Farbresten in der Schrift in Creality Print unter „Spülvolumen“ erhöhen).
Volumen bei 100 % Füllung (Stand 0.6): Unterteil 80,3 cm³, Deckel 27,6 cm³. Hyper PETG-CF braucht eine gehärtete
Düse; sein Profil nennt eine Erweichung bei 80 °C (nur 5 K über den angenommenen 75 °C im Steuerkasten). Einstellungen
nicht ausprobiert (**Annahme**).

**Montage, auf die man achten muss:** Die Platine wird seit 0.6 senkrecht von oben auf die Dome gelegt. Die Schnur
mit einem stumpfen Werkzeug (z. B. Rückseite eines Kunststoffspatels, **Annahme**) rundum durch die schmale Öffnung
in die Nut drücken; sie soll von selbst halten. Ein Maulschlüssel SW 24 lässt sich an den Gegenmuttern innen kaum
ansetzen: die Mutter mit Zange oder Fingern halten und außen anziehen, die mittlere Verschraubung zuerst. Der
Überstand der Stecker (im Werkzeug 9 mm) und der Platz zwischen Stecker und Gegenmutter (gerechnet 16 mm) sind
unbelegte **Annahmen**, wahrscheinlich bleiben nur etwa 12–14 mm; die Stecker liegen 6–10 mm seitlich versetzt zur
Verschraubung.

**Risiken (nicht erprobt):** Die Dichtfläche des Deckels entsteht auf Stützen und muss eben geschliffen werden; vier
Schrauben im 3 mm dicken Deckel verpressen die Schnur vermutlich nicht gleichmäßig (für 0.6 nicht neu gerechnet,
**offen**). Ob die Schnur im Hinterschnitt hält und sich noch eindrücken lässt, zeigt erst der Probedruck. Ein
Probedruck ist nötig; die Dichtheit ist nicht belegt, eine Schutzart wird nicht zugesagt.

Teileliste, Druckhinweise und Montage: README, Abschnitt „Platine HallTapBoard“ → „Gehäuse“, und Handbuch der 10-Zoll-Version,
Kapitel „Das HallTapBoard am Rack“.

© Silvio Sternitzke, 11/2026 · Samba Solar Track · Lizenz CC BY-NC-SA 4.0: keine kommerzielle Verwendung durch
Dritte, privater Nachbau erlaubt (siehe [LIZENZ.md](../../../LIZENZ.md))
