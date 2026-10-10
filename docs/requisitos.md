# Requisitos del proyecto

_Última actualización: 2026-10-10_

## Visión general

El proyecto tiene dos funciones en un mismo sitio:

- **Web profesional de mi hermana:** su imagen de marca y la de su negocio.
- **Plataforma donde vende sus cursos.**

Al principio se planteó como un "CRM muy complejo". De momento su núcleo es **web profesional + venta de cursos (LMS)**. Las funciones de gestión (alumnos, ventas, etc.) se irán detallando.

## 1. Web profesional

- Imágenes de ella y de su trabajo (portafolio/galería).
- **Navbar** fija y **menú con múltiples opciones**. Las secciones exactas están por definir.
- Menú según el boceto: **Inicio · Servicios · Formaciones · Sobre mí · Contacto** y el botón **Reservar**.
- Detalle de la marca, los servicios y las formaciones en [`marca.md`](marca.md).
- **Reserva de citas** para los servicios del estudio. Hoy se confirman por WhatsApp; el horario es de lunes a sábado, de 9:00 a 13:00.

## 2. Plataforma de cursos

El formato de los cursos **aún no está decidido**. Opciones planteadas:

| Formato | Descripción | Fase |
|---|---|---|
| Cursos grabados ("webinars") | Vídeos pregrabados subidos a la plataforma | Candidato para la fase 1 |
| Material complementario | Guías, PDFs y otros recursos descargables junto a los vídeos | Candidato para la fase 1 |
| Clases en vivo | Videollamadas en directo | **Futuro, no por ahora** |

Las formaciones actuales son presenciales (Lash Inicial, Lash Pro, Brow Art y Lash 360). La plataforma debe permitir, como mínimo, ver el catálogo, consultar los próximos cursos presenciales, **reservar plaza** y apuntarse a la **lista de espera**. Además se venderán cursos online.

Funciones implícitas a confirmar: venta y pago de cursos, cuentas de alumnos, acceso al contenido comprado y, posiblemente, seguimiento del progreso.

## Fases (borrador)

- **Fase 1:** web profesional + catálogo y venta de cursos grabados con material descargable.
- **Futuro:** clases en vivo por videollamada y funciones tipo CRM más avanzadas.
