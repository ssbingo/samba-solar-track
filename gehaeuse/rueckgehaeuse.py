# © Silvio Sternitzke, 10/2026 · Samba Solar Track · Lizenz CC BY-NC-SA 4.0: keine kommerzielle Verwendung, privater Nachbau erlaubt
"""
Rückwandgehäuse für Waveshare ESP32-P4-WIFI6-Touch-LCD-10.1
Parametrisch, erzeugt STL/3MF via manifold3d (pip install manifold3d trimesh numpy)

Koordinaten: Ursprung = Mitte der Rückwand, z=0 = Außenseite Gehäuseboden,
z=H = Auflagekante an der Display-Rückwand.

Befestigung über die 8 Randbohrungen der Rückwand (je 4,5 mm vom Rand):
  - oben/unten: Abstand horizontal 195,20 mm, vertikal 155,00 mm
  - links/rechts: Abstand vertikal 109,00 mm, horizontal 236,20 mm
"""
import manifold3d as m3
import trimesh

# ---------------- Parameter ----------------
W, D       = 245.20, 164.00   # Außenmaß (= Rückwandkontur laut Zeichnung)
R_CORNER   = 4.50             # Eckradius der Rückwand (Zeichnung R4,50, vom Nutzer am 23.10.2026 bestätigt)
WALL       = 2.0              # Wandstärke
FLOOR      = 5.0              # Bodenstärke (verstärkt, trägt die Aufhängung)
H          = 40.0             # Gesamttiefe außen (23.10.2026: 40 statt 30 mm, Platz für Platine RearCircuitBoard_10 und PG 11)
CHAMFER    = 1.2              # Fase an der Bodenaußenkante

# Befestigungsbohrungen (Lochmitten)
HOLES_TB = [(sx * 195.20 / 2, sy * 155.00 / 2) for sx in (-1, 1) for sy in (-1, 1)]   # oben/unten
HOLES_LR = [(sx * 236.20 / 2, sy * 109.00 / 2) for sx in (-1, 1) for sy in (-1, 1)]   # links/rechts
HOLES = HOLES_TB + HOLES_LR

SCREW_D    = 3.2              # Durchgang M2.5; 2,8 mm waren gedruckt zu eng (Nutzer, 23.10.2026), 3,2 mm ANNAHME
HEAD_D     = 5.5              # Senkung für Zylinderkopf M2.5 (Kopf 4,5 mm), gedruckt mit Spiel, ANNAHME
POST_D     = 8.0              # Domdurchmesser (wird mit der Wand verschmolzen)
SCREW_GRIP = 4.0              # Material zwischen Kopfauflage und Display

# Aussparung links (aus Zeichnung): Stirnfläche 8,00 mm ab Frontrahmen = 5,50 mm ab Grundplattenkante.
# Übergang aus zwei tangentialen Bögen mit dem Eckradius (25.10.2026: der Kosinusverlauf war an den Enden nur etwa
# R 2,3 und passte gedruckt nicht; R 4,50 wie an den Ecken ist ANNAHME). Die Mitte des Übergangs bleibt bei |y| = 38,30 mm.
NOTCH_DEPTH  = 5.50
NOTCH_R      = 4.50
NOTCH_LEN    = (4 * NOTCH_R ** 2 - (2 * NOTCH_R - NOTCH_DEPTH) ** 2) ** 0.5   # Länge des Übergangs in y (8,29 mm)
NOTCH_STRAIT = 38.30 - NOTCH_LEN / 2
NOTCH_END    = 38.30 + NOTCH_LEN / 2

# Kabelverschraubungen unten (Vorgabe des Nutzers vom 23.10.2026): 6 × PG 11 in der unteren Wand (y = -D/2),
# Bohrung 18,9 mm wie beim Gehäuse des HallTapBoard. Die Gegenmuttern (SW 22, etwa 25,4 mm über Eck, ANNAHME nach
# üblichen PG-11-Muttern) liegen innen mit 31 mm Abstand (etwa 5,6 mm Luft); die äußeren enden 3,4 mm vor den Domen
# der unteren Befestigungspunkte (x = ±97,6 mm, Ø 8 mm).
PG_D       = 18.9
PG_PITCH   = 31.0
PG_X       = [(i - 2.5) * PG_PITCH for i in range(6)]
PG_Z       = FLOOR + (H - FLOOR) / 2   # Mitte der Wandhöhe innen

# Stabilisierungsstege innen (Trapez: unten RIB_DEPTH_BOT tief, oben RIB_DEPTH_TOP, endet RIB_GAP unter der Auflagekante)
RIB_T, RIB_DEPTH_BOT, RIB_DEPTH_TOP, RIB_GAP = 1.6, 6.0, 2.0, 1.0
RIBS_LONG_X  = (-50.0, 50.0)   # 2 an der oberen langen Seite; an der unteren sitzen die Verschraubungen
RIBS_SHORT_Y = (0.0,)          # je 1 an den kurzen Seiten (links/rechts)

