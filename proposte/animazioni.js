/* ===== Animazioni Messina (proposta 25/10/2026): va messo dentro lo script del mockup, prima del primo render() ===== */
(function animazioni(){
  const calma = matchMedia('(prefers-reduced-motion: reduce)');
  const fermo = () => calma.matches;

  // Le sezioni e le schermate: l'animazione parte solo quando si cambia posto, non a ogni tocco
  const chiave = () => {
    const h = document.querySelector('#app .chead h2');
    return [S.view, S.t && S.t.sec, S.c && S.c.sec, S.p && S.p.sec, S.a && S.a.scr, S.a && S.a.cur,
            S.k && S.k.scr, S.m && S.m.scr, h ? h.textContent : ''].join('|');
  };
  // a fine animazione l'elemento torna identico a prima (niente classi o stili lasciati)
  const pulisci = (el, cls) => { el.classList.remove(cls); el.style.removeProperty('--m-i');
    if (!el.getAttribute('style')) el.removeAttribute('style'); if (!el.getAttribute('class')) el.removeAttribute('class'); };
  const inFila = (box, cls, max) => {
    if (!box) return;
    [...box.children].slice(0, max).forEach((el, i) => {
      el.style.setProperty('--m-i', i);
      el.classList.add(cls);
      el.addEventListener('animationend', () => pulisci(el, cls), { once: true });
    });
  };
  const entra = (cambioVista) => {
    if (fermo()) return;
    const app = document.getElementById('app');
    const dentro = app.querySelector('.content') || app.querySelector('.pscr');
    if (cambioVista || !dentro) {
      if (app.querySelector('.side')) inFila(app.querySelector('.side'), 'm-entra', 20);
      inFila(dentro || app, 'm-entra', 10);
      if (!dentro) return;
    } else inFila(dentro, 'm-entra', 10);
  };

  // 4 · Numeri: salgono fino al valore quando si apre la sezione, e quando cambiano (es. Incassato dopo «Pagata»)
  const NUM = /(\d{1,3}(?:\.\d{3})+|\d+)(,\d+)?/;
  const leggi = (t) => { const m = t.match(NUM); if (!m) return null;
    return { m, v: parseFloat(m[1].replace(/\./g, '') + (m[2] ? '.' + m[2].slice(1) : '')), dec: m[2] ? m[2].length - 1 : 0, punti: m[1].includes('.') }; };
  const scrivi = (v, dec, punti) => {
    const [i, d] = v.toFixed(dec).split('.');
    const ii = punti || i.length > 4 ? i.replace(/\B(?=(\d{3})+(?!\d))/g, '.') : i;
    return d ? ii + ',' + d : ii;
  };
  let prima = {};
  const numeri = (nuovaSezione) => {
    const ora = {};
    document.querySelectorAll('#app .big').forEach((el, k) => {
      const nodo = [...el.childNodes].find((n) => n.nodeType === 3 && /\d/.test(n.nodeValue));
      if (!nodo || /\[/.test(el.textContent)) return;
      const fine = nodo.nodeValue, a = leggi(fine); ora[k] = fine;
      if (!a || fermo()) return;
      const p = !nuovaSezione && prima[k] != null ? leggi(prima[k]) : null;
      if (!nuovaSezione && (!p || prima[k] === fine)) return;
      const da = p ? p.v : 0, t0 = performance.now(), durata = 650;
      const passo = (t) => {
        if (!nodo.isConnected) return;
        const x = Math.min(1, (t - t0) / durata), e = 1 - Math.pow(1 - x, 3);
        if (x >= 1) { nodo.nodeValue = fine; return; }
        const v = da + (a.v - da) * e;
        nodo.nodeValue = fine.slice(0, a.m.index) + scrivi(a.dec ? v : Math.round(v), a.dec, a.punti) + fine.slice(a.m.index + a.m[0].length);
        requestAnimationFrame(passo);
      };
      requestAnimationFrame(passo);
    });
    prima = ora;
  };

  // avviso di conferma (riquadro nero .msg): entra solo quando compare o cambia
  let msgPrima = '';
  const messaggio = () => {
    const m = document.querySelector('#app .msg'); const t = m ? m.textContent : '';
    if (m && t !== msgPrima && !fermo()) { m.classList.add('m-nuovo'); m.addEventListener('animationend', () => pulisci(m, 'm-nuovo'), { once: true }); }
    msgPrima = t;
  };

  // aggancio a render(): stesso disegno di prima, poi le animazioni
  let ultima = null, vista = null;
  const disegna = render;
  render = function () {
    disegna.apply(this, arguments);
    const k = chiave(), cambioVista = S.view !== vista, nuova = k !== ultima;
    if (nuova && ultima !== null) entra(cambioVista);
    numeri(nuova);
    messaggio();
    ultima = k; vista = S.view;
  };

  // avvisi: stesso testo di prima, ma l'animazione solo per il nuovo
  const visti = new Set();
  paintToasts = function () {
    const el = document.getElementById('toasts'); if (!el) return;
    el.innerHTML = S.live.toasts.slice(-3).map((x) => `<div class="toast glass${visti.has(x.id) ? ' m-visto' : ''}"><span class="pill dark">${x.chi}</span><span>${x.testo}</span></div>`).join('');
    S.live.toasts.forEach((x) => visti.add(x.id));
  };

  // 5 · Apertura (una volta sola, come l'avvio di JARVIS ma breve): barra, schede, contenuto
  requestAnimationFrame(() => {
    if (fermo()) return;
    const top = document.querySelector('header.top');
    if (top) { top.classList.add('m-apre'); top.addEventListener('animationend', () => pulisci(top, 'm-apre'), { once: true }); }
    inFila(document.getElementById('tabs'), 'm-entra', 12);
    entra(true);
  });
})();
