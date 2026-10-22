# 21/10 notte: Non Consegnato sparisce dopo la firma; Traffico con giri già pronti, un solo «Conferma», pagina di ogni giro modificabile.
import sys
P = sys.argv[1]
s = open(P, encoding='utf8').read()

def rep(old, new, count=1):
    global s
    if old not in s:
        raise SystemExit('NON TROVATO: ' + old[:100])
    s = s.replace(old, new, count)

# ===== Non Consegnato: dopo la firma confermata non c'è più =====
rep("""      <button class="bigbtn ghost" data-act="aMancata">Non Consegnato</button>
    </div>`;""", """      ${d3?'':`<button class="bigbtn ghost" data-act="aMancata">Non Consegnato</button>`}
    </div>`;""")
rep("""      <button class="bigbtn ghost" data-act="aMancata" ${f===2?'':'disabled style="opacity:.35;cursor:not-allowed"'}>Non Consegnato</button>""",
    """      ${a.firmata?'':`<button class="bigbtn ghost" data-act="aMancata" ${f===2?'':'disabled style="opacity:.35;cursor:not-allowed"'}>Non Consegnato</button>`}""")
rep("  aMancata:()=>{if(S.a.scr==='firma'&&S.a.foto[S.a.cur]!==2)return;", "  aMancata:()=>{if(S.a.firmata)return; if(S.a.scr==='firma'&&S.a.foto[S.a.cur]!==2)return;")
rep("Su un’altra fermata premi subito «Non Consegnato» in fondo alla prima pagina, senza scansionare niente,",
    "Dopo la firma «Non Consegnato» sparisce: se il cliente ha firmato, la merce l’ha presa. Su un’altra fermata premi subito «Non Consegnato» in fondo alla prima pagina, senza scansionare niente,")

# ===== Traffico =====
rep("S.t.giriConf=false; S.t.giacData={};", """S.t.giriConf=false; S.t.giacData={}; S.t.giroSel=null; S.t.giroEdit=null; S.t.giroAdd=false; S.t.giriNuove=0;
S.t.giri=[
 {mezzo:'Sprinter [targa]',aut:'Autista 1',zona:'Zona Ovest',partito:false,f:[
   {cli:'Apple',ind:'Via [indirizzo], Rho',fascia:'9–12',colli:'6 colli',acc:['Firma obbligatoria']},
   {cli:'Apple',ind:'Via [indirizzo], Pero',fascia:'9–12',colli:'4 colli',acc:[]},
   {cli:'[Cliente]',ind:'Via [indirizzo], Arese',fascia:'14–17',colli:'1 bancale',acc:['Sponda']},
   {cli:'Apple',ind:'Via [indirizzo], Garbagnate',fascia:'14–18',colli:'8 colli',acc:[]}]},
 {mezzo:'Motrice con sponda [targa]',aut:'Autista 2',zona:'Milano',partito:true,f:[
   {cli:'Snam',ind:'Via [indirizzo], Milano',fascia:'entro le 12',colli:'4 bancali',acc:['Sponda']},
   {cli:'Luxiona',ind:'Via [indirizzo], Assago',fascia:'9–13',colli:'3 bancali',acc:['Piano terra']},
   {cli:'[Cliente]',ind:'Via [indirizzo], Milano',fascia:'sabato 9–12',colli:'2 colli',acc:['Sabato']}]},
 {mezzo:'Bilico [targa]',aut:'Autista 3',zona:'Lombardia Est',partito:false,f:[
   {cli:'Apple',ind:'Via [indirizzo], Bergamo',fascia:'8–12',colli:'18 bancali',acc:['Sponda']},
   {cli:'Apple',ind:'Via [indirizzo], Brescia',fascia:'13–17',colli:'12 bancali',acc:['Sponda']}]}
];
S.t.daAss=[{cli:'Snam',ind:'Via [indirizzo], Milano',fascia:'giovedì 10:00',colli:'1 bancale',acc:['Riconsegna da giacenza']},{cli:'[Cliente]',ind:'Via [indirizzo], Lodi',fascia:'14–17',colli:'2 colli',acc:[]}];""")

