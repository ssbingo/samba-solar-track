# HallTapBoard – Bestellliste der Stecker

Platine HallTapBoard, Entwurf 0.5 (Musterbestellung zur Erprobung). JLCPCB liefert keine Teile lose mit. Die Stecker
deshalb **bei LCSC** bestellen und die Bestellung mit dem JLCPCB-Auftrag zusammenlegen (ein Paket), oder bei einem
Händler mit Lieferung an Privatkunden (Reichelt).

Bestand und Preise bei LCSC abgefragt am **13.10.2026 um 22:17 MESZ**; Reichelt-Preise vom 13.10.2026, 16:04 MESZ
(brutto). Vor der Bestellung erneut prüfen.

## Welche Klemme, welcher Stecker

| Klemme auf der Platine | Zweck | Raster | Pole | Grundleiste (auf der Platine) | **Stecker (dazu bestellen)** |
|---|---|---:|---:|---|---|
| J1 „+24V / 0V“ | Versorgung aus den 24 V der Antriebe | 5,08 mm | 2 | Kefa KF2EDGRC-5.08-2P | **Kefa KF2EDGK-5.08-2P-AA** |
| J2 „H1 H2 GND“ | Hall-Signale von der SCN4 | 3,81 mm | 3 | Kefa KF2EDGR-3.81-3P | **Kefa KF2EDGK-3.81-3P** |
| J3 „J22: A B GND“ | Kontakte zur Steuerung (J22 der RearCircuitBoard_10) | 3,5 mm | 3 | Kefa KF2EDGR-3.5-3P | **Kefa KF2EDGK-3.5-3P** |

Das unterschiedliche Raster von J2 (3,81 mm) und J3 (3,5 mm) ist Absicht: Die beiden 3-poligen Stecker lassen sich
nicht vertauschen. Kein VCC-Pin an J2: Die rote Ader (5 V) des Hall-Kabels wird **nicht** angeschlossen.

**Am anderen Ende des Kabels zur Steuerung** steckt ein zweiter Stecker KF2EDGK-3.5-3P in J22 der Platine
RearCircuitBoard_10. Er gehört zur Bestellung der RearCircuitBoard_10, ist hier aber mit aufgeführt, damit das Kabel
vollständig ist.

## Bestellung bei LCSC (empfohlen)

Mengen für **2 HallTapBoards**; LCSC verkauft diese Teile nur ab einer Mindestmenge, die Reserve kostet wenige Cent.

| LCSC-Nummer | Teil | gebraucht für 2 Platinen | **bestellen** (Mindestmenge) | Preis je Stück (Staffel ab Mindestmenge) | Bestand 13.10.2026 |
|---|---|---:|---:|---:|---:|
| C440880 | Stecker KF2EDGK-5.08-2P-AA (J1) | 2 | **5** | 0,1568 USD | 74 440 |
| C440859 | Stecker KF2EDGK-3.81-3P (J2) | 2 | **5** | 0,2339 USD | 12 540 |
| C440848 | Stecker KF2EDGK-3.5-3P (J3 und J22 am anderen Kabelende) | 2 + 2 | **5** | 0,2914 USD | 10 715 |

Summe der Stecker: etwa 3,41 USD netto (zuzüglich Versand und Einfuhrumsatzsteuer, mit dem JLCPCB-Paket).

**Nur bei der Bestückungsvariante „smd“** (Grundleisten lötest du selbst ein) zusätzlich:

| LCSC-Nummer | Teil | gebraucht für 2 Platinen | **bestellen** (Mindestmenge) | Preis je Stück | Bestand 13.10.2026 |
|---|---|---:|---:|---:|---:|
| C441236 | Grundleiste KF2EDGRC-5.08-2P (J1, mit Stirnwänden) | 2 | **10** | 0,0598 USD | 14 280 |
| C441183 | Grundleiste KF2EDGR-3.81-3P (J2) | 2 | **10** | 0,0691 USD | 14 760 |
| C441172 | Grundleiste KF2EDGR-3.5-3P (J3) | 2 | **5** | 0,0751 USD | 1 705 |

Bei der Variante **„voll“** lötet JLCPCB die Grundleisten selbst ein; dann nur die Stecker bestellen.

## Alternative mit Lieferung an Privatkunden (Reichelt, Phoenix Contact)

| Für | Reichelt (Phoenix Contact) | Preis je Stück |
|---|---|---:|
| Stecker J1 | MSTB 2,5/2-ST-5,08 (1757019) | 1,40 € |
| Stecker J2 | MC 1,5/3-ST-3,81 (1803581) | 1,99 € |
| Stecker J3 / J22 | MC 1,5/3-ST-3,5 („MC 3 ST 3,5“, 1840379) | 1,99 € |
| nur smd: Grundleiste J1 | MSTBA 2,5/2-G-5,08 (1757242) | 0,60 € |
| nur smd: Grundleiste J2 | MC 1,5/3-G-3,81 (1803280) | 0,87 € |
| nur smd: Grundleiste J3 | MC 1,5/3-G-3,5 („MC 3 G 3,5“, 1844223) | 0,87 € |

**Wichtig – nicht mischen:** Am sichersten passen Stecker und Grundleiste **desselben Herstellers**. Bei der Variante
„voll“ sitzen Kefa-Grundleisten auf der Platine, dann Kefa-Stecker von LCSC nehmen. Dass ein Phoenix-Stecker in eine
Kefa-Grundleiste passt, ist eine **Annahme** (nur der Footprint ist für J1 geprüft, das Zusammenstecken nicht). Wer bei
„smd“ die Phoenix-Grundleisten von Reichelt einlötet, nimmt auch die Phoenix-Stecker von Reichelt.

## Nach dem Erhalt prüfen

1. Jeden Stecker einmal in seine Grundleiste stecken. *Erwartet:* Er rastet ohne Kraft ein, sitzt bündig, kein Pin bleibt frei.
2. Den 3,81-mm-Stecker (J2) probeweise an J3 halten. *Erwartet:* Er passt nicht – das ist der Verwechslungsschutz.

---

© Silvio Sternitzke, 10/2026 · Samba Solar Track · Lizenz CC BY-NC-SA 4.0 (keine kommerzielle Verwendung,
Nachbau für private Zwecke erlaubt), siehe [LIZENZ.md](../../LIZENZ.md)
