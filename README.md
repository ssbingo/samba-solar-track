# Samba Solar Track

**© Silvio Sternitzke, 10/2026** · Lizenz CC BY-NC-SA 4.0 (keine kommerzielle Verwendung, Nachbau für private
Zwecke erlaubt), siehe [LIZENZ.md](LIZENZ.md)

Samba Solar Track ist eine Solarnachführung mit Sturmschutz für bewegliche Aufständerungen von Solarmodulen:
nur vertikal (1 Achse, Elevation) oder vertikal + horizontal (2 Achsen, Elevation und Azimut). Sie besteht aus
einem gekauften Waveshare ESP32-P4-WIFI6-Touch-LCD-10.1 (10,1-Zoll-Touch-Display) und einer eigenen Platine, die Sensoren, Schaltausgänge und
Meldeleuchten trägt. Dieses Repository enthält ausschließlich, was du für den Nachbau der Steuerung brauchst:
Handbuch, Platinen und Gehäuse.

**Stand: Release 0.5.2** (erzeugt aus dem Projekt am 28.10.2026)

## Inhalt

| Ordner | Inhalt |
|---|---|
| `handbuch/` | Handbuch für Anwender als HTML (Startseite `handbuch/index.html`) und als PDF |
| `hardware/RearCircuitBoard_10/` | Platine zum Waveshare ESP32-P4-WIFI6-Touch-LCD-10.1: KiCad-Projekt, Fertigungsdaten für JLCPCB, Stückliste, Vorschaubilder, Steckerliste |
| `hardware/HallTapBoard/` | kleine Platine für den Abgriff der Hall-Signale an der Synchronsteuerung, mit Gehäuse zum 3D-Druck |
| `gehaeuse/` | Rückgehäuse und Bohrschablone für das 10,1-Zoll-Board (STL, 3MF, PDF) |

## Firmware

Die Firmware gibt es nur fertig kompiliert. Die Steuerung holt neue Versionen selbst über das Internet
(Einrichtung → FIRMWARE); die Dateien für das erste Aufspielen liegen unter <https://firmware.samba-solar.de/>
(Repository [ssbingo/samba-solar-track-firmware](https://github.com/ssbingo/samba-solar-track-firmware)).
Wie du sie zum ersten Mal aufspielst, steht im Handbuch („Die Firmware zum ersten Mal aufspielen“).

## Lizenz

Platinen, Zeichnungen, Gehäuse, Handbuch und Logo stehen unter **CC BY-NC-SA 4.0**: privater Nachbau erlaubt,
keine kommerzielle Verwendung durch Dritte. Einzelheiten in [LIZENZ.md](LIZENZ.md), Lizenztext in [LICENSE](LICENSE).

---

© Silvio Sternitzke, 10/2026 · Samba Solar Track · Lizenz CC BY-NC-SA 4.0 (keine kommerzielle Verwendung,
Nachbau für private Zwecke erlaubt), siehe [LIZENZ.md](LIZENZ.md)
