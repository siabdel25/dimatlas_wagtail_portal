/* DimaAtlas portal — îlots d'animation (Vue 3 pour les compteurs + vanilla léger).
   Respecte prefers-reduced-motion. */
(function () {
  'use strict';
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── Menu mobile ──────────────────────────────────────────────────────── */
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', () => links.classList.toggle('open'));
  }

  /* ── Reveal au scroll ─────────────────────────────────────────────────── */
  const reveals = document.querySelectorAll('.reveal');
  if (reduce || !('IntersectionObserver' in window)) {
    reveals.forEach((el) => el.classList.add('in'));
  } else {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.15 });
    reveals.forEach((el) => io.observe(el));
  }

  /* ── Courbes de niveau : génère des chemins « topographiques » ─────────── */
  const svg = document.querySelector('.contour-svg');
  if (svg) {
    const W = 1200, H = 700, lines = 9;
    const ns = 'http://www.w3.org/2000/svg';
    svg.setAttribute('viewBox', `0 0 ${W} ${H}`);
    svg.setAttribute('preserveAspectRatio', 'xMidYMid slice');
    for (let i = 0; i < lines; i++) {
      const baseY = 120 + i * 60;
      const amp = 70 + i * 8;
      let d = `M -50 ${baseY}`;
      for (let x = 0; x <= W + 50; x += 60) {
        const y = baseY - Math.sin((x / W) * Math.PI * 2.2 + i * 0.5) * amp
                        - Math.cos((x / W) * Math.PI * 4 + i) * (amp / 3);
        d += ` L ${x} ${y.toFixed(1)}`;
      }
      const p = document.createElementNS(ns, 'path');
      p.setAttribute('d', d);
      if (!reduce) { p.classList.add('draw'); p.style.animationDelay = (i * 0.12) + 's'; }
      svg.appendChild(p);
    }
  }

  /* ── Compteurs animés (Vue 3 si présent, sinon fallback direct) ────────── */
  function animateValue(el) {
    const raw = el.dataset.value || el.textContent;
    const num = parseFloat(String(raw).replace(/[^\d.]/g, ''));
    if (reduce || isNaN(num)) { return; }
    const suffix = String(raw).replace(/[\d.\s]/g, '');
    const dur = 1400, t0 = performance.now();
    function step(now) {
      const k = Math.min(1, (now - t0) / dur);
      const eased = 1 - Math.pow(1 - k, 3);
      el.textContent = Math.round(num * eased) + suffix;
      if (k < 1) { requestAnimationFrame(step); }
    }
    requestAnimationFrame(step);
  }
  const counters = document.querySelectorAll('[data-counter]');
  if (counters.length) {
    const io2 = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) { animateValue(e.target); io2.unobserve(e.target); }
      });
    }, { threshold: 0.6 });
    counters.forEach((el) => io2.observe(el));
  }
})();
