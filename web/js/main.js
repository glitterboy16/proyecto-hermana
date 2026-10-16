'use strict';

const WA_LINK = 'https://wa.me/message/QUV53TXGIW26P1';
// Pendiente: número de Kay en formato 34XXXXXXXXX para abrir el chat con el mensaje ya escrito.
const WA_PHONE = '';

const $ = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];

/* Navegación */
const nav = $('.nav');
const menu = $('#menu');
const burger = $('.burger');

if (nav) {
  const onScroll = () => nav.classList.toggle('is-scrolled', window.scrollY > 10);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
}

if (menu && burger) {
  const setMenu = (open) => {
    menu.classList.toggle('is-open', open);
    burger.setAttribute('aria-expanded', String(open));
    burger.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
  };
  const isOpen = () => burger.getAttribute('aria-expanded') === 'true';

  burger.addEventListener('click', () => setMenu(!isOpen()));
  menu.addEventListener('click', (e) => { if (e.target.closest('a')) setMenu(false); });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && isOpen()) {
      setMenu(false);
      burger.focus();
    }
  });
  document.addEventListener('click', (e) => {
    if (isOpen() && !e.target.closest('.nav')) setMenu(false);
  });
}

/* Enlace activo del menú */
const spyLinks = menu ? $$('a[href^="#"]:not(.menu__cta)', menu) : [];
const spyTargets = spyLinks
  .map((link) => {
    const id = link.getAttribute('href').slice(1);
    const section = id === 'top' ? $('.hero') : document.getElementById(id);
    return section ? { link, section } : null;
  })
  .filter(Boolean);

if (spyTargets.length && 'IntersectionObserver' in window) {
  const setCurrent = (current) => {
    spyLinks.forEach((link) => {
      if (link === current) link.setAttribute('aria-current', 'true');
      else link.removeAttribute('aria-current');
    });
  };
  const spy = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      const match = spyTargets.find((t) => t.section === entry.target);
      if (match) setCurrent(match.link);
    });
  }, { rootMargin: '-40% 0px -55% 0px' });
  spyTargets.forEach((t) => spy.observe(t.section));
}

/* Aparición al hacer scroll */
const reveals = $$('.reveal');
const STAGGER_MS = 110;

const showReveal = (el, delay = 0) => {
  if (delay) {
    el.style.transitionDelay = `${delay}ms`;
    el.addEventListener('transitionend', () => { el.style.transitionDelay = ''; }, { once: true });
  }
  el.classList.add('is-in');
};

if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  reveals.forEach((el) => el.classList.add('is-in'));
} else if (reveals.length) {
  let observerAlive = false;
  const revealer = new IntersectionObserver((entries) => {
    observerAlive = true;
    const groups = new Map();
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      revealer.unobserve(entry.target);
      const parent = entry.target.parentElement;
      if (!groups.has(parent)) groups.set(parent, []);
      groups.get(parent).push(entry.target);
    });
    groups.forEach((items) => items.forEach((el, i) => showReveal(el, i * STAGGER_MS)));
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
  reveals.forEach((el) => revealer.observe(el));

  // Salvaguarda: si el observer nunca responde (entornos sin renderizado), el contenido no puede quedarse oculto.
  setTimeout(() => {
    if (observerAlive) return;
    revealer.disconnect();
    reveals.forEach((el) => el.classList.add('is-in'));
  }, 2000);

  // En pantallas muy altas el margen inferior del observer puede tapar lo último de la página:
  // al llegar al final se muestra lo que quede pendiente.
  const revealRest = () => {
    if (window.scrollY + window.innerHeight < document.documentElement.scrollHeight - 4) return;
    revealer.disconnect();
    reveals.forEach((el) => el.classList.add('is-in'));
    window.removeEventListener('scroll', revealRest);
  };
  window.addEventListener('scroll', revealRest, { passive: true });
  revealRest();
}

/* WhatsApp */
const toast = $('.toast');
let toastTimer;

function showToast(content, ms = 5000) {
  if (!toast) return;
  toast.replaceChildren(...[].concat(content));
  toast.hidden = false;
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => { toast.hidden = true; }, ms);
}

function copyFallback(text) {
  const area = document.createElement('textarea');
  area.value = text;
  area.setAttribute('readonly', '');
  area.style.cssText = 'position:fixed;top:0;left:0;opacity:0';
  document.body.append(area);
  area.select();
  let ok = false;
  try { ok = document.execCommand('copy'); } catch { ok = false; }
  area.remove();
  return ok;
}

function openUrl(url) {
  const win = window.open(url, '_blank');
  if (win) win.opener = null;
  else window.location.href = url;
}