azioni = r"""  tGiriConf:()=>{S.t.giriConf=true; S.t.giriNuove=0; const d=S.t.giri.filter(g=>g.partito).length; evt('Traffico','Giri confermati: ogni autista li trova nella sua app, in ordine, con il navigatore per camion.');},
  tGiroSim:()=>{const n={cli:'[Cliente]',ind:'Via [indirizzo], Corsico',fascia:'entro le 16',colli:'2 colli',acc:['Fascia oraria']}; S.t.giri[1].f.push(n); S.t.giriConf=false; S.t.giriNuove=1; evt('Traffico','Arrivata una spedizione nuova: il programma l’ha messa nel giro di Autista 2. Serve la conferma.');},
  tGiro:i=>{S.t.giroSel=(i===''?null:+i); S.t.giroEdit=null; S.t.giroAdd=false; window.scrollTo(0,0);},
  tFerSu:j=>{const g=S.t.giri[S.t.giroSel], k=+j; if(k<1)return; [g.f[k-1],g.f[k]]=[g.f[k],g.f[k-1]]; giroCambiato(g,`${g.f[k-1].cli} anticipata alla fermata ${k}`);},
  tFerGiu:j=>{const g=S.t.giri[S.t.giroSel], k=+j; if(k>=g.f.length-1)return; [g.f[k+1],g.f[k]]=[g.f[k],g.f[k+1]]; giroCambiato(g,`${g.f[k+1].cli} spostata alla fermata ${k+2}`);},
  tFerTogli:j=>{const g=S.t.giri[S.t.giroSel], x=g.f.splice(+j,1)[0]; S.t.daAss.push(x); giroCambiato(g,`${x.cli} tolta dal giro: torna in «Da assegnare»`);},
  tFerSposta:j=>{const el=document.getElementById('sposta-'+j); if(!el||el.value==='')return; const g=S.t.giri[S.t.giroSel], dst=S.t.giri[+el.value], x=g.f.splice(+j,1)[0]; dst.f.push(x); giroCambiato(g,`${x.cli} passata al giro di ${dst.aut}`); giroCambiato(dst,`${x.cli} aggiunta in fondo al giro`,true);},
  tFerEdit:j=>{S.t.giroEdit=(S.t.giroEdit===+j?null:+j);},
  tFerSalva:j=>{const g=S.t.giri[S.t.giroSel], x=g.f[+j], fa=document.getElementById('fascia-'+j); if(fa&&fa.value.trim())x.fascia=fa.value.trim(); x.acc=[...document.querySelectorAll('input[data-acc="'+j+'"]:checked')].map(e=>e.value); S.t.giroEdit=null; giroCambiato(g,`${x.cli}: fascia ${x.fascia}${x.acc.length?', '+x.acc.join(', '):''}`);},
  tGiroAddT:()=>{S.t.giroAdd=!S.t.giroAdd;},
  tGiroAdd:j=>{const g=S.t.giri[S.t.giroSel], x=S.t.daAss.splice(+j,1)[0]; g.f.push(x); S.t.giroAdd=false; giroCambiato(g,`${x.cli} aggiunta al giro`);},"""
rep("  tGiri:()=>{S.t.giriOk=true; S.t.giriConf=false;},\n  tGiriConf:()=>{if(S.t.giriOk)S.t.giriConf=true;},", azioni)

