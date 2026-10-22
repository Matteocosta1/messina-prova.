# Modifiche del 20/10 notte (vocale + "procedi"): Non Consegnato sempre attivo, anomalie del satellitare visibili,
# scaffali con Articoli e Arrivo, negozio con scheda completa e gradi A-D, Ricambi.
import sys
P = sys.argv[1]
s = open(P, encoding='utf8').read()

def rep(old, new, count=1):
    global s
    if old not in s:
        raise SystemExit('NON TROVATO: ' + old[:100])
    s = s.replace(old, new, count)

# ===== 1. Non Consegnato sempre attivo in fondo alla prima pagina =====
rep("""      <button class="bigbtn" data-act="aAvanti" ${d1?'':off}>Avanti</button>
    </div>`;""", """      <button class="bigbtn" data-act="aAvanti" ${d1?'':off}>Avanti</button>
      <button class="bigbtn ghost" data-act="aMancata">Non Consegnato</button>
    </div>`;""")
rep("  aMancata:()=>{if(S.a.scr==='firma'&&S.a.foto[S.a.cur]!==2)return; S.a.scr='mancata';},",
    "  aMancata:()=>{if(S.a.scr==='firma'&&S.a.foto[S.a.cur]!==2)return; if(S.a.scr==='dett'||S.a.scr==='firma')S.a.mancDa=S.a.scr; S.a.scr='mancata';},\n  aMancBack:()=>{S.a.scr=S.a.mancDa||'dett';},")
rep("""  if(a.scr==='mancata'){
    inner=`<div class="pscr">
      <button class="back" data-act="aFirma">Indietro</button>""", """  if(a.scr==='mancata'){
    inner=`<div class="pscr">
      <button class="back" data-act="aMancBack">Indietro</button>""")
rep(""">Non consegnato</button>""", """>Non Consegnato</button>""")
rep("poi «Consegnato» o «Non consegnato».</li><li>Su un’altra fermata prova «Non consegnato» e poi «Torna in magazzino: giacenza».</li>",
    "poi «Consegnato» o «Non Consegnato».</li><li>Su un’altra fermata premi subito «Non Consegnato» in fondo alla prima pagina, senza scansionare niente, e poi «Torna in magazzino: giacenza».</li>")

# ===== 2. Anomalie: la sezione Satellitare c'era nel conteggio ma non tra le schede =====
rep("    const SEZ=['Magazzino','Missioni','Bolle','Presenze','Fatturazione','Telepass'];",
    "    const SEZ=['Magazzino','Missioni','Bolle','Presenze','Fatturazione','Telepass','Satellitare'];")

# ===== 3. Scaffali: Articoli (quantità e tipo) e Arrivo con la data completa =====
rep("const SC_CONT={Apple:'Colli consegne Nord',Snam:'Bancale materiale con seriali',Luxiona:'Bancale ordine magazzino',Econocom:'Telefoni con IMEI e cespite',Corporation:'Bancale computer Messina Corporation'};",
    """const SC_CONT={Apple:'Colli consegne Nord',Snam:'Bancale materiale con seriali',Luxiona:'Bancale ordine magazzino',Econocom:'Telefoni con IMEI e cespite',Corporation:'Bancale computer Messina Corporation'};
const SC_ART={Apple:['10 iPhone, 10 iPad','24 colli MacBook','12 iPhone, 6 Apple Watch','8 iMac'],Snam:['18 apparati con seriale','6 cavi, 4 sensori','12 contatori','2 armadi tecnici'],Luxiona:['32 lampade','14 plafoniere','40 faretti','20 alimentatori'],Econocom:['1.000 telefoni Motorola','500 telefoni Samsung','300 caricabatterie','200 cover'],Corporation:['40 portatili','12 PC fissi','20 monitor','35 portatili Lenovo']};
const scArrivo=(sel,pi,po)=>{const d=new Date(); const lungo=(sel*7+pi*3+po)%11===0; d.setDate(d.getDate()-((sel+pi+po)%9+1)-(lungo?420:0)); return d.toLocaleDateString('it-IT',{day:'2-digit',month:'2-digit',year:'numeric'});};""")
rep("<td>${full?SC_CONT[cli]:'—'}</td><td>${full?((sel+pi+po)%9+1)+' giorni':'—'}</td>",
    "<td>${full?SC_ART[cli][(pi+po)%4]:'—'}</td><td>${full?scArrivo(sel,pi,po):'—'}</td>")