function openWhatsApp(text) {
  if (WA_PHONE) {
    openUrl(`https://wa.me/${WA_PHONE}?text=${encodeURIComponent(text)}`);
    return;
  }

  // La copia se lanza antes de abrir la pestaña para no perder la activación del usuario.
  let copied;
  try {
    copied = navigator.clipboard && window.isSecureContext
      ? navigator.clipboard.writeText(text).then(() => true, () => false)
      : Promise.resolve(copyFallback(text));
  } catch {
    copied = Promise.resolve(copyFallback(text));
  }

  openUrl(WA_LINK);

  copied.then((ok) => {
    if (ok) {
      showToast('Mensaje copiado: pégalo en el chat de WhatsApp');
      return;
    }
    const msg = document.createElement('q');
    msg.textContent = text;
    msg.style.cssText = 'display:block;margin-top:8px;user-select:all';
    showToast(['No se pudo copiar el mensaje. Cópialo y pégalo en el chat de WhatsApp:', msg], 12000);
  });
}

$$('[data-wa]').forEach((el) => {
  el.addEventListener('click', (e) => {
    e.preventDefault();
    openWhatsApp(el.dataset.wa);
  });
});

/* Formulario de reserva */
const form = $('#reserva');

$$('[data-service]').forEach((link) => {
  link.addEventListener('click', () => {
    if (!form) return;
    const radio = $$('input[name="servicio"]', form).find((r) => r.value === link.dataset.service);
    if (radio) {
      radio.checked = true;
      radio.dispatchEvent(new Event('change', { bubbles: true }));
    }
  });
});

if (form) {
  const pad = (n) => String(n).padStart(2, '0');
  const toISODate = (d) => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
  const parseDate = (value) => {
    const [y, m, d] = value.split('-').map(Number);
    return new Date(y, m - 1, d);
  };
  const longDate = new Intl.DateTimeFormat('es-ES', { weekday: 'long', day: 'numeric', month: 'long' });

  const radios = $$('input[name="servicio"]', form);
  const fecha = form.elements.fecha;
  const hora = form.elements.hora;
  const nombre = form.elements.nombre;
  const msg = $('.form__msg', form);
  let attempted = false;

  const today = () => toISODate(new Date());
  fecha.min = today();

  // L–S de 9:00 a 13:00: última cita a las 12:30.
  for (let mins = 9 * 60; mins <= 12 * 60 + 30; mins += 30) {
    const label = `${pad(Math.floor(mins / 60))}:${pad(mins % 60)}`;
    hora.add(new Option(label, label));
  }

  const syncHours = () => {
    const now = new Date();
    const isToday = fecha.value === today();
    [...hora.options].forEach((opt) => {
      if (!opt.value) return;
      const [h, m] = opt.value.split(':').map(Number);
      opt.disabled = isToday && h * 60 + m <= now.getHours() * 60 + now.getMinutes();
    });
    if (hora.selectedOptions[0]?.disabled) hora.value = '';
  };

  const validate = () => {
    if (!radios.some((r) => r.checked)) return { field: radios[0], text: 'Elige el servicio que quieres reservar.' };
    if (!fecha.value) return { field: fecha, text: 'Elige el día de tu cita.' };
    if (fecha.value < today()) return { field: fecha, text: 'Esa fecha ya ha pasado. Elige un día a partir de hoy.' };
    if (parseDate(fecha.value).getDay() === 0) return { field: fecha, text: 'Los domingos el estudio está cerrado. Elige de lunes a sábado.' };
    if (!hora.value) return { field: hora, text: 'Elige la hora de tu cita.' };
    if (!nombre.value.trim()) return { field: nombre, text: 'Escribe tu nombre para que Kay sepa quién reserva.' };
    return null;
  };

  const setMessage = (text, isError) => {
    msg.textContent = text;
    msg.classList.toggle('is-error', Boolean(isError));
  };

  const markInvalid = (error) => {
    [fecha, hora, nombre].forEach((f) => f.removeAttribute('aria-invalid'));
    if (error && error.field !== radios[0]) error.field.setAttribute('aria-invalid', 'true');
  };

  form.addEventListener('change', (e) => {
    if (e.target === fecha) syncHours();
    const error = validate();
    const sunday = e.target === fecha && fecha.value && parseDate(fecha.value).getDay() === 0;
    if (attempted || sunday) {
      markInvalid(error);
      setMessage(error ? error.text : '', Boolean(error));
    }
  });

  nombre.addEventListener('input', () => {
    if (attempted && msg.classList.contains('is-error') && nombre.value.trim()) {
      const error = validate();
      markInvalid(error);
      setMessage(error ? error.text : '', Boolean(error));
    }
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    attempted = true;
    syncHours();
    const error = validate();
    markInvalid(error);

    if (error) {
      setMessage(error.text, true);
      error.field.focus();
      return;
    }

    const servicio = radios.find((r) => r.checked).value;
    const texto = `Hola Kay, soy ${nombre.value.trim()}. Me gustaría reservar ${servicio} el ${longDate.format(parseDate(fecha.value))} a las ${hora.value}. ¿Está disponible?`;
    setMessage('Abriendo WhatsApp con tu solicitud…', false);
    openWhatsApp(texto);
  });
}
