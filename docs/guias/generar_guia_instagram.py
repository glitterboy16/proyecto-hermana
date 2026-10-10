"""Genera docs/guias/guia-instagram-kay.pdf: guía de una página para exportar Instagram."""
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
import sys

F = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("R", F + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("B", F + "DejaVuSans-Bold.ttf"))

BLACK = HexColor("#111111"); GREY = HexColor("#555555"); BLUE = HexColor("#0B5CD5"); RED = HexColor("#C0392B")
W, H = A4
M = 50
out = sys.argv[1] if len(sys.argv) > 1 else "guia-instagram-kay.pdf"
c = canvas.Canvas(out, pagesize=A4)
c.setTitle("Cómo sacar tus fotos y vídeos de Instagram")


def line(parts, y, size=12.5, x=M + 34, width=W - 2 * M - 34):
    """Escribe un párrafo; parts = [(texto, negrita)]. Devuelve la nueva y."""
    words = []  # (palabra, negrita, pegada a la anterior)
    prev_space = True
    for t, b in parts:
        for i, w in enumerate(t.split(" ")):
            if w:
                words.append((w, b, i == 0 and not prev_space and not t.startswith(" ")))
        prev_space = t.endswith(" ")
    sp = pdfmetrics.stringWidth(" ", "R", size)
    row, rw = [], 0
    def flush(row, y):
        cx = x
        for k, (w, b, glued) in enumerate(row):
            f = "B" if b else "R"
            if glued and k:
                cx -= sp
            c.setFont(f, size); c.setFillColor(BLACK); c.drawString(cx, y, w)
            cx += pdfmetrics.stringWidth(w, f, size) + sp
    for w, b, glued in words:
        ww = pdfmetrics.stringWidth(w, "B" if b else "R", size)
        if row and rw + ww > width:
            flush(row, y); y -= size * 1.4; row, rw = [], 0
        row.append((w, b, glued)); rw += ww + sp
    if row:
        flush(row, y); y -= size * 1.4
    return y


y = H - 70
c.setFont("B", 19); c.setFillColor(BLACK)
c.drawString(M, y, "Cómo sacar tus fotos y vídeos de Instagram")
y -= 24
c.setFont("R", 12); c.setFillColor(GREY)
c.drawString(M, y, "Desde el móvil, con wifi. Tardas 5 minutos.")
y -= 40

steps = [
    [("Abre Instagram, toca tu ", False), ("foto de perfil", True), (" (abajo a la derecha) y luego las ", False), ("tres rayas", True), (" (arriba a la derecha).", False)],
    [("Toca ", False), ("Centro de cuentas", True), (", luego ", False), ("Tu información y permisos", True), (", luego ", False), ("Exportar tu información", True), (" (o «Descargar tu información»).", False)],
    [("Toca ", False), ("Crear exportación", True), (", elige tu cuenta ", False), ("keyangel.beauty", True), (" y luego ", False), ("Exportar al dispositivo", True), (".", False)],
    [("Toca ", False), ("Personalizar información", True), (". Marca solo ", False), ("Publicaciones, Reels e Historias", True), (" y quita todo lo demás (sobre todo los Mensajes).", False)],
    [("Pon: Fechas ", False), ("Desde el principio", True), (", Formato ", False), ("HTML", True), (" y Calidad ", False), ("ALTA", True), (". Toca ", False), ("Iniciar exportación", True), (" y pon tu contraseña.", False)],
    [("Espera. Instagram te avisa por notificación o email (de minutos a 1 día). Entonces vuelve a ", False), ("Exportar tu información", True), (" y toca ", False), ("Descargar", True), (". Si salen varias partes, descárgalas todas.", False)],
    [("Mándalo por WhatsApp como ", False), ("Documento", True), (": en el chat toca ", False), ("+", True), (", luego ", False), ("Documento", True), (" y elige el archivo .zip (en iPhone está en Archivos, carpeta Descargas).", False)],
]
for i, parts in enumerate(steps, 1):
    c.setFillColor(BLUE); c.circle(M + 12, y + 4, 12, stroke=0, fill=1)
    c.setFillColor(HexColor("#FFFFFF")); c.setFont("B", 12); c.drawCentredString(M + 12, y, str(i))
    y = line(parts, y) - 14

y -= 6
c.setStrokeColor(RED); c.setLineWidth(1.5)
box_top = y + 14
c.setFont("B", 13); c.setFillColor(RED); c.drawString(M + 14, y - 6, "Importante")
y -= 28
for parts in [
    [("La calidad tiene que estar en ", False), ("ALTA", True), (".", False)],
    [("En WhatsApp, siempre como ", False), ("Documento", True), (". Nunca como foto o vídeo normal, porque pierde calidad.", False)],
    [("Si pesa más de 2 GB, WhatsApp no deja: súbelo a ", False), ("Google Drive", True), (" o ", False), ("WeTransfer", True), (" y manda el enlace.", False)],
    [("Si tienes las fotos y vídeos ", False), ("originales", True), (" en la galería (retratos, trabajos, formaciones), mándalos también como Documento. Tienen más calidad que Instagram.", False)],
]:
    c.setFont("B", 12); c.setFillColor(BLACK); c.drawString(M + 14, y, "•")
    y = line(parts, y, size=11.5, x=M + 30, width=W - 2 * M - 44) - 6
c.roundRect(M, y, W - 2 * M, box_top - y, 8, stroke=1, fill=0)

c.setFont("R", 9.5); c.setFillColor(GREY)
c.drawString(M, y - 26, "Si un botón no se llama exactamente así, toca el que más se parezca. Instagram a veces cambia los nombres.")
c.showPage(); c.save()