rep("<th>Posto</th><th>Piano</th><th>Cliente</th><th>Cosa c’è</th><th>Da</th>", "<th>Posto</th><th>Piano</th><th>Cliente</th><th>Articoli</th><th>Arrivo</th>")
rep("hintTxt='tocca uno scaffale e poi un posto per vedere il Contenuto;", "hintTxt='tocca uno scaffale e poi un posto per vedere gli Articoli;")
rep("<h3 style=\"font-size:20px\">Contenuto · ${t.posto}</h3>", "<h3 style=\"font-size:20px\">Articoli · ${t.posto}</h3>")

# ===== 4. Negozio: gradi A-D e scheda completa =====
rep("""const SHOP=[
 {brand:'Lenovo',name:'ThinkPad T14 Gen 2',spec:'Intel i5 · 14" Full HD',base:249},
 {brand:'HP',name:'EliteBook 840 G8',spec:'Intel i7 · 14" Full HD',base:309},
 {brand:'Dell',name:'Latitude 5420',spec:'Intel i5 · 14" Full HD',base:209},
 {brand:'Apple',name:'MacBook Air M1',spec:'Apple M1 · 13,3" Retina',base:449},
 {brand:'Lenovo',name:'ThinkPad X1 Carbon',spec:'Intel i7 · 14" Full HD',base:379},
 {brand:'HP',name:'ProBook 450 G8',spec:'Intel i5 · 15,6" Full HD',base:219}
];""", """const SHOP=[
 {brand:'Lenovo',name:'ThinkPad T14 Gen 2',spec:'Intel i5 · 14" Full HD',base:249,gen:'Gen 2 (2021)',cpu:'Intel Core i5-1135G7, 11ª generazione, 4 core',gpu:'Intel Iris Xe',schermo:'14" Full HD IPS, 1920 × 1080, antiriflesso',disco:'SSD NVMe',batt:'86% della capacità originale',os:'Windows 11 Pro',tastiera:'Italiana, retroilluminata',porte:'2 USB-C Thunderbolt 4, 2 USB-A, HDMI, Ethernet, jack audio',rete:'Wi-Fi 6, Bluetooth 5.1',webcam:'720p con copertura',peso:'1,47 kg'},
 {brand:'HP',name:'EliteBook 840 G8',spec:'Intel i7 · 14" Full HD',base:309,gen:'G8 (2021)',cpu:'Intel Core i7-1165G7, 11ª generazione, 4 core',gpu:'Intel Iris Xe',schermo:'14" Full HD IPS, 1920 × 1080',disco:'SSD NVMe',batt:'89% della capacità originale',os:'Windows 11 Pro',tastiera:'Italiana, retroilluminata',porte:'2 USB-C Thunderbolt 4, 2 USB-A, HDMI, jack audio',rete:'Wi-Fi 6, Bluetooth 5.2',webcam:'720p con copertura',peso:'1,33 kg'},
 {brand:'Dell',name:'Latitude 5420',spec:'Intel i5 · 14" Full HD',base:209,gen:'5420 (2021)',cpu:'Intel Core i5-1145G7, 11ª generazione, 4 core',gpu:'Intel Iris Xe',schermo:'14" Full HD, 1920 × 1080',disco:'SSD NVMe',batt:'82% della capacità originale',os:'Windows 11 Pro',tastiera:'Italiana',porte:'USB-C Thunderbolt 4, 2 USB-A, HDMI, Ethernet',rete:'Wi-Fi 6, Bluetooth 5.1',webcam:'720p',peso:'1,36 kg'},
 {brand:'Apple',name:'MacBook Air M1',spec:'Apple M1 · 13,3" Retina',base:449,gen:'M1 (2020)',cpu:'Apple M1, 8 core',gpu:'Apple M1, 7 core',schermo:'13,3" Retina, 2560 × 1600',disco:'SSD',batt:'88% della capacità originale',os:'macOS Sonoma',tastiera:'Italiana, retroilluminata',porte:'2 Thunderbolt / USB 4, jack audio',rete:'Wi-Fi 6, Bluetooth 5.0',webcam:'720p FaceTime HD',peso:'1,29 kg'},
 {brand:'Lenovo',name:'ThinkPad X1 Carbon',spec:'Intel i7 · 14" Full HD',base:379,gen:'Gen 9 (2021)',cpu:'Intel Core i7-1185G7, 11ª generazione, 4 core',gpu:'Intel Iris Xe',schermo:'14" WUXGA IPS, 1920 × 1200',disco:'SSD NVMe',batt:'84% della capacità originale',os:'Windows 11 Pro',tastiera:'Italiana, retroilluminata',porte:'2 USB-C Thunderbolt 4, 2 USB-A, HDMI, jack audio',rete:'Wi-Fi 6, Bluetooth 5.2',webcam:'720p con copertura',peso:'1,13 kg'},
 {brand:'HP',name:'ProBook 450 G8',spec:'Intel i5 · 15,6" Full HD',base:219,gen:'G8 (2021)',cpu:'Intel Core i5-1135G7, 11ª generazione, 4 core',gpu:'Intel Iris Xe',schermo:'15,6" Full HD, 1920 × 1080',disco:'SSD NVMe',batt:'80% della capacità originale',os:'Windows 11 Pro',tastiera:'Italiana con tastierino numerico',porte:'USB-C, 2 USB-A, HDMI, Ethernet, jack audio',rete:'Wi-Fi 6, Bluetooth 5.2',webcam:'720p',peso:'1,74 kg'}
];
const RICAMBI=[
 ['Display 14" Full HD','ThinkPad T14 Gen 2','PF3XXXX7','L-014',39,'Disponibile'],
 ['Tastiera italiana retroilluminata','EliteBook 840 G8','5CGXXXX4','L-014',29,'Disponibile'],
 ['Scheda madre i5-1145G7, 8 GB','Latitude 5420','JXXXXX9','L-013',89,'Disponibile'],
 ['Batteria, 81%','ThinkPad X1 Carbon','PF2XXXX2','L-015',35,'Venduto'],
 ['SSD 256 GB, dati cancellati con rapporto','ProBook 450 G8','5CDXXXX1','L-015',19,'Disponibile'],
 ['Cerniere e scocca inferiore','MacBook Air M1','C02XXXX5','L-015',25,'Disponibile']
];""")
rep("const GDELTA={'Ottimo':40,'Buono':0,'Discreto':-40};", "const GDELTA={'Grado A':40,'Grado B':0,'Grado C':-40,'Grado D':-90};")
a = s.index("const GDESC={'Ottimo':"); z = s.index("};", a) + 2
s = s[:a] + "const GDESC={'Grado A':'Quasi impossibile distinguerlo da nuovo. Al massimo micro-segni visibili da vicino. Funziona al 100%.','Grado B':'Leggeri segni d’uso sulla scocca. Schermo e tastiera in ordine. Funziona al 100%.','Grado C':'Segni evidenti d’uso, possibile piccola ammaccatura. Funziona al 100%.','Grado D':'Funziona al 100%, ma ha la scocca rotta o danni estetici importanti. Testato e garantito come gli altri gradi.'};" + s[z:]
rep("  nOpen:i=>{S.n.view='prod'; S.n.pid=+i; S.n.g='Buono'; S.n.ram=16; S.n.added=false;},",
    "  nOpen:i=>{S.n.view='prod'; S.n.pid=+i; S.n.g='Grado B'; S.n.ram=16; S.n.added=false;},\n  nRic:()=>{S.n.view='ricambi'; window.scrollTo(0,0);},")
