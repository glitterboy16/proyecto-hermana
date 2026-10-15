# Decisiones y preguntas abiertas

## Decisiones tomadas

| Fecha | Decisión |
|---|---|
| 2026-10-10 | El sitio combina web profesional y plataforma de venta de cursos. |
| 2026-10-10 | Las clases en vivo quedan para el futuro, fuera de la fase 1. |
| 2026-10-10 | La documentación del proyecto vive en `README.md` y `docs/`. |
| 2026-10-15 | Prototipo de la home (v0.1) como web **estática**: HTML, CSS y JS sin dependencias ni build, en `web/`. No condiciona el stack definitivo, que sigue abierto. |
| 2026-10-15 | El prototipo sigue la recomendación de estilo (base A, aire de B y negro de C en la academia y la llamada final) mientras no haya elección final. |
| 2026-10-15 | Publicación en **GitHub Pages** mediante GitHub Actions (`.github/workflows/pages.yml`) a partir de `web/`, más el moodboard en `propuestas/moodboard.html`. Se despliega con cada push a `main`. |
| 2026-10-15 | La web es **pública** por decisión de Angel (el repositorio también pasa a público), pero todas las páginas llevan `noindex` para que no salgan en buscadores. |
| 2026-10-15 | Las imágenes de `web/img/` son **provisionales**: recortes de las capturas de Instagram y de los bocetos de Kay. Se sustituirán por las fotos originales y el logo en alta. |
| 2026-10-15 | La reserva no tiene backend: el formulario compone el mensaje y abre WhatsApp. Mientras falte el número de Kay, se copia el mensaje al portapapeles y se abre su enlace `wa.me/message/…`. Los testimonios del prototipo son de ejemplo. |

## Preguntas abiertas

- [x] Sector: pestañas, cejas y estética + academia de formación (ver `marca.md`)
- [x] Menú base según boceto: Inicio, Servicios, Formaciones, Sobre mí, Contacto + Reservar (ajustable)
- [ ] ¿Qué formato final tendrán los cursos? (grabados + PDFs, por módulos, con progreso…)
- [ ] ¿Cómo se cobrará? (pago único, suscripción, pasarela: Stripe, PayPal…)
- [ ] ¿Facturación? (España, EUR)
- [ ] ¿Dónde se alojarán los vídeos? (protección contra descargas)
- [ ] ¿Qué funciones tipo CRM necesita? (gestión de alumnos, leads, emails…)
- [ ] ¿Qué idiomas tendrá el sitio?
- [x] Marca: Key Angel Beauty, con logo y paleta definidos (ver `marca.md`)
- [ ] Stack técnico (por decidir cuando estén claros los requisitos; el prototipo estático no lo condiciona)
- [ ] Dirección visual final (ver `estilo.md`; el prototipo usa la recomendación A+B+C)

## Recursos pendientes de recibir

- [x] Nombre de la marca
- [x] Instagram de mi hermana (el acceso automatizado está bloqueado; usar capturas o descargas que aporte el usuario)
- [x] Bocetos e imágenes de referencia hechos por ella
- [ ] Fotos originales y logo en alta resolución, para sustituir las imágenes provisionales del prototipo
- [ ] Número de WhatsApp de Kay en formato `34XXXXXXXXX` (va en `WA_PHONE`, en `web/js/main.js`)
- [ ] Enlaces de TikTok y YouTube (aparecen en el footer de los bocetos)
- [ ] Testimonios reales, con permiso de cada clienta o alumna

## Proceso acordado

1. Recibir los recursos de arriba.
2. Buscar webs y plataformas reales similares, muy bien hechas, como referencia.
3. Elegir la dirección de diseño (registrar en `docs/estilo.md`).
4. Después, contenido y desarrollo.

Estado a 2026-10-15: pasos 1 y 2 hechos (faltan las fotos originales), paso 3 pendiente y paso 4 en curso con el prototipo v0.1 de la home. Resumen visual en `web/avance.html`.

## Material de Instagram

- 2026-10-10: Instagram no es accesible desde el entorno cloud y no se usan credenciales ni scraping.
- Se pide a Kay la **exportación oficial** (solo Publicaciones, Reels e Historias, sin Mensajes; formato HTML; calidad Alta). Se envía por WhatsApp como **documento**, o por Drive o WeTransfer si pesa más de 2 GB.
- También se piden **originales de la galería** (retratos, trabajos, formaciones, logo en alta).
- Guía para Kay (1 página): `docs/guias/guia-instagram-kay.pdf`. Se genera con `docs/guias/generar_guia_instagram.py`.
- [ ] Recibir el ZIP y los originales, y organizarlos en `assets/`.