# Aufhängung: 2 verdeckte Schlüssellöcher im oberen Bereich (Schraube Ø4 mm, Kopf bis Ø9 mm, Kopfhöhe bis 3,2 mm)
# Von außen: Einführloch (blind) + Schlitz nach oben durch die tragende Lippe; dahinter ein verdeckter Kopfkanal.
# Zum Innenraum geschlossen – dafür innen ein Verstärkungspad um jedes Schlüsselloch.
KEYHOLES_X   = (-80.0, 80.0)   # Lochabstand 160 mm, symmetrisch zur Mitte
KEYHOLE_Y    = 40.0            # Mitte Einführloch (oberer Bereich, +y = oben)
KEY_HEAD_D   = 10.0            # Einführloch und Kopfkanal
KEY_SLOT_W   = 4.6             # Schlitz für den Schraubenschaft
KEY_SLOT_LEN = 12.0            # Schlitzlänge nach oben
KEY_LIP      = 2.0             # tragende Lippe außen
KEY_POCKET   = 3.4             # Höhe des verdeckten Kopfkanals (Kopfhöhe + Spiel)
KEY_CEIL     = 2.0             # Decke über dem Kopfkanal zum Innenraum
KEY_RIDGE    = 1.0             # Grat oben am Dach des Kopfkanals: Dach mit 45° statt flacher Decke, damit der Kanal ohne
                               # Stützen druckt (Boden liegt auf dem Bett; Vorgabe 26.10.2026)
KEY_ROOF     = (KEY_HEAD_D - KEY_RIDGE) / 2   # Höhe des Dachs (4,5 mm)
KEY_PAD_WALL = 3.0             # Wandstärke des Verstärkungspads um den Kanal

# Lüftungsschlitze im Boden
VENT_FIELDS = [(sx * 100.0, sy * 62.0) for sx in (-1, 1) for sy in (-1, 1)]   # alle 4 Ecken
VENT_SLOTS, VENT_LEN, VENT_W, VENT_PITCH = 5, 24.0, 2.0, 4.0
# -------------------------------------------

SEG = 64
CS, M = m3.CrossSection, m3.Manifold


def rrect(w, d, r):
    return CS.square((w - 2 * r, d - 2 * r), center=True).offset(r, m3.JoinType.Round, circular_segments=SEG)


def notch_poly():
    import math
    x_edge = -W / 2
    def xf(y):
        a = abs(y)
        if a <= NOTCH_STRAIT:
            return x_edge + NOTCH_DEPTH
        if a >= NOTCH_END:
            return x_edge
        if a <= NOTCH_STRAIT + NOTCH_LEN / 2:   # Bogen an der Stirnfläche
            return x_edge + NOTCH_DEPTH - NOTCH_R + math.sqrt(NOTCH_R ** 2 - (a - NOTCH_STRAIT) ** 2)
        return x_edge + NOTCH_R - math.sqrt(NOTCH_R ** 2 - (NOTCH_END - a) ** 2)   # Bogen an der Außenkante
    n = 60
    ys = [-NOTCH_END + (NOTCH_END - NOTCH_STRAIT) * i / n for i in range(n + 1)] + \
         [NOTCH_STRAIT + (NOTCH_END - NOTCH_STRAIT) * i / n for i in range(n + 1)]
    pts = [(x_edge - 5, -NOTCH_END - 0.5), (x_edge - 0.001, -NOTCH_END - 0.5)]
    pts += [(xf(y), y) for y in ys]
    pts += [(x_edge - 0.001, NOTCH_END + 0.5), (x_edge - 5, NOTCH_END + 0.5)]
    return CS([pts])


def ext(cs, h, z0=0.0):
    return M.extrude(cs, h).translate((0, 0, z0))


def cyl(h, d, x, y, z0=0.0, seg=SEG):
    return M.cylinder(h, d / 2, circular_segments=seg).translate((x, y, z0))


outline = rrect(W, D, R_CORNER) - notch_poly()

# Außenkörper mit Fase (in 0,1-mm-Schichten, folgt auch der Aussparung)
steps = max(1, round(CHAMFER / 0.1))
body = ext(outline, H - CHAMFER, CHAMFER)
for i in range(steps):
    dz = CHAMFER / steps
    inset = CHAMFER - (i + 0.5) * dz
    body += ext(outline.offset(-inset, m3.JoinType.Round, circular_segments=SEG), dz + 0.001, i * dz)

cavity = ext(outline.offset(-WALL, m3.JoinType.Round, circular_segments=SEG), H, FLOOR)
shell = body - cavity

# Dome an der Wand: Zylinder volle Höhe, auf Außenkontur beschnitten
posts = M()
for x, y in HOLES:
    posts += cyl(H, POST_D, x, y)
shell += posts ^ body

# Stabilisierungsstege
def rib(px, py, nx, ny):
    """Steg an Innenwand-Punkt (px,py), Normale (nx,ny) zeigt ins Gehäuseinnere."""
    def slab(depth, z):
        bx = RIB_T if nx == 0 else depth + 0.5
        by = RIB_T if ny == 0 else depth + 0.5
        cx = px + nx * (depth - 0.5) / 2
        cy = py + ny * (depth - 0.5) / 2
        return M.cube((bx, by, 0.05), center=True).translate((cx, cy, z))
    return M.batch_hull([slab(RIB_DEPTH_BOT, FLOOR - 0.1), slab(RIB_DEPTH_TOP, H - RIB_GAP)])

