# Toglie la Presentazione, porta il Portale dentro Autotrasporti, aggiunge i due siti vetrina.
import json, re, sys
P = sys.argv[1]
s = open(P, encoding='utf8').read()

def rep(old, new, count=1):
    global s
    if old not in s:
        raise SystemExit('NON TROVATO: ' + old[:90])
    s = s.replace(old, new, count)

# --- CSS: via la regia e lo spot, restano i toast; stile della finestra del sito
lines = s.split('\n')
out = []
for ln in lines:
    if re.search(r'\.regia|\.rtit|\.rtxt|\.rbtn|demo-on|^\.spot\{|@keyframes spot', ln):
        continue
    out.append(ln)
s = '\n'.join(out)
rep('@media (prefers-reduced-motion:reduce){.spot,.toast{animation:none}}', '''@media (prefers-reduced-motion:reduce){.toast{animation:none}}
.browser{border-radius:22px;overflow:hidden;padding:0}
.bbar{display:flex;gap:12px;align-items:center;padding:10px 14px;border-bottom:1px solid var(--line)}
.bbar .dots{display:flex;gap:6px;flex:none}.bbar .dots i{width:10px;height:10px;border-radius:99px;background:rgba(17,18,20,.16)}
.bbar .url{flex:1;min-width:0;text-align:center;font-size:13px;color:var(--muted);background:var(--soft);border-radius:99px;padding:6px 12px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sitoframe{display:block;width:100%;height:calc(100vh - 230px);height:calc(100dvh - 230px);min-height:520px;border:0;background:#f2f3f5}
.portbar{display:flex;flex-direction:column;gap:12px;padding:14px 16px;margin-bottom:14px}
@media (max-width:760px){.sitoframe{height:calc(100dvh - 190px);min-height:460px}}''')
rep('<div id="regia"></div>\n', '')

# --- viste e menu
rep("['demo','Presentazione'],", '')
rep(",['portale','Portale clienti']]", ",['sitoT','Sito Autotrasporti'],['sitoC','Sito Corporation']]")
rep("['clienti','Clienti'],['fatture','Fatturazione']", "['clienti','Clienti'],['portale','Portale'],['fatture','Fatturazione']")
s = s.replace("'Cerca cliente, bolla, targa'", "'Cerca'").replace("'Cerca seriale, modello, lotto'", "'Cerca'")

# --- presentazione: via tutto il codice
a = s.index('/* ---------- PRESENTAZIONE')
z = s.index('/* ---------- VISTE ---------- */')
s = s[:a] + s[z:]
rep("S.demo={on:false,i:0,auto:false,min:false,spot:null,timers:[]};\n", '')
rep("const INIT=JSON.parse(JSON.stringify(S));\nconst ORDINI0=ORDINI.map(x=>x.slice());\n", '')
rep("function oraDemo(){return S.demo.on&&DEMO[S.demo.i]?DEMO[S.demo.i].ora:ora();}\n", '')
s = s.replace('oraDemo()', 'ora()')
rep("eventi, portale, J7, presentazione", "eventi, portale, J7, siti")
rep("""  document.getElementById('regia').innerHTML=regia();
  if(S.demo.on) applySpot();
""", '')

# --- portale dentro Autotrasporti
rep("A.pGo=v=>{S.p.sec=v; S.p.pod=false; S.view='portale'; window.scrollTo(0,0);};",
    "A.pGo=v=>{S.p.sec=v; S.p.pod=false; S.view='trasp'; S.t.sec='portale'; window.scrollTo(0,0);};\nA.pSec=v=>{S.p.sec=v; S.p.pod=false;};")
rep("function portale(){", "function portaleBody(){")
old_ret = s[s.index("  return hint('scegli il cliente qui sotto: Snam vede"):]
old_ret = old_ret[:old_ret.index('\n') + 1]
rep(old_ret, """  const testa=`<div class="glass portbar"><div class="row between"><b style="font-size:17px">Messina Autotrasporti <span style="font-weight:500">· Area clienti</span></b><span class="lbl">portale.[dominio] · entra ${p.cli}</span></div>
    <div class="row" style="gap:6px">${P_NAV.map(x=>chip(x[1],'pSec',x[0],s===x[0])).join('')}</div></div>`;
  return cli+'<div style="height:12px"></div>'+testa+'<div class="stack">'+body+'</div>';
""")
rep("  if(s==='mail'){\n    title='Mail'; hintTxt='apri la mail di Snam",
    "  if(s==='portale'){\n    title='Portale'; hintTxt='è il portale dei clienti di Messina Autotrasporti, visto con i loro occhi. Scegli Snam o Econocom: Snam vede spedizioni e magazzino dal vivo, Econocom i telefoni UniCredit con IMEI, cespite e utente.';\n    body=portaleBody();\n  }\n  if(s==='mail'){\n    title='Mail'; hintTxt='apri la mail di Snam")