rep("c.det.indexOf('Ottimo')===0?'A':(c.det.indexOf('Buono')===0?'B':'C')", "((c.det.match(/Grado ([A-D])/)||[])[1]||'B')")
rep("""<div><b>Condizioni</b><div class="gradebox" style="margin-top:8px">${['Discreto','Buono','Ottimo'].map(g=>""",
    """<div><b>Grado</b><div class="gradebox g4b" style="margin-top:8px">${['Grado A','Grado B','Grado C','Grado D'].map(g=>""")
rep("""        <div class="row">${pill('Dati cancellati con metodo certificato')}${pill('Garanzia [mesi]')}${pill('Reso entro [giorni]')}</div>
      </div></div></div>`;""", """        <div class="row">${pill('Dati cancellati con metodo certificato')}${pill('Garanzia [mesi]')}${pill('Reso entro [giorni]')}</div>
      </div></div>
      <div class="pcard" style="padding:18px;margin-top:18px"><b style="font-size:20px">Scheda tecnica</b><div class="schedat">${[['Marca',p.brand],['Modello',p.name],['Generazione',p.gen],['Processore',p.cpu],['Scheda grafica',p.gpu],['RAM',n.ram+' GB'],['Disco','256 GB '+p.disco],['Schermo',p.schermo],['Batteria',p.batt],['Sistema operativo',p.os],['Tastiera',p.tastiera],['Porte',p.porte],['Rete',p.rete],['Webcam',p.webcam],['Peso',p.peso],['Grado',n.g],['Dati','Cancellati con software certificato, rapporto per numero di serie']].map(r=>`<div><span class="lbl">${r[0]}</span><b>${r[1]}</b></div>`).join('')}</div></div></div>`;""")
