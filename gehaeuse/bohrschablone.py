# © Silvio Sternitzke, 10/2026 · Samba Solar Track · Lizenz CC BY-NC-SA 4.0: keine kommerzielle Verwendung, privater Nachbau erlaubt
"""
Bohrschablone (A4 quer, 1:1) für die Wandaufhängung des Rückwandgehäuses.
Liest die Parameter aus rueckgehaeuse.py.  Aufruf: python3 bohrschablone.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

exec(open("rueckgehaeuse.py").read().split("if __name__")[0])

PW, PH = 297.0, 210.0                     # A4 quer in mm
cx, y_screw = PW / 2, 160.0               # Schraubenlinie auf der Seite
y_screw_rel = KEYHOLE_Y + KEY_SLOT_LEN    # Schraube relativ zur Gehäusemitte im eingehängten Zustand
cy = y_screw - y_screw_rel                # Gehäusemitte auf der Seite

fig = plt.figure(figsize=(PW / 25.4, PH / 25.4))
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, PW); ax.set_ylim(0, PH); ax.set_aspect("equal"); ax.axis("off")

# Gehäuseumriss gespiegelt = Ansicht von vorn (Raumseite), Aussparung dann rechts
for p in outline.to_polygons():
    xs = [cx - x for x, y in p] + [cx - p[0][0]]
    ys = [cy + y for x, y in p] + [cy + p[0][1]]
    ax.plot(xs, ys, color="0.6", lw=0.6, ls="--")
ax.text(cx, cy - 60, "Umriss Gehäuse im eingehängten Zustand (Ansicht von vorn)", ha="center", va="center", fontsize=8, color="0.5")

# Schraubenpositionen
for kx in KEYHOLES_X:
    x = cx - kx
    ax.add_patch(Circle((x, y_screw), 2.0, fill=False, lw=0.8))
    ax.add_patch(Circle((x, y_screw), 4.5, fill=False, lw=0.4, ls=":"))
    ax.plot([x - 7, x + 7], [y_screw, y_screw], "k", lw=0.5); ax.plot([x, x], [y_screw - 7, y_screw + 7], "k", lw=0.5)
ax.plot([cx - 120, cx + 120], [y_screw, y_screw], "k", lw=0.3)       # Bezugslinie für die Wasserwaage
span = KEYHOLES_X[1] - KEYHOLES_X[0]
ax.annotate("", (cx - span / 2, y_screw + 9), (cx + span / 2, y_screw + 9), arrowprops=dict(arrowstyle="<->", lw=0.6))
ax.text(cx, y_screw + 11, f"{span:.1f} mm".replace(".", ","), ha="center", va="bottom", fontsize=9)
ax.text(cx, y_screw - 9,
        f"Bohrlöcher: Dübel + Schraube Ø 4 mm, Kopf Ø ≤ {KEY_HEAD_D - 1:.0f} mm, Kopfhöhe ≤ {KEY_POCKET - 0.4:.0f} mm  –  "
        "Kopfunterseite ca. 2–2,5 mm vor der Wand stehen lassen", ha="center", va="top", fontsize=7.5)
ax.annotate("", (cx + 100, y_screw), (cx + 100, cy + D / 2), arrowprops=dict(arrowstyle="<->", lw=0.5))
ax.text(cx + 102, (y_screw + cy + D / 2) / 2, f"{D / 2 - y_screw_rel:.0f} mm bis Gehäuseoberkante", va="center", fontsize=7, rotation=90)

ax.text(cx, PH - 8, "Bohrschablone – Rückwandgehäuse ESP32-P4-WIFI6-Touch-LCD-10.1    ▲ OBEN", ha="center", va="top", fontsize=11, weight="bold")
ax.text(cx, PH - 15, "Drucken mit 100 % / „Tatsächliche Größe“ – Kontrollmaß unten prüfen", ha="center", va="top", fontsize=8)
ax.plot([20, 120], [12, 12], "k", lw=1.2); ax.plot([20, 20], [9, 15], "k", lw=1); ax.plot([120, 120], [9, 15], "k", lw=1)
ax.text(70, 15, "Kontrollmaß 100,0 mm", ha="center", va="bottom", fontsize=8)

fig.savefig("Bohrschablone_A4quer_ESP32-P4_10.1.pdf")
print("Bohrschablone_A4quer_ESP32-P4_10.1.pdf geschrieben")
