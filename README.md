# Proyecto Hermana

**Key Angel Beauty**: web profesional + plataforma de formaciones de Kay Villorina, Lash Master y educadora en Mérida (Badajoz).

> **Estado:** definición + prototipo v0.1 de la home (2026-10-15). La dirección visual aún no está elegida; el prototipo sigue la recomendación A+B+C (ver `docs/estilo.md`).

## Qué es

1. **Web profesional / empresarial:** presenta a mi hermana y su trabajo con fotos y portafolio. Tiene navbar y un menú con varias secciones.
2. **Plataforma de cursos:** donde ella vende sus cursos en línea (formato aún por definir, ver `docs/requisitos.md`).
3. **Objetivo de diseño:** estilo de lo más *top* posible, con una estética premium y cuidada.

## Ver el prototipo

- **En local:** abre `web/index.html` en el navegador. No hace falta servidor ni instalar nada.
- **En GitHub Pages:** https://glitterboy16.github.io/proyecto-hermana/
  - Estado del proyecto: https://glitterboy16.github.io/proyecto-hermana/avance.html
  - Moodboard A/B/C: https://glitterboy16.github.io/proyecto-hermana/propuestas/moodboard.html

Se publica solo con cada push a `main` (workflow `.github/workflows/pages.yml`). Las páginas llevan `noindex` para que no aparezcan en buscadores.

## Estructura de `web/`

| Ruta | Contenido |
|---|---|
| `web/index.html` | Home: hero, servicios, Academy, sobre mí, testimonios, reserva y llamada final |
| `web/avance.html` | Estado del proyecto: proceso, cronología, pendientes y próximos pasos |
| `web/css/estilos.css` | Todos los estilos (tokens en `:root`) |
| `web/js/main.js` | Nav, menú móvil, enlace activo, apariciones al hacer scroll, WhatsApp y formulario de reserva |
| `web/img/` | Imágenes **provisionales** recortadas de capturas de Instagram y de los bocetos, más `logo.png` y `favicon.png` |

HTML, CSS y JS sin dependencias ni build. El número de WhatsApp de Kay va en `WA_PHONE`, al principio de `web/js/main.js`.

## Documentación

| Documento | Contenido |
|---|---|
| [`docs/marca.md`](docs/marca.md) | Marca Key Angel Beauty: identidad, servicios, formaciones y paleta |
| [`docs/requisitos.md`](docs/requisitos.md) | Visión, módulos, funcionalidades y alcance por fases |
| [`docs/decisiones.md`](docs/decisiones.md) | Decisiones tomadas y preguntas abiertas |
| [`docs/estilo.md`](docs/estilo.md) | Dirección visual, inspiraciones y tokens del prototipo |

Mantén estos documentos al día: son la fuente de verdad del proyecto.
