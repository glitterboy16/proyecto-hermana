from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit
from reportlab.lib.colors import HexColor
import sys

F = "/usr/share/fonts/truetype/"
pdfmetrics.registerFont(TTFont("Sans", F + "dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("SansB", F + "dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Serif", F + "liberation/LiberationSerif-Regular.ttf"))
pdfmetrics.registerFont(TTFont("SerifI", F + "liberation/LiberationSerif-Italic.ttf"))

IVORY = HexColor("#F8F2E8"); GOLD = HexColor("#A8803F"); GOLD_L = HexColor("#E9D9BC")
INK = HexColor("#1D1813"); MUTED = HexColor("#6E6255"); WHITE = HexColor("#FFFFFF")
RED = HexColor("#B3412F"); RED_L = HexColor("#F6E1DC"); GREEN = HexColor("#3F7A4A"); GREEN_L = HexColor("#E2EFE3")

W, H = 432, 768  # proporción de móvil (9:16)
M = 34
out, logo = sys.argv[1], sys.argv[2]
c = canvas.Canvas(out, pagesize=(W, H))
c.setTitle("Cómo sacar tus fotos y vídeos de Instagram")
c.setAuthor("Key Angel Beauty")
TOTAL = 12
page_no = [0]

def bg():
    c.setFillColor(IVORY); c.rect(0, 0, W, H, stroke=0, fill=1)

def footer():
    page_no[0] += 1
    c.setFont("Sans", 8); c.setFillColor(MUTED)
    c.drawString(M, 22, "Key Angel Beauty · Guía Instagram")
    c.drawRightString(W - M, 22, f"{page_no[0]} / {TOTAL}")

def text(s, y, font="Sans", size=13, color=INK, lead=1.4, x=M, width=None):
    width = width or (W - 2 * M - (x - M))
    c.setFont(font, size); c.setFillColor(color)
    for line in simpleSplit(s, font, size, width):
        c.drawString(x, y, line); y -= size * lead
    return y

def rich(parts, y, size=13, x=M, width=None):
    """Párrafo con trozos en negrita: parts = [(texto, bold), ...]"""
    width = width or (W - 2 * M - (x - M))
    words = []
    for t, b in parts:
        for w in t.split(" "):
            if w: words.append((w, b))
    line, lw = [], 0
    sp = pdfmetrics.stringWidth(" ", "Sans", size)
    def flush(line, y):
        cx = x
        for w, b in line:
            f = "SansB" if b else "Sans"
            c.setFont(f, size); c.setFillColor(INK); c.drawString(cx, y, w)
            cx += pdfmetrics.stringWidth(w, f, size) + sp
    for w, b in words:
        ww = pdfmetrics.stringWidth(w, "SansB" if b else "Sans", size)
        if line and lw + ww > width:
            flush(line, y); y -= size * 1.45; line, lw = [], 0
        line.append((w, b)); lw += ww + sp
    if line: flush(line, y); y -= size * 1.45
    return y

def step_head(n, title, y=H - 70):
    c.setFillColor(GOLD); c.circle(M + 20, y, 20, stroke=0, fill=1)
    c.setFillColor(WHITE); c.setFont("SansB", 17); c.drawCentredString(M + 20, y - 6, str(n))
    c.setFont("Sans", 9); c.setFillColor(GOLD); c.drawString(M + 52, y + 7, "PASO " + str(n))
    yy = y - 12
    for line in simpleSplit(title, "Serif", 24, W - 2 * M - 52):
        c.setFont("Serif", 24); c.setFillColor(INK); c.drawString(M + 52, yy, line); yy -= 27
    return min(yy, y - 30) - 18

def button(label, y, primary=False, note=None):
    """Dibuja el botón tal y como se ve en Instagram."""
    h = 44
    c.setFillColor(GOLD if primary else WHITE); c.setStrokeColor(GOLD); c.setLineWidth(1.2)
    c.roundRect(M, y - h, W - 2 * M, h, 10, stroke=1, fill=1)
    c.setFillColor(WHITE if primary else INK); c.setFont("SansB", 14)
    c.drawString(M + 16, y - h / 2 - 5, label)
    c.setFont("SansB", 16); c.drawRightString(W - M - 16, y - h / 2 - 6, "›")
    y -= h + 6
    if note:
        y = text(note, y - 6, size=10, color=MUTED, lead=1.35, x=M + 4)
    return y - 10

def tap(y):
    c.setFont("Sans", 10); c.setFillColor(GOLD)
    c.drawString(M, y, "TOCA AQUÍ:")
    return y - 12

def box(kind, title, body, y):
    col, bgc = {"ok": (GREEN, GREEN_L), "no": (RED, RED_L), "tip": (GOLD, HexColor("#F3E8D4"))}[kind]
    lines = []
    for p in body:
        lines += simpleSplit(p, "Sans", 11.5, W - 2 * M - 28) + [""]
    lines = lines[:-1]
    h = 34 + len(lines) * 16
    c.setFillColor(bgc); c.roundRect(M, y - h, W - 2 * M, h, 10, stroke=0, fill=1)
    c.setFillColor(col); c.rect(M, y - h, 4, h, stroke=0, fill=1)
    c.setFont("SansB", 12); c.drawString(M + 16, y - 22, title)
    yy = y - 40
    c.setFillColor(INK); c.setFont("Sans", 11.5)
    for l in lines:
        c.drawString(M + 16, yy, l); yy -= 16
    return y - h - 16

def menu_icon(x, y):
    c.setStrokeColor(INK); c.setLineWidth(2.2)
    for i in range(3): c.line(x, y - i * 7, x + 22, y - i * 7)

# ---------- 1. Portada ----------
bg()
c.drawImage(logo, (W - 210) / 2, H - 205, width=210, height=90, mask=None, preserveAspectRatio=True)
c.setFont("Serif", 12); c.setFillColor(GOLD)
c.drawCentredString(W / 2, H - 232, "K E Y   A N G E L   B E A U T Y")
y = H - 300
c.setFont("Sans", 10); c.setFillColor(GOLD); c.drawString(M, y, "GUÍA PARA KAY · 10 MINUTOS")
y -= 34
for line in ["Cómo sacar todas tus", "fotos y vídeos de", "Instagram"]:
    c.setFont("Serif", 32); c.setFillColor(INK); c.drawString(M, y, line); y -= 36
c.setFont("SerifI", 20); c.setFillColor(GOLD); c.drawString(M, y - 4, "en la máxima calidad"); y -= 44
y = text("Son unos pocos toques en el móvil. Al final tendrás un archivo (un .zip) con todas tus publicaciones, reels e historias, y se lo mandas a tu hermano por WhatsApp.", y, size=13)
y -= 10
y = box("tip", "Lo que vas a hacer", [
    "1. Pedir a Instagram una copia de tus fotos y vídeos.",
    "2. Esperar a que te avise (minutos u horas).",
    "3. Descargarla y mandarla por WhatsApp como documento."], y)
footer(); c.showPage()

# ---------- 2. Antes de empezar ----------
bg()
y = H - 70
c.setFont("Sans", 9); c.setFillColor(GOLD); c.drawString(M, y + 6, "ANTES DE EMPEZAR")
c.setFont("Serif", 26); c.setFillColor(INK); c.drawString(M, y - 24, "Ten esto a mano")
y -= 70
for t, d in [
    ("Tu móvil con Instagram", "Hazlo desde la app de Instagram, con la cuenta keyangel.beauty."),
    ("Wi-Fi y batería", "Conéctate a Wi-Fi: el archivo puede pesar varios GB."),
    ("Tu contraseña de Instagram", "Te la pedirá una vez para confirmar que eres tú."),
    ("Acceso a tu email", "Instagram te avisa por email cuando la copia está lista."),
]:
    c.setFillColor(GOLD); c.circle(M + 9, y - 4, 9, stroke=0, fill=1)
    c.setFillColor(WHITE); c.setFont("SansB", 11); c.drawCentredString(M + 9, y - 8, "✓")
    c.setFont("SansB", 14); c.setFillColor(INK); c.drawString(M + 30, y - 8, t)
    y = text(d, y - 28, size=12, color=MUTED, x=M + 30) - 14
y = box("tip", "Si algo no se ve igual", [
    "Instagram cambia a veces el nombre de los botones. Si no ves exactamente el texto de la guía, toca el que más se parezca. En esta guía pongo los dos nombres que suele usar."], y - 6)
footer(); c.showPage()

# ---------- 3. Paso 1: perfil y menú ----------
bg()
y = step_head(1, "Abre el menú de tu perfil")
y = rich([("Abre Instagram y toca ", False), ("tu foto de perfil", True), (" (abajo a la derecha).", False)], y, size=14) - 14
y = rich([("Arriba a la derecha toca las ", False), ("tres rayas", True), (":", False)], y, size=14) - 8
c.setFillColor(WHITE); c.setStrokeColor(GOLD); c.roundRect(M, y - 70, W - 2 * M, 70, 10, stroke=1, fill=1)
c.setFont("SansB", 14); c.setFillColor(INK); c.drawString(M + 16, y - 42, "keyangel.beauty")
menu_icon(W - M - 42, y - 28)
c.setStrokeColor(GOLD); c.setLineWidth(2); c.circle(W - M - 31, y - 35, 22, stroke=1, fill=0)
y -= 96
y = tap(y)
y = button("Centro de cuentas", y, primary=True, note="Suele salir arriba del todo, con el logo de Meta (∞).")
footer(); c.showPage()

# ---------- 4. Paso 2: tu información ----------
bg()
y = step_head(2, "Entra en tu información")
y = text("Dentro de Centro de cuentas, baja un poco y toca:", y, size=14) - 8
y = tap(y)
y = button("Tu información y permisos", y, primary=True)
y = text("Después toca:", y - 4, size=14) - 8
y = tap(y)
y = button("Exportar tu información", y, primary=True,
           note="En algunos móviles se llama «Descargar tu información». Es lo mismo.")
y = text("Y por último:", y - 4, size=14) - 8
y = tap(y)
y = button("Crear exportación", y, primary=True)
footer(); c.showPage()

# ---------- 5. Paso 3: cuenta y destino ----------
bg()
y = step_head(3, "Elige tu cuenta y dónde guardarla")
y = text("Te pregunta de qué cuenta quieres la copia. Marca:", y, size=14) - 8
y = tap(y)
y = button("keyangel.beauty  (Instagram)", y, primary=True, note="Si también sale Facebook, no lo marques.")
y = text("Luego te pregunta dónde guardarla. Elige:", y - 4, size=14) - 8
y = tap(y)
y = button("Exportar al dispositivo", y, primary=True,
           note="También puede llamarse «Descargar en el dispositivo». No elijas Google Drive ni Dropbox aquí.")
footer(); c.showPage()

# ---------- 6. Paso 4: qué información ----------
bg()
y = step_head(4, "Elige solo tus fotos y vídeos")
y = rich([("Toca ", False), ("«Personalizar información»", True), (" (o «Información que se va a exportar»). Sale una lista larga.", False)], y, size=13.5) - 10
y = box("ok", "MARCA solo esto", [
    "✓  Publicaciones",
    "✓  Reels  (puede venir dentro de «Contenido»)",
    "✓  Historias  (también las destacadas)"], y)
y = box("no", "QUITA todo lo demás", [
    "Sobre todo los «Mensajes»: son conversaciones privadas con tus clientas y no hacen falta para la web.",
    "Seguidores, comentarios, anuncios, etc.: tampoco."], y)
y = rich([("Si solo ves «Contenido», márcalo entero. Luego toca ", False), ("Guardar", True), (".", False)], y, size=12.5)
footer(); c.showPage()

# ---------- 7. Paso 5: CALIDAD ----------
bg()
y = step_head(5, "La calidad (lo más importante)")
y = text("Antes de terminar verás tres opciones. Déjalas EXACTAMENTE así:", y, size=13.5) - 12
for label, val, note in [
    ("Intervalo de fechas", "Desde el principio", "También puede salir como «Todo el tiempo». Si no, saca solo el último año."),
    ("Formato", "HTML", "Es el más fácil de abrir."),
    ("Calidad del contenido multimedia", "Alta", "Si pones Media o Baja, las fotos pierden calidad. Tiene que ser ALTA."),
]:
    c.setFillColor(WHITE); c.setStrokeColor(GOLD); c.setLineWidth(1.2)
    c.roundRect(M, y - 62, W - 2 * M, 62, 10, stroke=1, fill=1)
    c.setFont("Sans", 11); c.setFillColor(MUTED); c.drawString(M + 16, y - 22, label)
    c.setFont("SansB", 17); c.setFillColor(GOLD); c.drawString(M + 16, y - 46, val)
    c.setFont("SansB", 13); c.setFillColor(GREEN); c.drawRightString(W - M - 16, y - 40, "✓")
    y = text(note, y - 78, size=10.5, color=MUTED, x=M + 4) - 10
y = tap(y - 2)
y = button("Iniciar exportación", y, primary=True, note="Pon tu contraseña de Instagram si te la pide. ¡Ya está pedida!")
footer(); c.showPage()

# ---------- 8. Paso 6: esperar ----------
bg()
y = step_head(6, "Espera el aviso")
y = text("Instagram prepara la copia. Puede tardar desde unos minutos hasta uno o dos días si tienes muchos vídeos. No hace falta que dejes la app abierta.", y, size=13.5) - 10
y = text("Te avisará con una notificación y un email.", y, size=13.5) - 16
y = box("tip", "Mientras esperas", [
    "En «Exportar tu información» verás la copia como «Pendiente» o «En curso». Es normal."], y)
y = box("no", "Ojo con el plazo", [
    "Cuando esté lista, tienes unos 4 días para descargarla. Si se pasa el plazo, hay que pedirla otra vez."], y)
footer(); c.showPage()

# ---------- 9. Paso 7: descargar ----------
bg()
y = step_head(7, "Descarga la copia")
y = text("Cuando te avise, vuelve al mismo sitio:", y, size=14) - 6
y = text("Perfil  ›  tres rayas  ›  Centro de cuentas  ›  Tu información y permisos  ›  Exportar tu información", y, font="SansB", size=12, color=GOLD, lead=1.5) - 10
y = text("Al lado de tu copia toca:", y, size=14) - 8
y = tap(y)
y = button("Descargar", y, primary=True, note="Te pedirá la contraseña otra vez.")
y = box("tip", "En iPhone", [
    "Se guarda en la app «Archivos», carpeta «Descargas». Si te pregunta, elige «Descargar».",
    "Puede salir en varias partes (parte 1, parte 2…). Descárgalas TODAS."], y - 4)
y = box("no", "No lo abras ni lo descomprimas", [
    "Deja el .zip tal cual. Si lo abres o lo pasas por otra app, puede perder calidad."], y)
footer(); c.showPage()

# ---------- 10. Paso 8: WhatsApp ----------
bg()
y = step_head(8, "Mándalo por WhatsApp sin perder calidad")
y = box("no", "NUNCA como foto o vídeo normal", [
    "WhatsApp comprime las fotos y vídeos y pierden calidad."], y)
y = text("Haz esto en el chat con tu hermano:", y, size=13.5) - 8
for i, (a, b) in enumerate([
    ("Toca el ", "+"), ("Elige ", "Documento"), ("Toca ", "Elegir de Archivos"), ("Busca en Descargas el ", ".zip y envíalo")], 1):
    c.setFillColor(GOLD); c.circle(M + 11, y - 4, 11, stroke=0, fill=1)
    c.setFillColor(WHITE); c.setFont("SansB", 11); c.drawCentredString(M + 11, y - 8, str(i))
    rich([(a, False), (b, True)], y - 8, size=14, x=M + 32)
    y -= 34
y = box("tip", "Si pesa más de 2 GB", [
    "WhatsApp no deja enviar archivos tan grandes. Súbelo a Google Drive o a WeTransfer y manda el enlace por WhatsApp."], y - 4)
footer(); c.showPage()

# ---------- 11. Extra: originales ----------
bg()
y = H - 70
c.setFont("Sans", 9); c.setFillColor(GOLD); c.drawString(M, y + 6, "EXTRA · MUY RECOMENDADO")
for line in simpleSplit("Lo que tienes en la galería vale aún más", "Serif", 24, W - 2 * M):
    c.setFont("Serif", 24); c.setFillColor(INK); c.drawString(M, y - 24, line); y -= 28
y -= 40
y = text("Instagram comprime todo al subirlo. Las fotos y vídeos ORIGINALES de tu móvil tienen más calidad que cualquier cosa que salga de Instagram. Para la web, lo mejor de lo mejor:", y, size=13) - 10
y = box("ok", "Lo que más vamos a usar", [
    "✓  Retratos tuyos (los profesionales y los buenos del móvil)",
    "✓  Tus mejores trabajos: primeros planos, antes y después",
    "✓  Fotos y vídeos de tus formaciones y alumnas",
    "✓  El logo en alta calidad (PNG, PDF o el archivo del diseñador)"], y)
y = text("Cómo mandarlos sin perder calidad:", y - 8, font="SansB", size=12.5) - 6
y = text("Chat  ›  +  ›  Documento  ›  «Elegir foto o vídeo»  ›  selecciona varias  ›  Enviar", y, font="SansB", size=12, color=GOLD, lead=1.5) - 6
y = text("Así salen como documento, sin comprimir. Si son muchas, mejor juntarlas en un álbum de Google Drive o Google Fotos y mandar el enlace.", y, size=11.5, color=MUTED)
footer(); c.showPage()

# ---------- 12. Checklist ----------
bg()
y = H - 70
c.setFont("Sans", 9); c.setFillColor(GOLD); c.drawString(M, y + 6, "RESUMEN")
c.setFont("Serif", 26); c.setFillColor(INK); c.drawString(M, y - 24, "Comprueba antes de enviar")
y -= 74
for item in [
    "Pedí solo Publicaciones, Reels e Historias (sin Mensajes)",
    "Fechas: desde el principio",
    "Formato: HTML",
    "Calidad: ALTA",
    "Descargué todas las partes del .zip",
    "Lo mandé por WhatsApp como DOCUMENTO (o por Drive o WeTransfer si pesa más de 2 GB)",
    "Extra: mandé mis mejores fotos y vídeos originales como documento",
]:
    c.setStrokeColor(GOLD); c.setLineWidth(1.4); c.roundRect(M, y - 14, 18, 18, 4, stroke=1, fill=0)
    y = text(item, y - 10, size=13, x=M + 30) - 12
c.setFont("SerifI", 22); c.setFillColor(GOLD)
c.drawCentredString(W / 2, 90, "Beauty with Purpose")
c.setFont("Sans", 10); c.setFillColor(MUTED)
c.drawCentredString(W / 2, 70, "¡Gracias! Con esto montamos tu web.")
footer(); c.showPage()

c.save()
print("pages", page_no[0])