x_left_inner = -W / 2 + NOTCH_DEPTH + WALL
for x in RIBS_LONG_X:
    shell += rib(x, D / 2 - WALL, 0, -1)
for y in RIBS_SHORT_Y:
    shell += rib(W / 2 - WALL, y, -1, 0)
    shell += rib(x_left_inner if abs(y) <= NOTCH_STRAIT else -W / 2 + WALL, y, 1, 0)

# Bohrungen + Senkungen von außen
for x, y in HOLES:
    shell -= cyl(H + 2, SCREW_D, x, y, -1)
    shell -= cyl(H - SCREW_GRIP + 1, HEAD_D, x, y, -1)

# Kabelverschraubungen unten (y = -D/2): Bohrungen quer durch die Wand
for x in PG_X:
    shell -= M.cylinder(WALL + 4, PG_D / 2, circular_segments=SEG).rotate((90, 0, 0)).translate((x, -D / 2 + WALL + 2, PG_Z))

# Schlüssellöcher (Aufhängung)
def stadium(w, L, x, y0):
    """Langloch der Breite w von (x,y0) um L nach +y, mit runden Enden."""
    return (CS.square((w, L), center=True).translate((x, y0 + L / 2))
            + CS.circle(w / 2, SEG).translate((x, y0))
            + CS.circle(w / 2, SEG).translate((x, y0 + L)))

KEY_PAD_H = KEY_LIP + KEY_POCKET + KEY_ROOF + KEY_CEIL   # lokale Bodendicke am Schlüsselloch (ragt KEY_PAD_H - FLOOR nach innen)
for kx in KEYHOLES_X:
    if KEY_PAD_H > FLOOR:                                                                     # Verstärkungspad innen
        shell += ext(stadium(KEY_HEAD_D + 2 * KEY_PAD_WALL, KEY_SLOT_LEN, kx, KEYHOLE_Y), KEY_PAD_H - 0.01, 0.005)
    shell -= cyl(KEY_LIP + KEY_POCKET + 1, KEY_HEAD_D, kx, KEYHOLE_Y, -1)                     # Einführloch, blind
    shell -= ext(stadium(KEY_SLOT_W, KEY_SLOT_LEN, kx, KEYHOLE_Y), KEY_LIP + 1, -1)           # Schaftschlitz durch die Lippe
    shell -= ext(stadium(KEY_HEAD_D, KEY_SLOT_LEN, kx, KEYHOLE_Y), KEY_POCKET, KEY_LIP)      # verdeckter Kopfkanal
    steps = round(KEY_ROOF / 0.1)                                                            # Dach 45°, in 0,1-mm-Lagen
    for i in range(steps):
        w = KEY_HEAD_D - 2 * (i + 1) * KEY_ROOF / steps
        shell -= ext(stadium(max(w, KEY_RIDGE), KEY_SLOT_LEN, kx, KEYHOLE_Y), KEY_ROOF / steps + 0.01,
                     KEY_LIP + KEY_POCKET + i * KEY_ROOF / steps - 0.005)

# Lüftungsschlitze
slot = CS.square((VENT_LEN - VENT_W, 0.001), center=True).offset(VENT_W / 2, m3.JoinType.Round, circular_segments=24)
for cx, cy in VENT_FIELDS:
    off = (VENT_SLOTS - 1) * VENT_PITCH / 2
    for i in range(VENT_SLOTS):
        shell -= ext(slot, FLOOR + 2, -1).translate((cx, cy - off + i * VENT_PITCH, 0))

if __name__ == "__main__":
    mesh = shell.to_mesh()
    tm = trimesh.Trimesh(vertices=mesh.vert_properties[:, :3], faces=mesh.tri_verts)
    print("status:", shell.status(), "genus:", shell.genus(),
          "bounds:", tm.bounds.round(2).tolist(), "vol cm3:", round(tm.volume / 1000, 1))
    tm.export("Rueckgehaeuse_ESP32-P4_10.1.stl")
    tm.export("Rueckgehaeuse_ESP32-P4_10.1.3mf")

    # Passprobe: 1,2 mm Rahmen der Auflagekontur mit den 8 Bohrungen (schneller Testdruck)
    gauge = ext(outline - outline.offset(-8.0, m3.JoinType.Round, circular_segments=SEG), 1.2)
    for x, y in HOLES:
        gauge -= cyl(4, SCREW_D, x, y, -1)
    gm = gauge.to_mesh()
    gt = trimesh.Trimesh(vertices=gm.vert_properties[:, :3], faces=gm.tri_verts)
    gt.export("Passprobe_Kontur_ESP32-P4_10.1.stl")
    gt.export("Passprobe_Kontur_ESP32-P4_10.1.3mf")
    print("gauge status:", gauge.status(), "bounds:", gt.bounds.round(2).tolist())