rep("""<button class="tab" data-act="nHome">Per aziende</button></div>""", """<button class="tab" data-act="nHome">Per aziende</button><button class="tab" data-act="nRic">Ricambi</button></div>""")
rep("""  if(n.view==='pay'){""", """  if(n.view==='ricambi'){
    inner=`<div class="shopbody"><h1 class="shoph1">Ricambi</h1><p class="muted" style="max-width:60ch;margin:0 0 18px">Pezzi originali smontati dai computer che non si possono vendere interi. Ogni ricambio dice da quale modello arriva. I dischi si vendono solo dopo la cancellazione certificata dei dati.</p>
      <div class="grid" style="grid-template-columns:repeat(auto-fill,minmax(230px,1fr))">${RICAMBI.filter(r=>r[5]==='Disponibile').map(r=>`<div class="prod" style="cursor:default"><span class="lbl">Da ${r[1]}</span><b style="font-size:18px;letter-spacing:-.02em">${r[0]}</b><span><b style="font-size:20px">€ ${r[4]}</b></span></div>`).join('')}</div></div>`;
  }
  if(n.view==='pay'){""")
rep("return hint('apri un computer, cambia condizione e memoria e guarda il prezzo che cambia. Poi aggiungilo al carrello.')",
    "return hint('apri un computer: cambia grado (A, B, C, D) e memoria e guarda il prezzo; sotto c’è la scheda tecnica completa. In alto anche «Ricambi».')")

# ===== 5. Corporation: grado D nell'inventario e voce Ricambi =====
rep("${['Tutti','A','B','C'].map(x=>chip(x==='Tutti'?'Tutti i gradi':'Grado '+x,'cGrado',x,c.grado===x)).join('')}",
    "${['Tutti','A','B','C','D'].map(x=>chip(x==='Tutti'?'Tutti i gradi':'Grado '+x,'cGrado',x,c.grado===x)).join('')}")