# --- intro: niente presentazione, portale dentro Autotrasporti, siti
rep("    ['portale','Portale clienti','Quello che vedono Snam ed Econocom: spedizioni, magazzino con i seriali, giacenze e fatture.'],\n    ['demo','Presentazione','Una giornata intera in Messina che si svolge da sola, dalla mail del mattino alle fatture della sera.']",
    "    ['portale','Portale clienti','Dentro Autotrasporti: quello che vedono Snam ed Econocom. Spedizioni, magazzino con i seriali, giacenze e fatture.','pGo','home'],\n    ['sitoT','Sito Autotrasporti','Il sito pubblico di Messina Autotrasporti: servizi, flotta, traccia, preventivi e candidature che arrivano nella Mail.'],\n    ['sitoC','Sito Corporation','Il sito pubblico di Messina Corporation: cancellazione dei dati, valutazione dei lotti, gradi e il tasto Negozio.']")
rep('<button class="part glass" data-act="view" data-arg="${p[0]}">', '<button class="part glass" data-act="${p[3]||\'view\'}" data-arg="${p[4]||p[0]}">')


# --- intro: programmi e siti in due gruppi
rep("  const parts=[", "  const WEB=['negozio','portale','sitoT','sitoC'];\n  const parts=[")
rep("""  <div class="grid g4" style="margin-bottom:16px">
    ${parts.map(p=>`<button class="part glass" data-act="${p[3]||'view'}" data-arg="${p[4]||p[0]}"><h3>${p[1]}</h3><span class="muted">${p[2]}</span><span class="go">Apri</span></button>`).join('')}
  </div>""", """  <h2 class="gruppo-tit">Programmi</h2>
  <div class="grid g-prog" style="margin-bottom:22px">
    ${parts.filter(p=>WEB.indexOf(p[0])<0).map(p=>`<button class="part glass" data-act="${p[3]||'view'}" data-arg="${p[4]||p[0]}"><h3>${p[1]}</h3><span class="muted">${p[2]}</span><span class="go">Apri</span></button>`).join('')}
  </div>
  <h2 class="gruppo-tit">Siti web</h2>
  <div class="grid g-siti" style="margin-bottom:16px">
    ${WEB.map(k=>parts.find(p=>p[0]===k)).map(p=>`<button class="part sitocard glass" data-act="${p[3]||'view'}" data-arg="${p[4]||p[0]}"><span class="minibar" aria-hidden="true"><i></i><i></i><i></i><span>${({negozio:'negozio.[dominio]',portale:'portale.[dominio]',sitoT:'www.messina-autotrasporti.it',sitoC:'www.[dominio-corporation]'})[p[0]]}</span></span><h3>${p[1]}</h3><span class="muted">${p[2]}</span><span class="go">Apri</span></button>`).join('')}
  </div>""")
rep('.portbar{', """.gruppo-tit{font-size:20px;font-weight:800;letter-spacing:-.02em;margin:6px 2px 12px}
.g-prog{grid-template-columns:repeat(3,minmax(0,1fr))}
.g-siti{grid-template-columns:repeat(4,minmax(0,1fr))}
.sitocard{padding:20px}
.sitocard h3{font-size:20px;letter-spacing:-.02em}
.minibar{display:flex;align-items:center;gap:6px;padding:8px 10px;border-radius:12px;background:var(--soft);margin-bottom:8px}
.minibar i{width:8px;height:8px;border-radius:99px;background:rgba(17,18,20,.18);flex:none}
.minibar span{flex:1;min-width:0;text-align:center;font-size:12px;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
@media (max-width:1000px){.g-prog{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:1000px){.g-siti{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:640px){.g-siti{grid-template-columns:1fr}}
.portbar{""")