helper = r"""
/* traffico: ogni modifica a un giro va nello Storico; se il giro è confermato e l'autista è partito, gli arriva l'avviso */
function giroCambiato(g,cosa,silenzioso){
  S.t.log.unshift([ora(),'Mauro','Giro',cosa,g.mezzo+' · '+g.aut,'Manuale']);
  if(S.t.giriConf&&g.partito) evt('Autista',`${g.aut} riceve l’avviso nell’app: «Il tuo giro è cambiato». ${cosa}.`);
  else if(!silenzioso) evt('Traffico',`Giro di ${g.aut}: ${cosa}.`);
}
const giroOre=g=>{let m=7*60+30; return g.f.map((x,i)=>{m+=i?28:25; return String(Math.floor(m/60)).padStart(2,'0')+':'+String(m%60).padStart(2,'0');});};
const giroKm=g=>({ 'Zona Ovest':22,'Milano':18,'Lombardia Est':105 }[g.zona]||20)*g.f.length;
function mappaGiro(g){
  const P=[[60,170],[110,120],[170,95],[230,70],[280,110],[300,170],[240,200],[180,215]];
  const pts=g.f.map((x,i)=>P[(i+1)%P.length]);
  return `<svg viewBox="0 0 340 240" style="width:100%;display:block" role="img" aria-label="Mappa del giro di ${g.aut}"><rect width="340" height="240" rx="16" fill="rgba(17,18,20,.03)"/>
    <path d="M0 120 Q170 100 340 140" stroke="rgba(17,18,20,.07)" stroke-width="10" fill="none"/><path d="M150 0 Q160 140 140 240" stroke="rgba(17,18,20,.07)" stroke-width="8" fill="none"/>
    <path d="M40 200 ${pts.map(p=>'L'+p[0]+' '+p[1]).join(' ')}" stroke="#111214" stroke-width="3" fill="none" stroke-linejoin="round"/>
    <rect x="26" y="188" width="28" height="24" rx="6" fill="#111214"/>
    ${pts.map((p,i)=>`<circle cx="${p[0]}" cy="${p[1]}" r="11" fill="#fff" stroke="#111214" stroke-width="2"/><text x="${p[0]}" y="${p[1]+4}" text-anchor="middle" font-size="11" font-weight="800" fill="#111214">${i+1}</text>`).join('')}</svg>`;
}
function giroPagina(t){
  const g=t.giri[t.giroSel], ore=giroOre(g), altri=t.giri.map((x,i)=>[x,i]).filter(([x,i])=>i!==t.giroSel);
  const ACC=['Sponda','Piano terra','Consegna al piano','Fascia oraria','Sabato','Firma obbligatoria','Chiamare prima'];
  return `<div class="row">${b('← Tutti i giri','tGiro','','ghost sm')}</div>
    <div class="glass card row between" style="gap:12px"><div><b style="font-size:22px">${g.aut} · ${g.mezzo}</b><div class="lbl">${g.zona} · ${g.f.length} fermate · ${giroKm(g)} km · partenza 07:30</div></div>${g.partito?pill('Partito','dark'):pill('In magazzino')}</div>
    ${t.giriConf&&g.partito?msg('Questo giro è confermato e l’autista è già partito: ogni modifica gli arriva subito nell’app con un avviso.'):''}
    <div class="row" style="align-items:flex-start;gap:16px">
      <div class="glass card stack" style="flex:2 1 520px;min-width:0;gap:0">
        ${g.f.map((x,j)=>`<div class="ferm">
          <span class="fn">${j+1}</span>
          <div style="flex:1;min-width:0"><div class="row between" style="gap:8px"><b style="font-size:17px">${x.cli}</b><span class="lbl">arrivo ${ore[j]}</span></div>
            <div class="lbl">${x.ind} · ${x.fascia} · ${x.colli}</div>
            ${x.acc.length?`<div class="row" style="gap:6px;margin-top:6px">${x.acc.map(a=>pill(a)).join('')}</div>`:''}
            ${t.giroEdit===j?`<div class="stack" style="gap:8px;margin-top:10px;padding:12px;border-radius:14px;background:var(--soft)">
              <label class="stack" style="gap:4px"><span class="lbl">Fascia oraria</span><input id="fascia-${j}" value="${x.fascia}" style="font:inherit;padding:8px 10px;border-radius:10px;border:1px solid var(--line)"></label>
              <div class="row" style="gap:6px">${ACC.map(a=>`<label class="chipbtn" style="cursor:pointer"><input type="checkbox" data-acc="${j}" value="${a}" ${x.acc.indexOf(a)>=0?'checked':''} style="margin-right:6px">${a}</label>`).join('')}</div>
              <div class="row">${b('Salva','tFerSalva',j,'sm')}${b('Annulla','tFerEdit',j,'ghost sm')}</div></div>`:''}
            <div class="row" style="gap:6px;margin-top:10px">
              ${b('Su','tFerSu',j,'ghost sm')}${b('Giù','tFerGiu',j,'ghost sm')}${b('Modifica','tFerEdit',j,'ghost sm')}
              <select id="sposta-${j}" aria-label="Passa a un altro mezzo" style="font:inherit;font-size:14px;padding:6px 8px;border-radius:999px;border:1px solid var(--line);background:#fff"><option value="">Passa a…</option>${altri.map(([x2,i])=>`<option value="${i}">${x2.aut}</option>`).join('')}</select>${b('Sposta','tFerSposta',j,'ghost sm')}
              ${b('Togli','tFerTogli',j,'ghost sm')}
            </div></div></div>`).join('')}
        <div style="padding-top:12px">${b('+ Aggiungi fermata','tGiroAddT','','ghost sm')}</div>
        ${t.giroAdd?`<div class="list" style="margin-top:8px">${t.daAss.length?t.daAss.map((x,j)=>`<button class="li" data-act="tGiroAdd" data-arg="${j}"><span class="row between" style="width:100%"><b>${x.cli}</b><span class="lbl">${x.fascia}</span></span><span class="lbl">${x.ind} · ${x.colli}</span></button>`).join(''):'<div class="lbl" style="padding:10px">Nessuna spedizione da assegnare.</div>'}</div>`:''}
      </div>
      <div class="glass card stack" style="flex:1 1 320px;min-width:0"><b>Il giro di ${g.aut}</b>${mappaGiro(g)}<div class="lbl">Percorso per camion, nell’ordine delle fermate. Ogni modifica finisce nello Storico con chi l’ha fatta e quando.</div></div>
    </div>`;
}
"""
rep("/* satellitare: percorso del giorno confrontato con il giro */", helper + "\n/* satellitare: percorso del giorno confrontato con il giro */")

