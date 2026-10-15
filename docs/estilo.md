# Dirección visual

**Objetivo:** un estilo de lo más *top* posible, con una estética premium y profesional.

**Estado:** propuesta 1 presentada (2026-10-10). **Pendiente de elegir.** Mientras tanto, el prototipo v0.1 de la home (2026-10-15) aplica la recomendación (ver "Prototipo v0.1" más abajo).

- Moodboard publicado: https://claude.ai/artifact/3SUjaH9qskxoRoQ8hfgwpA
- Copia local: `docs/propuestas/01-moodboard.html`

## Direcciones propuestas

| | Dirección | Idea | Referencias reales |
|---|---|---|---|
| **A** | Atelier Dorado | El boceto de Kay refinado: marfil satinado, dorado, mayúsculas espaciadas y retrato en arco | Guerlain, La Mer, Sisley Paris |
| **B** | Editorial Silencioso | Lujo discreto: mucho blanco, tipografía grande y fina, fotos a sangre y dorado mínimo | Westman Atelier, Augustinus Bader, Aesop |
| **C** | Noir Doré | Negro y oro cinematográfico, con imágenes a pantalla completa; catálogo de cursos como estrenos | Tom Ford Beauty, Byredo, MasterClass |

## Academia online (válida con cualquier dirección)

- Página de curso con tráiler, módulos de vídeo, PDFs y láminas, compra lateral, progreso y certificado.
- Patrones de referencia:
  - Tráiler y lista de lecciones (MasterClass)
  - Módulos con recursos descargables (Domestika)
  - Certificación con examen y revisión de fotos de trabajos (Sugarlash PRO Academy)
  - Acceso de por vida (Lash Affair Academy)
  - Academia hispana sobre Teachable (Master Lashing Academy)
  - Reserva en 3 pasos (Fresha, Treatwell)
- Modelo sugerido: **online + práctica presencial**, que encaja con cómo forma Kay hoy.

## Recomendación de Claude

**A como base**, con el espacio en blanco y la tipografía de **B**, y el negro de **C** solo en la academia y la llamada final.

## Prototipo v0.1 (2026-10-15)

`web/index.html` aplica la recomendación, a falta de la elección final:

- **Base A (Atelier Dorado):** fondo marfil satinado, dorado, títulos serif en mayúsculas con tracking, lema en script y retrato en arco.
- **Aire de B (Editorial Silencioso):** mucho espacio en blanco, titulares grandes y finos y listas limpias (servicios numerados 01–05).
- **Negro de C (Noir Doré):** solo en el bloque Academy y en la llamada final "Comienza aquí".

### Tokens principales (`web/css/estilos.css`, `:root`)

| Token | Valor | Uso |
|---|---|---|
| `--ivory` | `#FBF7F0` | Fondo general |
| `--cream` | `#F3EADC` | Fondos secundarios y degradados |
| `--ink` / `--ink-2` | `#1C1712` / `#3A3128` | Texto principal y secundario |
| `--muted` | `#6B5F51` | Texto atenuado (5,8:1 sobre marfil) |
| `--gold` | `#B08A4F` | Líneas, iconos y detalles. **No** para texto pequeño (3:1) |
| `--gold-ink` | `#7A5A26` | Texto dorado sobre claro (5,9:1) |
| `--gold-hi` | `#D7B97E` | Dorado sobre negro (10:1) |
| `--bronze-1` → `--bronze-2` | `#94702F` → `#6B4E1F` | Degradado de los botones principales |
| `--noir` / `--noir-2` | `#12100D` / `#1B1814` | Academy y llamada final |
| `--on-noir` / `--on-noir-muted` | `#EFE6D8` / `#B9AD9C` | Texto sobre negro |

- **Tipografía:** Cormorant Garamond (títulos), Pinyon Script (lema y firma) y Jost (texto, etiquetas y botones), todas de Google Fonts.
- **Maquetación:** contenedor de 1200 px, márgenes laterales `clamp(20px, 5vw, 56px)` y nav fija de 84 px (72 px en móvil).

### Reglas

- Los botones usan **bronce oscuro** (`#94702F` → `#6B4E1F`) y no el dorado de la marca para cumplir el contraste **AA** con texto claro (`#FFF9EF`). Allí donde cae el texto, el contraste es de 4,7:1 o más (5,6:1 en el centro). El dorado `#B08A4F` solo daría 3:1, así que el degradado no debe aclararse.
- Sin texto con degradado: "Comienza aquí" usa un color sólido (`--gold-hi`).
- Apariciones suaves al hacer scroll, que se desactivan con `prefers-reduced-motion`.

## Elección final

_(Pendiente.)_

## Nota técnica

Desde el entorno cloud no se pueden abrir webs externas ni Instagram, por lo que no fue posible hacer capturas de las referencias.
