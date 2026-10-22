# Gehäuse HallTapBoard (Entwurf 0.4)

3D-Druck-Gehäuse für die Platine HallTapBoard (Entwurf 0.4, 70 × 40 mm). **Nur am Rechner entworfen: nicht
gedruckt, nicht gemessen, nicht erprobt.** Maße, die nicht aus einer Herstellerangabe stammen, sind in
`tools/halltap_gehaeuse.py` als ANNAHME markiert.

| Datei | Inhalt |
|---|---|
| `HallTapBoard-gehaeuse-unterteil.step` / `.stl` | Grundgehäuse (Boden auf dem Druckbett) |
| `HallTapBoard-gehaeuse-deckel.step` / `.stl` | Deckel, schon in Druckrichtung (Oberseite auf dem Druckbett) |
| `vorschau-*.png` | offen mit Platine, geschlossen, Deckel von oben, Schnitt durch D9 „24V“ und durch die mittlere Verschraubung |

Erzeugt mit (CadQuery 2.8.0 in einer eigenen Umgebung):

```
python3 -m venv ~/.local/share/samba-solar-track/cad-venv
~/.local/share/samba-solar-track/cad-venv/bin/pip install cadquery==2.8.0 cairosvg
~/.local/share/samba-solar-track/cad-venv/bin/python tools/halltap_gehaeuse.py
```

Maße: außen 98 × 82 × 40 mm (ohne Laschen; mit Laschen 122 mm breit), innen 92 × 76 × 34 mm, Wände und Boden 3 mm.
Drei runde Bohrungen 18,9 mm (beim Druck mit Stützmaterial) für Kabelverschraubungen PG 11 in der vorderen Wand, acht Bohrungen 4,0 mm für
Gewindeeinsätze ruthex M3 (RX-M3x5,7), je ein Lichtschacht über den Meldeleuchten D9 „24V“ (gelb) und D4 „5V OK“ (grün), 8 mm
auseinander, die Bedeutung als Prägung daneben (seit Entwurf 0.3). Prägungen fett, 1,0 mm tief, auf dem Deckel 6 mm hoch (seit 14.10.2026).
Tipp: Beim Deckel nach 1,0 mm einen Farbwechsel einstellen, dann ist die Schrift zweifarbig.

**Lichtleiter (seit Entwurf 0.4):** In jeden Schacht kommt ein **PMMA-Rundstab (Acrylglas) Ø 3,0 mm, Länge 26,0 mm**,
Enden geschliffen und poliert. Er wird von oben eingedrückt, schließt bündig mit der Deckeloberseite ab und endet
1,55 mm über der Leuchte (Schacht bis 2,4 mm über der Platine, Leuchte 0,85 mm hoch). Die Bohrung ist mit 3,2 mm
gezeichnet: Senkrechte Löcher werden im FDM-Druck meist 0,1–0,2 mm kleiner (**Annahme**), der Stab sitzt dann mit
leichtem Presssitz bis Schiebesitz. Zu stramm: mit einem Bohrer 3,1 mm von Hand nacharbeiten; zu lose: oben ein
Tropfen klarer Kleber (kein Sekundenkleber, er trübt PMMA; **Annahme**).

Teileliste, Druckhinweise und Montage: README, Abschnitt „Platine HallTapBoard“ → „Gehäuse“, und Handbuch der 10-Zoll-Version,
Kapitel „Das HallTapBoard im Steuerkasten“.

© Silvio Sternitzke, 10/2026 · Samba Solar Track · Lizenz CC BY-NC-SA 4.0: keine kommerzielle Verwendung durch
Dritte, privater Nachbau erlaubt (siehe [LIZENZ.md](../../../LIZENZ.md))