# --- mail: le richieste dal sito in cima alla lista
rep("const filt=mails.map((m,i)=>Object.assign({i:i},m)).filter(m=>st.cart==='In arrivo'||m.cart===st.cart);",
    "const filt=mails.map((m,i)=>Object.assign({i:i},m)).filter(m=>st.cart==='In arrivo'||m.cart===st.cart).sort((x,y)=>(y.top||0)-(x.top||0));")
rep("const ab={btn:b('Crea bolla da questa mail','tCrea'),",
    "const ab=T_MAILS[t.mail].sito?{btn:b('Prepara il preventivo','tReply'),msg:''}:{btn:b('Crea bolla da questa mail','tCrea'),")
# chiude la graffa dell'oggetto originale: l'espressione diventa cond?{...}:{...}

# --- siti vetrina
sitoT = open(sys.argv[2], encoding='utf8').read()
sitoC = open(sys.argv[3], encoding='utf8').read()
def prepara(h):
    h = h.replace('<script src="config.js"></script>\n', '')
    h = h.replace('href="privacy.html"', 'href="#" data-link="privacyUrl"')
    return json.dumps(h, ensure_ascii=False).replace('<', '\\u003c')
siti_js = """
/* siti vetrina: lo stesso HTML dei siti veri, dentro una finestra */
const SITO_T=%s;
const SITO_C=%s;
const escA=x=>x.replace(/&/g,'&amp;').replace(/"/g,'&quot;');
function sito(k){
  const t=k==='T';
  return hint(t?'è il sito pubblico di Messina Autotrasporti, con tutte le sue pagine: usa il menu come su un sito vero. Prova «Preventivo», «Prenota un ritiro» o «Lavora con noi»: ogni richiesta arriva in Autotrasporti › Mail. In «Traccia» scrivi un numero qualsiasi.':'è il sito pubblico di Messina Corporation, con tutte le sue pagine. «Negozio» porta al negozio online; «Valuta un lotto» arriva in Corporation › Mail, cartella Lotti.')+
    `<div class="browser glass"><div class="bbar"><span class="dots" aria-hidden="true"><i></i><i></i><i></i></span><span class="url">${t?'www.messina-autotrasporti.it':'www.[dominio-corporation]'}</span></div><iframe class="sitoframe" data-k="${k}" title="${t?'Sito di Messina Autotrasporti':'Sito di Messina Corporation'}" srcdoc="${escA(t?SITO_T:SITO_C)}"></iframe></div>`;
}
window.addEventListener('message',e=>{
  const d=e.data; if(!d||typeof d!=='object')return;
  const f=[...document.querySelectorAll('iframe.sitoframe')].find(x=>x.contentWindow===e.source); if(!f)return;
  if(d.tipo==='messina-sito'&&d.corpo){
    const c=d.corpo, chi=(c.nome||'').slice(0,80)+(c.azienda?' ('+String(c.azienda).slice(0,80)+')':''), det=c.dettagli||{};
    const righe=Object.keys(det).map(k=>k+': '+(Array.isArray(det[k])?det[k].join(', '):det[k])).join('\\n');
    const testo=['Nome: '+c.nome,c.azienda&&'Azienda: '+c.azienda,'Email: '+c.email,c.telefono&&'Telefono: '+c.telefono,righe,c.note&&'\\n'+c.note].filter(Boolean).join('\\n');
    const esc=x=>String(x).replace(/[&<>"]/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]));
    const ant=esc((c.note||righe||'').slice(0,60))+'…', base={da:esc(chi),ind:esc(c.email),ora:ora(),ant:ant,testo:esc(testo),all:'',top:Date.now()};
    if(c.sito==='trasporti'){
      if(c.tipo==='ritiro'){
        T_MAILS.push(Object.assign(base,{ogg:'Richiesta di ritiro dal sito',tag:'Ordine',cart:'Ordini',bozza:'Buongiorno '+esc(c.nome)+',\\nconfermiamo il ritiro per [giorno], fascia [orario]. Grazie.\\nUfficio ordini, Messina Autotrasporti'}));
        evt('Sito','Nuova richiesta di ritiro da '+esc(chi)+': è in Autotrasporti › Mail, cartella Ordini. Da lì si crea la bolla.');
      } else if(c.tipo==='candidatura'){
        T_MAILS.push(Object.assign(base,{ogg:'Candidatura dal sito',tag:'Personale',cart:'In arrivo',bozza:'Buongiorno '+esc(c.nome)+',\\ngrazie per la candidatura. La chiamiamo per un colloquio [giorno].\\nMessina Autotrasporti'}));
        evt('Sito','Nuova candidatura da '+esc(chi)+': è in Autotrasporti › Mail.');
      } else if(c.tipo==='contatto'){
        T_MAILS.push(Object.assign(base,{ogg:'Messaggio dal sito',tag:'Sito',cart:'In arrivo',bozza:'Buongiorno '+esc(c.nome)+',\\ngrazie per il messaggio. [risposta]\\nMessina Autotrasporti'}));
        evt('Sito','Nuovo messaggio dal sito da '+esc(chi)+': è in Autotrasporti › Mail.');
      } else {
        T_MAILS.push(Object.assign(base,{ogg:'Richiesta di preventivo dal sito',tag:'Preventivo',cart:'Clienti',sito:true,
          bozza:'Buongiorno '+esc(c.nome)+',\\ngrazie per la richiesta. Per '+esc(righe.replace(/\\n/g,'; ')||'la spedizione indicata')+' il nostro preventivo è di € [importo], tariffa [tipo]. Restiamo a disposizione.\\nUfficio commerciale, Messina Autotrasporti'}));
        evt('Sito','Nuova richiesta di preventivo da '+esc(chi)+': è in Autotrasporti › Mail, cartella Clienti.');
      }
    } else if(c.tipo==='contatto'){
      C_MAILS.push(Object.assign(base,{ogg:'Messaggio dal sito',tag:'Sito',cart:'In arrivo',bozza:'Buongiorno '+esc(c.nome)+',\\ngrazie per il messaggio. [risposta]\\nMessina Corporation',az:'Rispondi',azMsg:'Usa «Rispondi»: la bozza è già pronta.',azGo:'home'}));
      evt('Sito','Nuovo messaggio dal sito da '+esc(chi)+': è in Corporation › Mail.');
    } else {
      C_MAILS.push(Object.assign(base,{ogg:'Lotto da valutare dal sito',tag:'Lotti',cart:'Lotti',
        bozza:'Buongiorno '+esc(c.nome)+',\\ngrazie. Per il lotto indicato vi proponiamo ritiro, cancellazione certificata con rapporto per seriale e una valutazione di € [importo]. Possiamo passare [giorno].\\nMessina Corporation',
        az:'Rispondi con la valutazione',azMsg:'Usa «Rispondi»: la bozza con la proposta è già pronta.',azGo:'lotti'}));
      evt('Sito','Nuovo lotto da valutare da '+esc(chi)+': è in Corporation › Mail, cartella Lotti.');
    }
  }
  if(d.tipo==='messina-pagina'){const u=f.parentNode.querySelector('.url'); if(u) u.textContent=u.textContent.split('/')[0]+(d.path==='/'?'':d.path.replace(/\/$/,'')); return;}
  if(d.tipo==='messina-vai'){
    const v=d.dove;
    if(v==='negozioUrl'){S.view='negozio'; S.n.view='home';}
    else if(v==='portaleUrl'){A.pGo('home');}
    else if(v==='corporationUrl'){S.view='sitoC';}
    else if(v==='trasportiUrl'){S.view='sitoT';}
    else if(v==='privacyUrl'){evt('Sito','L’informativa privacy è una bozza: la fa verificare il consulente prima di metterla online.'); return;}
    else return;
    window.scrollTo(0,0); render();
  }
});
""" % (prepara(sitoT), prepara(sitoC))
rep('/* ---------- VISTE ---------- */', siti_js + '\n/* ---------- VISTE ---------- */')

rep("app.innerHTML = v==='intro'?intro():v==='demo'?demoView():v==='portale'?portale():v==='trasp'?trasp():",
    "const fr=app.querySelector('iframe.sitoframe');\n  if((v==='sitoT'||v==='sitoC')&&fr&&fr.dataset.k===v.slice(-1)) return;   // il sito resta com'è: niente ricarica mentre lo si usa\n  app.innerHTML = v==='intro'?intro():v==='sitoT'?sito('T'):v==='sitoC'?sito('C'):v==='trasp'?trasp():")

open(P, 'w', encoding='utf8').write(s)
for w in ['DEMO', 'S.demo', 'regia(', 'applySpot', 'demoView', "'portale'?"]:
    if w in s: print('RESTA:', w)
print('ok', len(s))
