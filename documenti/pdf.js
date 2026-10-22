const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const dir = process.argv[2];
  const b = await chromium.launch();
  const p = await b.newPage();
  const lista = process.argv[3] ? [[process.argv[3], process.argv[4]]] : [['spiegazione', 'Messina - Spiegazione del progetto.pdf'], ['domande', 'Messina - Domande per papa e mamma.pdf'], ['informativa', 'Messina - Informativa presenze (bozza).pdf']];
  for (const [n, out] of lista) {
    await p.goto('file://' + path.join(dir, n + '.html'));
    await p.pdf({ path: path.join(dir, out), format: 'A4', printBackground: true, preferCSSPageSize: true,
      displayHeaderFooter: true, headerTemplate: '<div></div>',
      footerTemplate: '<div style="font-family:Inter;font-size:8px;color:#999;width:100%;text-align:right;padding-right:20mm"><span class="pageNumber"></span> / <span class="totalPages"></span></div>' });
  }
  await b.close();
})();
