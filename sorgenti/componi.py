# Mette dentro pagina.html i programmi veri già costruiti da messina-sistema (cartelle dist/ e anteprime dei siti).
# Uso: python3 sorgenti/componi.py <percorso di messina-sistema> <file di uscita>
import json, pathlib, re, sys

QUI = pathlib.Path(__file__).resolve().parent
SIS = pathlib.Path(sys.argv[1]).resolve()
USCITA = pathlib.Path(sys.argv[2])


def programma(nome):
    """index.html del programma con CSS, configurazione e JavaScript dentro la pagina (una cornice non carica file a parte)."""
    dist = SIS / 'apps' / nome / 'dist'
    h = (dist / 'index.html').read_text(encoding='utf8')
    css = (dist / 'main.css').read_text(encoding='utf8').replace('/*# sourceMappingURL=main.css.map */', '')
    js = (dist / 'main.js').read_text(encoding='utf8').replace('//# sourceMappingURL=main.js.map', '').replace('</script', '<\\/script')
    cfg = '// Prova: nessuna configurazione, quindi i programmi usano il database di esempio\nwindow.MESSINA = {};\n'
    sostituzioni = [
        ('<link rel="stylesheet" href="./main.css">', '<style>' + css + '</style>'),
        ('<script src="./config.js"></script>', '<script>' + cfg + '</script>'),
        ('<script type="module" src="./main.js"></script>', '<script type="module">' + js + '</script>'),
    ]
    for vecchio, nuovo in sostituzioni:
        if h.count(vecchio) != 1:
            raise SystemExit(f'{nome}: non trovo {vecchio}')
        h = h.replace(vecchio, nuovo)
    # nella cornice non servono manifest e icone dell'app installabile
    h = re.sub(r'<link rel="(manifest|apple-touch-icon|icon)"[^>]*>\n?', '', h)
    return h


def sito(nome):
    h = (SIS / 'apps' / nome / 'anteprima.html').read_text(encoding='utf8')
    return h.replace('<script src="config.js"></script>\n', '').replace('<script src="/config.js"></script>\n', '')


programmi = {
    'gestionale': programma('gestionale'), 'app': programma('app'), 'portale': programma('portale'), 'negozio': programma('negozio'),
    'sitoT': sito('sito-trasporti'), 'sitoC': sito('sito-corporation'),
}
js = 'var PROGRAMMI = ' + json.dumps(programmi, ensure_ascii=False).replace('<', '\\u003c') + ';'
pagina = (QUI / 'pagina.html').read_text(encoding='utf8')
if pagina.count('/*@@PROGRAMMI@@*/') != 1:
    raise SystemExit('pagina.html: segnaposto mancante')
USCITA.write_text(pagina.replace('/*@@PROGRAMMI@@*/', js), encoding='utf8')
print(f'{USCITA.name} ricostruito: {USCITA.stat().st_size // 1024} KB')