rep(""" {brand:'HP',model:'ProBook 450 G8',cpu:'i5-1135G7',ram:'8 GB',disk:'256 GB SSD',screen:'15,6"',grade:'B',dif:'Batteria sotto 80%',lotto:'L-015',sn:'5CDXXXXX',shelf:'Ricevimento',banc:'B-0146',costo:'€ 61',price:'€ 219',stato:'Reso',siti:'—',gpu:'Intel UHD',gg:1}
];""", """ {brand:'HP',model:'ProBook 450 G8',cpu:'i5-1135G7',ram:'8 GB',disk:'256 GB SSD',screen:'15,6"',grade:'B',dif:'Batteria sotto 80%',lotto:'L-015',sn:'5CDXXXXX',shelf:'Ricevimento',banc:'B-0146',costo:'€ 61',price:'€ 219',stato:'Reso',siti:'—',gpu:'Intel UHD',gg:1},
 {brand:'Lenovo',model:'ThinkPad T14 Gen 2',cpu:'i5-1135G7',ram:'16 GB',disk:'256 GB SSD',screen:'14"',grade:'D',dif:'Scocca inferiore crepata, funziona al 100%',lotto:'L-015',sn:'PF3XXXX8',shelf:'S11-1-2',banc:'B-0145',costo:'€ 61',price:'€ 159',stato:'Disponibile',siti:'eBay, Subito',gpu:'Intel Iris Xe',gg:4}
];""")
rep("['stageTel','Stage Cellulari'],['telecamere','Telecamere']]", "['stageTel','Stage Cellulari'],['ricambi','Ricambi'],['telecamere','Telecamere']]")
rep("  if(s==='telecamere'){ title='Telecamere'; hintTxt='la stessa sezione del gestionale Autotrasporti: il capannone è uno solo.'; body=telecamere(S.t); }",
    """  if(s==='telecamere'){ title='Telecamere'; hintTxt='la stessa sezione del gestionale Autotrasporti: il capannone è uno solo.'; body=telecamere(S.t); }
  if(s==='ricambi'){ title='Ricambi'; hintTxt='i pezzi smontati dai computer che non si vendono interi. Ogni ricambio resta legato al computer e al lotto da cui viene: quello che incassa conta nel recupero del lotto.';
    const tot=RICAMBI.filter(r=>r[5]==='Venduto').reduce((n,r)=>n+r[4],0);
    body=`<div class="grid g4"><div class="glass card"><div class="lbl">Ricambi a magazzino</div><div class="big">${RICAMBI.filter(r=>r[5]==='Disponibile').length}</div></div><div class="glass card"><div class="lbl">Venduti a ottobre</div><div class="big">€ ${tot}</div><div class="lbl">già nel recupero dei lotti</div></div><div class="glass card"><div class="lbl">Computer da smontare</div><div class="big">3</div><div class="lbl">non funzionanti, dischi già cancellati</div></div></div>
    <div class="glass tbox"><table class="t nw"><thead><tr><th>Ricambio</th><th>Da</th><th>Seriale del computer</th><th>Lotto</th><th>Prezzo</th><th>Stato</th></tr></thead><tbody>
    ${RICAMBI.map(r=>`<tr><td><b>${r[0]}</b></td><td>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td><td>€ ${r[4]}</td><td>${r[5]==='Venduto'?pill('Venduto','ok'):pill(r[5],'dark')}</td></tr>`).join('')}
    </tbody></table></div>
    <p class="lbl" style="margin:0">Prima di smontare, il disco passa dalla cancellazione certificata come tutto il resto: un disco non si vende mai senza rapporto.</p>`; }""")

# stile
rep(".seg{display:flex;", """.g4b{grid-template-columns:repeat(4,minmax(0,1fr))!important}
@media (max-width:520px){.g4b{grid-template-columns:repeat(2,minmax(0,1fr))!important}}
.schedat{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(240px,100%),1fr));gap:0 24px;margin-top:10px}
.schedat>div{display:flex;flex-direction:column;gap:2px;padding:10px 0;border-top:1px solid var(--line)}
.seg{display:flex;""")

open(P, 'w', encoding='utf8').write(s)
print('ok', len(s))