a = s.index("  if(s==='traffico'){")
z = s.index("  if(s==='magazzino'){", a)
s = s[:a] + r"""  if(s==='traffico'){
    title='Traffico';
    if(t.giroSel!==null){ hintTxt='qui Mauro e Nelson cambiano il giro all’ultimo momento: Su e Giù per l’ordine, Modifica per fascia e accessori, Passa a… per darla a un altro mezzo, Togli, oppure «+ Aggiungi fermata».'; body=giroPagina(t); }
    else {
    hintTxt='i giri di domani sono già pronti: il programma li prepara da solo. Tocca un giro per aprirlo grande e modificarlo; quando va bene, «Conferma». Se poi arriva una spedizione nuova, la richiesta di conferma ricompare.';
    const tot=t.giri.reduce((n,g)=>n+g.f.length,0);
    body=`<div class="glass card row between"><span><b>Domani</b> <span class="lbl">${tot} fermate in questi giri · ${t.giri.length} mezzi negli esempi</span></span><div class="row">${t.giriConf?pill('Confermati','ok'):b('Conferma','tGiriConf')}${t.giriConf?b('Simula: arriva una spedizione','tGiroSim','','ghost sm'):''}</div></div>
    ${!t.giriConf&&!t.giriNuove?msg('Il programma ha preparato i giri di domani: ha diviso le spedizioni tra i mezzi guardando portata, sponda e fasce orarie dei clienti, e ha messo le fermate di ogni mezzo nell’ordine più corto per un camion (356 km invece di 412). Controllate, aprite un giro se volete cambiarlo, poi premete «Conferma».'):''}
    ${!t.giriConf&&t.giriNuove?msg('È arrivata una spedizione nuova e il programma l’ha messa nel giro di Autista 2. Controllate e premete «Conferma».'):''}
    <div class="grid g4">
      ${t.giri.map((g,i)=>`<button class="glass card giro" data-act="tGiro" data-arg="${i}"><span class="row between" style="width:100%"><b>${g.mezzo} · ${g.aut}</b>${pill(g.zona)}</span><ol style="margin:12px 0 0;padding-left:20px;line-height:1.9;text-align:left">${g.f.map(x=>`<li>${x.cli} · ${x.ind.split(', ').pop()}</li>`).join('')}</ol><span class="lbl" style="margin-top:8px">${giroKm(g)} km · ${g.f.length} fermate</span><span class="go" style="margin-top:6px">Apri</span></button>`).join('')}
      <div class="glass card" style="border-style:dashed"><b>Da assegnare</b>${t.daAss.length?`<ul style="margin:12px 0 0;padding-left:20px;line-height:1.9">${t.daAss.map(x=>`<li>${x.cli} · ${x.fascia}</li>`).join('')}</ul><p class="lbl" style="margin:8px 0 0">Aprite un giro e premete «+ Aggiungi fermata».</p>`:'<p class="lbl" style="margin:10px 0 0">Tutto assegnato.</p>'}</div>
    </div>${mappaGiri(true)}`;
    }
  }
""" + s[z:]
rep("  tGo:s=>{S.view='trasp'; S.t.sec=s;", "  tGo:s=>{S.view='trasp'; S.t.sec=s; S.t.giroSel=null;")

rep(".seg{display:flex;", """.giro{display:flex;flex-direction:column;align-items:stretch;text-align:left;cursor:pointer;font:inherit;color:inherit}
.giro:hover{background:rgba(255,255,255,.9)}
.ferm{display:flex;gap:12px;padding:14px 0;border-top:1px solid var(--line)}
.ferm:first-child{border-top:0;padding-top:0}
.fn{width:30px;height:30px;border-radius:99px;background:var(--solid);color:var(--on-solid);display:flex;align-items:center;justify-content:center;font-weight:800;flex:none}
.seg{display:flex;""")

rep("hook('tGiri',()=>evt('Traffico','Giri di domani: 38 spedizioni su 11 mezzi, 356 km invece di 412. Un mezzo resta libero.'));", '')
open(P, 'w', encoding='utf8').write(s)
print('ok', len(s))
