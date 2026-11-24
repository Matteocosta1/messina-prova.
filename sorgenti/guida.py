#!/usr/bin/env python3
"""Riallinea il manuale del mockup con quello del programma (supabase/functions/_comune/guida.json).
Uso: python3 sorgenti/guida.py /percorso/messina-sistema"""
import json, re, sys, pathlib
sis = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '../messina-sistema')
g = json.loads((sis / 'supabase/functions/_comune/guida.json').read_text())
p = pathlib.Path(__file__).resolve().parent.parent / 'index.html'
s = p.read_text()
nuovo = '/* GUIDA:inizio (generato da sorgenti/guida.py: non modificare qui) */\nconst GUIDA=' + json.dumps(g['sezioni'], ensure_ascii=False) + ';\n/* GUIDA:fine */'
s2, n = re.subn(r'/\* GUIDA:inizio.*?/\* GUIDA:fine \*/', lambda m: nuovo, s, flags=re.S)
if n != 1: sys.exit('segnaposto GUIDA non trovato')
p.write_text(s2); print('guida aggiornata:', len(g['sezioni']), 'sezioni')
