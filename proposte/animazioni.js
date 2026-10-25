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
  // il telefono: la schermata si scopre dall'alto con la riga di luce
  const sopra = (cls) => {
    const sc = document.querySelector('#app .screen'); if (!sc) return;
    const r = document.createElement('i'); r.className = cls; r.setAttribute('aria-hidden', 'true');
    r.style.setProperty('--m-h', sc.clientHeight + 'px'); sc.appendChild(r);
    r.addEventListener('animationend', () => r.remove(), { once: true });
  };
  const accendi = () => {
    const ps = document.querySelector('#app .pscr'); if (!ps) return;
    ps.classList.add('m-svela'); ps.addEventListener('animationend', () => pulisci(ps, 'm-svela'), { once: true });
    sopra('m-riga');
  };
  const entra = (cambioVista) => {
    if (fermo()) return;
    const app = document.getElementById('app');
    if (app.querySelector('.pscr')) { if (cambioVista) inFila(app.querySelector('.appinfo'), 'm-entra', 8); accendi(); return; }
    const dentro = app.querySelector('.content');
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

  // nella stessa schermata di un'app: cosa è comparso o cambiato dall'ultimo tocco
  const firma = (el) => el.tagName + '|' + el.className + '|' + (el.getAttribute('style') || '') + '|' + el.textContent.trim().slice(0, 90);
  let segniPrima = null;
  const esiti = (stessa) => {
    const ps = document.querySelector('#app .pscr');
    if (!ps) { segniPrima = null; return; }
    const els = [...ps.querySelectorAll('.pcard,.kvp,.pill,span[style*="border-radius:99px"]')];
    const ora = els.map(firma);
    if (stessa && segniPrima && !fermo()) {
      const resto = {}; segniPrima.forEach((f) => { resto[f] = (resto[f] || 0) + 1; });
      const nuovi = [];
      els.forEach((el, i) => { const f = ora[i]; if (resto[f]) resto[f]--; else nuovi.push(el); });
      nuovi.forEach((el) => {
        if (nuovi.some((x) => x !== el && x.contains(el) && !/var\(--ok\)/.test(el.getAttribute('style') || ''))) return;   // ci pensa il riquadro che lo contiene
        const st = el.getAttribute('style') || '';
        let cls = 'm-entra';
        if (/var\(--alert\)/.test(st)) cls = 'm-allarme';
        else if (el.tagName === 'SPAN' || el.classList.contains('pill')) cls = /var\(--ok\)/.test(st) || el.classList.contains('ok') ? 'm-pop' : '';
        else if (/border:2px solid var\(--ok\)/.test(st)) cls = 'm-ok';
        if (!cls) return;
        el.classList.add(cls); el.addEventListener('animationend', () => pulisci(el, cls), { once: true });
      });
    }
    segniPrima = ora;
  };
  let barrePrima = [];
  const barre = (stessa) => {
    const bs = [...document.querySelectorAll('#app .bar i')];
    if (stessa && !fermo()) bs.forEach((el, i) => {
      const da = barrePrima[i], a = el.style.width;
      if (da == null || da === a) return;
      el.style.width = da; void el.offsetWidth;
      el.classList.add('m-barra'); el.style.width = a;
      el.addEventListener('transitionend', () => pulisci(el, 'm-barra'), { once: true });
    });
    barrePrima = bs.map((el) => el.style.width);
  };
  const caricamento = () => {
    document.querySelectorAll('#app .pscr .pcard').forEach((el) => { if (/^Controllo la foto/.test(el.textContent.trim())) el.classList.add('m-carica'); });
  };
  // l'ultimo tasto toccato: dopo uno sparo passa la fascia di scansione
  let atto = '';
  document.addEventListener('click', (e) => { const el = e.target.closest('[data-act]'); atto = el ? el.dataset.act : ''; }, true);

  // il QR del badge: quando cambia (ogni 30 secondi) quello nuovo entra con una messa a fuoco
  let qrBox = null, qrDentro = null;
  setInterval(() => {
    const q = document.getElementById('qrbox'), c = q && q.firstElementChild;
    if (q && q === qrBox && c !== qrDentro && !fermo()) {
      q.classList.add('m-qr'); q.addEventListener('animationend', () => pulisci(q, 'm-qr'), { once: true });
    }
    qrBox = q; qrDentro = c;
  }, 100);

  // aggancio a render(): stesso disegno di prima, poi le animazioni
  let ultima = null, vista = null;
  const disegna = render;
  render = function () {
    disegna.apply(this, arguments);
    const k = chiave(), cambioVista = S.view !== vista, nuova = k !== ultima;
    if (nuova && ultima !== null) entra(cambioVista);
    numeri(nuova);
    messaggio();
    esiti(!nuova);
    barre(!nuova);
    caricamento();
    if (/Scan$/.test(atto) && !fermo()) sopra('m-scan');
    atto = '';
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
