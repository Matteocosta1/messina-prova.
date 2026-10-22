# Modifiche del 20/10 sera (recap vocale + "procedi"):
# app autisti a conferme e firma vera, badge Entrata/Uscita, magazzino Bancale/Collo, Traffico spiegato,
# giacenze con giorno e ora, mezzi con autista fisso, Satellitare e Telecamere.
import sys
P = sys.argv[1]
s = open(P, encoding='utf8').read()

def rep(old, new, count=1):
    global s
    if old not in s:
        raise SystemExit('NON TROVATO: ' + old[:100])
    s = s.replace(old, new, count)

# ================= STATO =================
rep("a:{scr:'lista', cur:0, done:{}, why:{}, foto:{}, fotoInfo:{}, soglia:35, analisi:false, scanned:false, acc:{}, accOpen:false, nav:false, accOk:{}, firmata:false},",
    "a:{scr:'lista', cur:0, done:{}, why:{}, foto:{}, fotoInfo:{}, soglia:35, analisi:false, scanned:false, acc:{}, accOpen:false, nav:false, accOk:{}, firmata:false, colliOk:false, accConf:false, firmaOpen:false, firmaImg:null},")
rep("S.n.ord=null;", "S.n.ord=null;\nS.t.giriConf=false; S.t.giacData={}; S.t.giacForm=false; S.t.giacChiesto={}; S.t.giacReso={}; S.t.giacResoOpen=false; S.t.satSel=0; S.t.camSel=null;\nS.m.inTipo='Bancale'; S.m.mvTipo='Bancale';\nS.mezAut={};")

# ================= APP AUTISTI =================
rep("  aOpen:i=>{S.a.cur=+i; S.a.scr='dett'; S.a.scanned=false; S.a.accOpen=false; S.a.nav=false; S.a.accOk={}; S.a.firmata=false; window.scrollTo(0,0);},",
    "  aOpen:i=>{S.a.cur=+i; S.a.scr='dett'; S.a.scanned=false; S.a.accOpen=false; S.a.nav=false; S.a.accOk={}; S.a.firmata=false; S.a.colliOk=false; S.a.accConf=false; S.a.firmaOpen=false; S.a.firmaImg=null; window.scrollTo(0,0);},\n"
    "  aColliOk:()=>{if(S.a.scanned)S.a.colliOk=true;},\n"
    "  aAccConf:()=>{if(S.a.colliOk){S.a.accConf=true; S.a.accOpen=false;}},\n"
    "  aFirmaApri:()=>{S.a.firmaOpen=true; S.a.firmaImg=null;},\n"
    "  aFirmaCanc:()=>{S.a.firmaImg=null;},\n"
    "  aFirmaOk:()=>{if(S.a.firmaImg){S.a.firmata=true; S.a.firmaOpen=false;}},\n"
    "  aAvanti:()=>{if(S.a.colliOk){S.a.scr='firma'; window.scrollTo(0,0);}},")
rep("  aFirma:()=>{if(!S.a.pronto)return; S.a.scr='firma';},", "  aFirma:()=>{if(!S.a.colliOk)return; S.a.scr='firma';},")
rep("  aMancata:()=>{if(!S.a.scanned&&S.a.scr==='dett')return; S.a.scr='mancata';},",
    "  aMancata:()=>{if(S.a.scr==='firma'&&S.a.foto[S.a.cur]!==2)return; S.a.scr='mancata';},")
rep("  aOk:()=>{ if(S.a.foto[S.a.cur]!==2) return; S.a.done[S.a.cur]='ok'; S.a.scr='lista';},",
    "  aOk:()=>{ if(S.a.foto[S.a.cur]!==2||!S.a.pronto) return; S.a.done[S.a.cur]='ok'; S.a.scr='lista';},")
rep("acc:{},accOpen:false,nav:false,accOk:{},firmata:false};},", "acc:{},accOpen:false,nav:false,accOk:{},firmata:false,colliOk:false,accConf:false,firmaOpen:false,firmaImg:null};},")

a0 = s.index("    const d1=a.scanned, d2=d1&&accs.every(x=>a.accOk[x]), d3=d2&&a.firmata; a.pronto=d3;")
a1 = s.index("  if(a.scr==='firma'){")
nuovo_dett = r"""    const d1=a.colliOk, d2=d1&&a.accConf, d3=d2&&a.firmata; a.pronto=d3;
    const cam=KI.cam.replace(/width="22" height="22"/,'width="30" height="30"');
    const pin=`<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-7-6.1-7-11.5a7 7 0 0114 0C19 14.9 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>`;
    const blk=(n,t,done,on,body)=>`<div class="pcard stack" style="padding:14px;gap:10px;${done?'border:2px solid var(--ok);background:var(--ok-soft);':(on?'border:2px solid var(--solid);':'opacity:.4;pointer-events:none;')}">
      <div class="row" style="gap:10px;flex-wrap:nowrap"><span style="width:30px;height:30px;border-radius:99px;display:flex;align-items:center;justify-content:center;font-weight:800;flex:none;${done?'background:var(--ok);color:#fff':'border:2px solid currentColor'}">${done?'✓':n}</span><b style="font-size:20px;${done?'color:var(--ok)':''}">${t}</b></div>${body}</div>`;
    const off='disabled style="opacity:.35;cursor:not-allowed"';
    const conf=(act,ok)=>`<button class="bigbtn" data-act="${act}" ${ok?'':off}>Conferma</button>`;
    const colli=d1?`<div style="font-size:17px">${s.colli} · tutti scansionati</div>`
      :(a.scanned?`<div style="font-size:17px">${s.colli} · tutti scansionati</div>${conf('aColliOk',true)}`
      :`<div style="font-size:17px">${s.colli} da scaricare. Scansiona ogni collo.</div><button class="bigbtn ghost" data-act="aScan" aria-label="Scansiona i colli" style="display:flex;align-items:center;justify-content:center">${cam}</button>${conf('aColliOk',false)}`);
    const righeAcc=accs.length?accs.map(x=>`<div class="pcard row between" style="padding:12px 14px;font-size:17px"><span>${x}</span>${extra.indexOf(x)>=0?'<span class="lbl">aggiunto</span>':'<span class="lbl">in bolla</span>'}</div>`).join(''):'<div class="lbl">Nessuno sulla bolla.</div>';
    const accesso=d2?righeAcc:righeAcc+`<button class="chipbtn" style="align-self:flex-start;border-style:dashed" data-act="aAccT">+ Aggiungi</button>${a.accOpen?`<div class="row" style="gap:6px">${all.map(x=>chip(x,'aAcc',x,false)).join('')}</div><div class="lbl">Va da solo in fattura.</div>`:''}`+conf('aAccConf',true);
    const firma=d3?`<img src="${a.firmaImg}" alt="Firma del cliente" style="width:100%;height:110px;object-fit:contain;background:#fff;border-radius:12px"><div style="font-size:17px">Firmata dal cliente</div>`
      :(a.firmaOpen?`<div style="font-size:15px">Fai firmare il cliente qui sotto, con il dito.</div><canvas id="firmaPad" width="600" height="300" style="width:100%;height:160px;background:#fff;border-radius:12px;border:2px dashed var(--muted);touch-action:none;cursor:crosshair"></canvas>
          <div class="row" style="gap:8px;flex-wrap:nowrap"><button class="bigbtn ghost" style="flex:1" data-act="aFirmaCanc">Cancella</button><button class="bigbtn" style="flex:1" data-act="aFirmaOk" ${a.firmaImg?'':off}>Conferma</button></div>`
      :`<div style="font-size:17px">Tocca e fai firmare il cliente.</div><button class="bigbtn" data-act="aFirmaApri" aria-label="Firma del cliente" style="display:flex;align-items:center;justify-content:center">${KI.pen.replace(/width="22" height="22"/,'width="30" height="30"')}</button>`);
    inner=`<div class="pscr">
      <button class="back" data-act="aBack">Consegne</button>
      <div><div class="lbl">Fermata ${a.cur+1} · ${s.fascia}</div><div class="ptitle">${s.cliente}</div>
        <div class="row between" style="flex-wrap:nowrap;gap:10px;margin-top:4px"><span style="font-size:16px">${s.ind}</span><button class="round" data-act="aNav" aria-label="Navigatore per camion" style="flex:none;display:flex;align-items:center;justify-content:center">${pin}</button></div>
        ${a.nav?`<div class="lbl">Si apre il navigatore per camion verso ${s.ind}.</div>`:''}
        ${nota?`<div style="margin-top:6px">${pill(nota,'dark')}</div>`:''}</div>
      ${blk(1,'Colli',d1,true,colli)}
      ${blk(2,'Accessori',d2,d1,accesso)}
      ${blk(3,'Firma',d3,d2,firma)}
      <div style="flex:1"></div>
      <button class="bigbtn" data-act="aAvanti" ${d1?'':off}>Avanti</button>
    </div>`;
  }
"""
s = s[:a0] + nuovo_dett + s[a1:]

# pagina 2: prima la bolla, poi Consegnato / Non consegnato
rep("""      <div class="lbl">Se la foto è sfocata o buia diventa rossa: rifalla. Poi premi Conferma.</div>
      <div style="flex:1"></div>
      <button class="bigbtn" data-act="aOk" ${f===2?'':'disabled style="opacity:.35;cursor:not-allowed"'}>Conferma</button>""",
"""      <div class="lbl">Se la foto è sfocata o buia diventa rossa: rifalla.</div>
      ${f===2&&!a.pronto?`<div class="lbl" style="color:var(--alert);font-weight:600">Per «Consegnato» servono anche Accessori e Firma confermati.</div>`:''}
      <div style="flex:1"></div>
      <button class="bigbtn" data-act="aOk" ${f===2&&a.pronto?'':'disabled style="opacity:.35;cursor:not-allowed"'}>Consegnato</button>
      <button class="bigbtn ghost" data-act="aMancata" ${f===2?'':'disabled style="opacity:.35;cursor:not-allowed"'}>Non consegnato</button>""")
rep("""      <div class="row" style="gap:10px;flex-wrap:nowrap"><span style="width:30px;height:30px;border-radius:99px;display:flex;align-items:center;justify-content:center;font-weight:800;flex:none;${f===2?'background:var(--ok);color:#fff':'border:2px solid currentColor'}">${f===2?'✓':'4'}</span><div class="ptitle">Bolla</div></div>
      <div style="font-size:18px">Fai la foto alla bolla firmata.</div>""",
"""      <div class="row" style="gap:10px;flex-wrap:nowrap"><span style="width:30px;height:30px;border-radius:99px;display:flex;align-items:center;justify-content:center;font-weight:800;flex:none;${f===2?'background:var(--ok);color:#fff':'border:2px solid currentColor'}">${f===2?'✓':'4'}</span><div class="ptitle">Bolla</div></div>
      <div style="font-size:18px">Fai la foto alla bolla.</div>""")
# "Non consegnato": indietro torna alla pagina Bolla
rep("""  if(a.scr==='mancata'){
    inner=`<div class="pscr">
      <button class="back" data-act="aDett">Indietro</button>""", """  if(a.scr==='mancata'){
    inner=`<div class="pscr">
      <button class="back" data-act="aFirma">Indietro</button>""")
rep("""<ol><li>Tocca la prima fermata, Snam. La pagina si legge dall’alto: 1 Colli, 2 Accessori, 3 Firma. Ogni blocco si accende quando hai finito quello sopra.</li><li>Premi il tasto con la fotocamera per scansionare i colli, spunta la sponda, poi il tasto con la penna quando il cliente ha firmato. Prova anche «+ Aggiungi».</li><li>Premi «Consegnato»: nella pagina Bolla premi la fotocamera e si apre quella vera. Fai una foto mossa e poi una ferma: la prima viene rifiutata, la seconda accettata.</li><li>Su un’altra fermata prova «Non consegnato» e poi «Torna in magazzino: giacenza».</li><li>Nel gestionale apri Autotrasporti › Giacenze: la trovi lì.</li></ol>""",
"""<ol><li>Tocca la prima fermata, Snam. Prima pagina: 1 Colli, 2 Accessori, 3 Firma. Ogni blocco ha il suo «Conferma» e si accende quando hai confermato quello sopra.</li><li>Colli: tasto fotocamera per scansionarli, poi «Conferma». Accessori: vedi quelli della bolla, con «+ Aggiungi» metti quelli chiesti all’ultimo, poi «Conferma». Firma: tocca la penna e fai firmare il cliente con il dito, poi «Conferma».</li><li>«Avanti»: seconda pagina, la Bolla. Prima la foto (si apre la fotocamera vera: una foto mossa viene rifiutata), poi «Consegnato» o «Non consegnato».</li><li>Su un’altra fermata prova «Non consegnato» e poi «Torna in magazzino: giacenza».</li><li>Nel gestionale apri Autotrasporti › Giacenze: la trovi lì.</li></ol>""")

# firma con il dito: disegno sul canvas, salvato nello stato a ogni tratto
rep("document.addEventListener('change',e=>{", r"""(function(){
  let disegna=false, ultimo=null;
  const pos=(c,e)=>{const r=c.getBoundingClientRect(); return [(e.clientX-r.left)*c.width/r.width,(e.clientY-r.top)*c.height/r.height];};
  document.addEventListener('pointerdown',e=>{const c=e.target; if(c.id!=='firmaPad')return; disegna=true; ultimo=pos(c,e); c.setPointerCapture(e.pointerId); e.preventDefault();});
  document.addEventListener('pointermove',e=>{const c=e.target; if(!disegna||c.id!=='firmaPad')return; const p=pos(c,e), x=c.getContext('2d'); x.lineWidth=5; x.lineCap='round'; x.strokeStyle='#111214'; x.beginPath(); x.moveTo(ultimo[0],ultimo[1]); x.lineTo(p[0],p[1]); x.stroke(); ultimo=p;});
  document.addEventListener('pointerup',e=>{const c=e.target; if(!disegna)return; disegna=false; if(c.id==='firmaPad'){S.a.firmaImg=c.toDataURL('image/png'); const k=document.querySelector('[data-act="aFirmaOk"]'); if(k){k.disabled=false; k.removeAttribute('style'); k.style.flex='1';}}});
})();
document.addEventListener('change',e=>{
  if(e.target.dataset&&e.target.dataset.mez!==undefined){S.mezAut[e.target.dataset.mez]=e.target.value; evt('Mezzi',`${e.target.value==='—'?'Mezzo senza autista fisso':e.target.value+' è l’autista fisso di questo mezzo'}: giri, Telepass e satellitare si collegano a lui.`); render(); return;}""")
# dopo ogni render, ridisegna la firma già fatta
rep("  if(window.innerWidth<=760){ const on=document.querySelector('.side .nav.on');",
    "  const pad=document.getElementById('firmaPad'); if(pad&&S.a.firmaImg){const im=new Image(); im.onload=()=>pad.getContext('2d').drawImage(im,0,0); im.src=S.a.firmaImg;}\n  if(window.innerWidth<=760){ const on=document.querySelector('.side .nav.on');")

# ================= BADGE =================
rep("  bTimbra:()=>{const now=new Date(); const hh=String(now.getHours()).padStart(2,'0')+':'+String(now.getMinutes()).padStart(2,'0'); S.b.timb.unshift([S.b.timb.length%2===0?'Entrata':'Uscita',hh]);},",
    "  bTimbra:v=>{const dentro=S.b.timb.length&&S.b.timb[0][0]==='Entrata'; if((v==='Entrata')===!!dentro)return; const now=new Date(); const hh=String(now.getHours()).padStart(2,'0')+':'+String(now.getMinutes()).padStart(2,'0'); S.b.timb.unshift([v,hh]);},")
rep("  const dentro=t.length%2===1;", "  const dentro=t.length>0&&t[0][0]==='Entrata';")
rep("""    <button class="bigbtn" data-act="bTimbra">${dentro?'Simula: timbro l’uscita':'Simula: timbro l’entrata'}</button>""",
    """    <div class="row" style="gap:10px;flex-wrap:nowrap"><button class="bigbtn" style="flex:1" data-act="bTimbra" data-arg="Entrata" ${dentro?'disabled style="flex:1;opacity:.35;cursor:not-allowed"':''}>Entrata</button><button class="bigbtn" style="flex:1" data-act="bTimbra" data-arg="Uscita" ${dentro?'':'disabled style="flex:1;opacity:.35;cursor:not-allowed"'}>Uscita</button></div>""")
rep("<li>Premi «Simula: timbro l’entrata», poi l’uscita.</li>", "<li>Premi «Entrata», poi «Uscita». Si possono ripetere più volte nello stesso giorno.</li>")

# ================= MAGAZZINO: Bancale o Collo =================
rep("  mInScan:()=>{ if(S.m.inStep===0){S.m.inStep=1;} else {S.m.inStep=0; S.m.inN=Math.min(4,S.m.inN+1);} },",
    "  mInScan:()=>{ if(S.m.inStep===0){S.m.inStep=1;} else {S.m.inStep=0; S.m.inN=Math.min(4,S.m.inN+1);} },\n  mInTipo:v=>{S.m.inTipo=v; S.m.inStep=0;},\n  mMvTipo:v=>{S.m.mvTipo=v; S.m.mvStep=0;},")
rep("""      :`<div class="scanbox"><b style="font-size:18px">${m.inStep===0?'1. Scansiona il bancale':'2. Scansiona il posto'}</b><span class="lbl">${m.inStep===0?'Etichetta del bancale o del collo':'Posto proposto: <b>S04-2-'+(m.inN%3+1)+'</b>, in basso vicino alla baia'}</span></div>
      <button class="bigbtn" data-act="mInScan">${m.inStep===0?'Scansiona bancale':'Scansiona posto'}</button>`}""",
"""      :`<div class="seg">${['Bancale','Collo'].map(x=>`<button class="${m.inTipo===x?'on':''}" data-act="mInTipo" data-arg="${x}">${x}</button>`).join('')}</div>
      ${m.inTipo==='Bancale'?`<div class="scanbox"><b style="font-size:18px">${m.inStep===0?'1. Scansiona il bancale':'2. Scansiona il posto'}</b><span class="lbl">${m.inStep===0?'Etichetta del bancale':'Posto proposto: <b>S04-2-'+(m.inN%3+1)+'</b>, in basso vicino alla baia'}</span></div>
      <button class="bigbtn" data-act="mInScan">${m.inStep===0?'Scansiona bancale':'Scansiona posto'}</button>`
      :`<div class="scanbox"><b style="font-size:18px">${m.inStep===0?'1. Scansiona il collo':'2. Scansiona il bancale'}</b><span class="lbl">${m.inStep===0?'Etichetta della scatola':'Il bancale dove appoggi la scatola: <b>B-01'+(60+m.inN)+'</b>'}</span></div>
      <button class="bigbtn" data-act="mInScan">${m.inStep===0?'Scansiona collo':'Scansiona bancale'}</button>`}`}""")
rep("""<div class="lbl">${m.inN} di 4 bancali messi a posto</div>""", """<div class="lbl">${m.inN} di 4 messi a posto</div>""")
rep("""      :`<div class="scanbox"><b style="font-size:18px">${m.mvStep===0?'1. Scansiona cosa trasferisci':'2. Scansiona il posto nuovo'}</b><span class="lbl">${m.mvStep===0?'Collo o bancale':'Bancale Luxiona, adesso in S05-1-2'}</span></div><button class="bigbtn" data-act="mMv">${m.mvStep===0?'Scansiona collo':'Scansiona posto'}</button>`}""",
"""      :`<div class="seg">${['Bancale','Collo'].map(x=>`<button class="${m.mvTipo===x?'on':''}" data-act="mMvTipo" data-arg="${x}">${x}</button>`).join('')}</div>
      <div class="scanbox"><b style="font-size:18px">${m.mvStep===0?'1. Scansiona il '+m.mvTipo.toLowerCase():(m.mvTipo==='Bancale'?'2. Scansiona il posto nuovo':'2. Scansiona il bancale o il posto nuovo')}</b><span class="lbl">${m.mvStep===0?(m.mvTipo==='Bancale'?'Etichetta del bancale':'Etichetta della scatola'):(m.mvTipo==='Bancale'?'Bancale Luxiona, adesso in S05-1-2':'Scatola Luxiona, adesso sul bancale B-0133')}</span></div><button class="bigbtn" data-act="mMv">${m.mvStep===0?'Scansiona '+m.mvTipo.toLowerCase():(m.mvTipo==='Bancale'?'Scansiona posto':'Scansiona bancale o posto')}</button>`}""")
rep("""<b style="color:var(--ok)">Trasferito</b><div style="font-size:14px;margin-top:4px">Bancale Luxiona da S05-1-2 a S06-3-1.</div>""",
    """<b style="color:var(--ok)">Trasferito</b><div style="font-size:14px;margin-top:4px">${m.mvTipo==='Bancale'?'Bancale Luxiona da S05-1-2 a S06-3-1.':'Scatola Luxiona dal bancale B-0133 al bancale B-0141.'}</div>""")
rep("<li>«Entrata»: scansiona il bancale, poi il posto proposto. Quattro volte.</li>",
    "<li>«Entrata»: scegli «Bancale» (bancale, poi posto) o «Collo» (scatola, poi il bancale dove la appoggi). Quattro volte.</li>")
rep("${big('Trasferisci','mGo','sposta','Cambio posto a un collo o a un bancale')}", "${big('Trasferisci','mGo','sposta','Cambio posto a un bancale o a un collo')}")
rep("hook('mInScan',(x,p)=>{const prima=JSON.parse(p)[2]; if(S.m.inN>prima){evt('Portale',`Snam vede il bancale ${S.m.inN} di 4 in S04-2-${(prima%3)+1}, con 18 seriali, in tempo reale.`);}});",
    "hook('mInScan',(x,p)=>{const prima=JSON.parse(p)[2]; if(S.m.inN>prima){evt('Portale',S.m.inTipo==='Bancale'?`Snam vede il bancale ${S.m.inN} di 4 in S04-2-${(prima%3)+1}, con 18 seriali, in tempo reale.`:`Snam vede la scatola ${S.m.inN} di 4 sul bancale B-01${59+S.m.inN}, in tempo reale.`); evt('Telecamere','Foto della scansione salvata insieme al movimento: Magazziniere 1, baia 2.');}});")

# ================= TRAFFICO =================
rep("  tGiri:()=>{S.t.giriOk=true;},", "  tGiri:()=>{S.t.giriOk=true; S.t.giriConf=false;},\n  tGiriConf:()=>{if(S.t.giriOk)S.t.giriConf=true;},")
rep("""    title='Traffico'; hintTxt='premi «Proponi i giri»: il programma assegna da solo le spedizioni ancora aperte.';""",
    """    title='Traffico'; hintTxt='«Proponi i giri» fa il lavoro che oggi Mauro e Nelson fanno a mano: divide tra i mezzi le spedizioni di domani e mette in ordine le fermate. Loro controllano, spostano se serve e premono «Conferma i giri».';""")
rep("""<div class="row">${b(t.giriOk?'Giri proposti':'Proponi i giri','tGiri')}</div></div>
    ${t.giriOk?msg('Giri proposti: 38 spedizioni assegnate, 4 spostate sui mezzi liberi. Mauro e Nelson possono cambiare le fermate trascinandole.'):''}""",
"""<div class="row">${t.giriConf?pill('Giri confermati','ok'):(t.giriOk?b('Conferma i giri','tGiriConf'):b('Proponi i giri','tGiri'))}${t.giriOk&&!t.giriConf?b('Rifai','tGiri','','ghost'):''}</div></div>
    ${t.giriOk&&!t.giriConf?msg('Cosa ha fatto il programma: ha preso le 42 spedizioni di domani e le ha divise tra 11 mezzi, guardando portata, sponda e fasce orarie dei clienti. Le 4 che erano «da assegnare» ora sono dentro un giro. Poi ha messo le fermate di ogni mezzo nell’ordine più corto per un camion: 356 km totali invece di 412. Adesso controllate: se volete cambiare, trascinate una fermata da un giro all’altro. Quando va bene, premete «Conferma i giri».'):''}
    ${t.giriConf?msg('Giri confermati: domattina ogni autista li trova già in ordine nella sua app, con il navigatore per camion.'):''}""")

# ================= GIACENZE =================
rep("  tGiacChiedi:()=>{S.t.giacMsg='chiesto';},", "  tGiacChiedi:()=>{if(S.t.giacChiesto[S.t.giac])return; S.t.giacChiesto[S.t.giac]=ora(); S.t.giacMsg='chiesto';},\n  tGiacForm:()=>{S.t.giacForm=!S.t.giacForm; S.t.giacResoOpen=false;},\n  tGiacReso:()=>{S.t.giacResoOpen=!S.t.giacResoOpen; S.t.giacForm=false;},\n  tGiacResoOk:()=>{S.t.giacReso[S.t.giac]=true; S.t.giacResoOpen=false; S.t.giacMsg='reso';},")
rep("  tGiacPren:()=>{S.t.giacPren[S.t.giac]=true; S.t.giacMsg='prenotata';},",
    "  tGiacPren:()=>{const g=document.getElementById('giacGiorno'), o=document.getElementById('giacOra'); if(!g||!g.value||!o||!o.value)return; S.t.giacPren[S.t.giac]=true; S.t.giacData[S.t.giac]=[g.value,o.value]; S.t.giacForm=false; S.t.giacMsg='prenotata';},")
rep("  tGiac:i=>{S.t.giac=+i; S.t.giacMsg='';},", "  tGiac:i=>{S.t.giac=+i; S.t.giacMsg=''; S.t.giacForm=false; S.t.giacResoOpen=false;},")
rep("""    title='Giacenze'; hintTxt='scegli una giacenza e premi «Chiedi al cliente quando riconsegnare» oppure «Prenota la riconsegna».';""",
    """    title='Giacenze'; hintTxt='tre strade per ogni giacenza. «Prenota la riconsegna»: scegli giorno e ora, ed è fatta. «Chiedi al cliente»: un clic e parte la mail che chiede la data. «Reso al mittente»: la merce torna a chi l’ha spedita e la giacenza si chiude.';""")
rep("""          <div><div class="lbl">Riconsegna</div><b>${t.giacPren[t.giac]?'Prenotata · data scelta dal cliente':cur.rico}</b></div>""",
    """          <div><div class="lbl">Riconsegna</div><b>${t.giacReso[t.giac]?'Reso al mittente':(t.giacData[t.giac]?'Prenotata · '+new Date(t.giacData[t.giac][0]).toLocaleDateString('it-IT',{weekday:'long',day:'numeric',month:'long'})+', ore '+t.giacData[t.giac][1]:(t.giacPren[t.giac]?'Prenotata':(t.giacChiesto[t.giac]?'Chiesta al cliente alle '+t.giacChiesto[t.giac]:cur.rico)))}</b></div>""")
rep("""        ${t.giacMsg==='chiesto'?msg('Mail al cliente pronta in Mail: avvisa della giacenza, del costo e chiede la data per la riconsegna.'):''}
        ${t.giacMsg==='prenotata'?msg('Riconsegna prenotata: la spedizione è nei giri del giorno scelto e la riconsegna è già in fattura.','Vai al Traffico','tGo','traffico'):''}
        <div class="row">${pren?'':b('Prenota la riconsegna','tGiacPren')}${pren?'':b('Chiedi al cliente quando riconsegnare','tGiacChiedi','','ghost')}${b('Reso al mittente','noop','','ghost')}</div>""",
"""        ${t.giacMsg==='chiesto'?msg('Mail inviata al cliente: lo avvisa della giacenza e del costo e chiede in che giorno riconsegnare. La sua risposta arriva in Mail.'):''}
        ${t.giacMsg==='prenotata'?msg('Riconsegna prenotata. La spedizione entra da sola nei giri di quel giorno e la riconsegna va in fattura.'):''}
        ${t.giacMsg==='reso'?msg('Reso confermato: la merce torna al mittente con il prossimo giro verso di lui, la giacenza si chiude e il viaggio di ritorno va in fattura.'):''}
        ${t.giacForm?`<div class="row" style="align-items:flex-end;gap:10px"><label class="stack" style="gap:4px"><span class="lbl">Giorno</span><input id="giacGiorno" type="date" min="${new Date().toISOString().slice(0,10)}" style="font:inherit;padding:10px 12px;border-radius:12px;border:1px solid var(--line)"></label><label class="stack" style="gap:4px"><span class="lbl">Ora</span><select id="giacOra" style="font:inherit;padding:10px 12px;border-radius:12px;border:1px solid var(--line)"><option value="">Scegli</option>${['08:00','09:00','10:00','11:00','12:00','14:00','15:00','16:00','17:00'].map(h=>`<option>${h}</option>`).join('')}</select></label>${b('Conferma','tGiacPren')}</div>`:''}
        ${t.giacResoOpen?`<div class="glass card stack" style="gap:8px;padding:14px"><b>Reso al mittente</b><span>Il cliente decide di non riconsegnare: la merce torna a chi l’ha spedita, la giacenza si chiude e il cliente paga il viaggio di ritorno con la sua tariffa.</span><div class="row">${b('Conferma il reso','tGiacResoOk')}${b('Annulla','tGiacReso','','ghost')}</div></div>`:''}
        ${t.giacReso[t.giac]||pren?'':`<div class="row">${b('Prenota la riconsegna','tGiacForm')}${t.giacChiesto[t.giac]?pill('Mail inviata al cliente','ok'):b('Chiedi al cliente quando riconsegnare','tGiacChiedi','','ghost')}${b('Reso al mittente','tGiacReso','','ghost')}</div>`}""")

# ================= MEZZI: autista fisso, Telepass, satellitare =================
rep("""    title='Mezzi'; hintTxt='tocca un tipo di mezzo: la colonna Sponda dice se ce l’ha.';""",
    """    title='Mezzi'; hintTxt='tocca un tipo di mezzo. Nella colonna Autista scegli l’autista fisso del mezzo: giri, Telepass e satellitare si collegano a lui.';""")
rep("""    <div class="glass tbox"><table class="t"><thead><tr><th>Targa</th><th>Tipo</th><th>Sponda</th><th>Autista</th><th>Telepass</th><th>Scadenza</th><th>Oggi</th></tr></thead><tbody>
    ${list.length?list.map(m=>`<tr><td><b>${m[0]}</b></td><td>${m[1]}</td><td>${m[2]}</td><td>${m[3]}</td><td>${m[4]}</td><td>${m[5]}</td><td>${m[6]==='Fermo'?pill('Fermo','red'):pill(m[6],'dark')}</td></tr>`).join(''):'<tr><td colspan="7" class="lbl">Nessun mezzo di questo tipo negli esempi.</td></tr>'}""",
"""    <div class="glass tbox"><table class="t"><thead><tr><th>Targa</th><th>Tipo</th><th>Sponda</th><th>Autista</th><th>Telepass</th><th>Satellitare</th><th>Scadenza</th><th>Oggi</th></tr></thead><tbody>
    ${list.length?list.map(m=>{const k=MEZZI.indexOf(m), aut=S.mezAut[k]||m[3];return `<tr><td><b>${m[0]}</b></td><td>${m[1]}</td><td>${m[2]}</td><td><select data-mez="${k}" aria-label="Autista fisso" style="font:inherit;padding:6px 8px;border-radius:10px;border:1px solid var(--line);background:#fff">${['—'].concat(AUT_TUTTI).map(x=>`<option ${x===aut?'selected':''}>${x}</option>`).join('')}</select></td><td>${m[4]}</td><td>${m[6]==='Fermo'?'<span class="lbl">Fermo</span>':pill('Collegato','ok')}</td><td>${m[5]}</td><td>${m[6]==='Fermo'?pill('Fermo','red'):pill(m[6],'dark')}</td></tr>`;}).join(''):'<tr><td colspan="8" class="lbl">Nessun mezzo di questo tipo negli esempi.</td></tr>'}""")
rep("const AUTISTI=[", "const AUT_TUTTI=['Autista 1','Autista 2','Autista 3','Autista 4','Autista 5','Autista 6','Autista 7','Autista 8','Autista 9','Autista 10'];\nconst AUTISTI=[")

# ================= NUOVE VOCI: Satellitare (Autotrasporti) e Telecamere (tutti e due) =================
rep("['telepass','Telepass'],", "['telepass','Telepass'],['satellitare','Satellitare'],")
rep("['presenze','Presenze'],['j7','J7']]", "['presenze','Presenze'],['telecamere','Telecamere'],['j7','J7']]")
rep("['stageTel','Stage Cellulari']]", "['stageTel','Stage Cellulari'],['telecamere','Telecamere']]")
rep("  tTp:i=>{S.t.tpSel=+i;},", "  tTp:i=>{S.t.tpSel=+i;},\n  tSat:i=>{S.t.satSel=+i;},\n  camSel:i=>{S.t.camSel=S.t.camSel===+i?null:+i;},")

nuove = r"""
/* satellitare: percorso del giorno confrontato con il giro */
const SAT=[
 {aut:'Autista 1',mezzo:'Sprinter [targa]',giro:'Zona Ovest',kmP:86,kmF:88,soste:0,dev:0,litri:'9,8',stato:'In regola',an:[]},
 {aut:'Autista 2',mezzo:'Motrice [targa]',giro:'Milano',kmP:54,kmF:67,soste:1,dev:1,litri:'21,4',stato:'2 da guardare',an:[
   ['11:20–11:58','Deviazione','6 km fuori rotta verso Corsico, lontano dalle fermate del giro','red'],
   ['13:05–13:43','Sosta','38 minuti fermo in via [indirizzo], Buccinasco: non è una fermata del giro','red'],
   ['10:12','Strada parallela','Viale [nome] invece di via [nome], a 400 m: non è un problema','ok']]},
 {aut:'Autista 3',mezzo:'Bilico [targa]',giro:'Lombardia Est',kmP:210,kmF:214,soste:0,dev:0,litri:'31,2',stato:'1 da guardare',an:[
   ['15:40','Rifornimento','Carta carburante usata a Cremona, 40 km fuori dal giro','red'],
   ['06:10–06:31','Motore acceso','21 minuti fermo con il motore acceso nel piazzale','red']]},
 {aut:'Autista 5',mezzo:'Furgone [targa]',giro:'Pavia',kmP:72,kmF:73,soste:0,dev:0,litri:'8,9',stato:'In regola',an:[]},
];
function satellitare(t){
  const cur=SAT[t.satSel]||SAT[0], bad=SAT.reduce((n,x)=>n+x.an.filter(a=>a[3]==='red').length,0);
  const mappa=`<svg viewBox="0 0 340 220" style="width:100%;display:block" role="img" aria-label="Percorso previsto e percorso fatto">
    <rect width="340" height="220" rx="16" fill="rgba(17,18,20,.03)"/>
    <path d="M0 110 Q170 90 340 130" stroke="rgba(17,18,20,.07)" stroke-width="10" fill="none"/><path d="M160 0 Q170 120 150 220" stroke="rgba(17,18,20,.07)" stroke-width="8" fill="none"/>
    <path d="M40 180 L110 120 L180 100 L250 70 L300 50" stroke="#111214" stroke-width="3" fill="none" stroke-dasharray="7 6"/>
    ${cur.an.some(a=>a[1]==='Deviazione')?'<path d="M40 180 L110 120 L120 160 L150 175 L180 100 L250 70 L300 50" stroke="#b42318" stroke-width="3" fill="none"/>':'<path d="M40 180 L112 122 L178 98 L252 72 L300 50" stroke="#146c43" stroke-width="3" fill="none"/>'}
    ${cur.an.some(a=>a[1]==='Sosta')?'<circle cx="150" cy="175" r="9" fill="#b42318"/><text x="150" y="200" text-anchor="middle" font-size="11" font-weight="700" fill="#b42318">Sosta 38 min</text>':''}
    ${[[110,120],[180,100],[250,70],[300,50]].map(p=>`<circle cx="${p[0]}" cy="${p[1]}" r="6" fill="#fff" stroke="#111214" stroke-width="2"/>`).join('')}
    <rect x="26" y="168" width="28" height="24" rx="6" fill="#111214"/></svg>
    <div class="row lbl" style="gap:14px;margin-top:6px"><span>- - - giro previsto</span><span style="color:${cur.an.some(a=>a[1]==='Deviazione')?'var(--alert)':'var(--ok)'}">——— percorso fatto</span></div>`;
  return `<div class="grid g4">
      <div class="glass card"><div class="lbl">Mezzi in giro</div><div class="big">${SAT.length}</div><div class="lbl">posizione dal satellitare</div></div>
      <div class="glass card"><div class="lbl">Km oggi</div><div class="big">${SAT.reduce((n,x)=>n+x.kmF,0)}</div><div class="lbl">previsti ${SAT.reduce((n,x)=>n+x.kmP,0)}</div></div>
      <div class="glass card"><div class="lbl">Da guardare</div><div class="big">${bad}</div><div class="lbl">deviazioni, soste, rifornimenti</div></div>
      <div class="glass card"><div class="lbl">Gasolio a ottobre</div><div class="big">€ [importo]</div><div class="lbl">carte carburante e km a confronto</div></div>
    </div>
    <div class="row" style="align-items:flex-start;gap:16px">
      <div class="glass tbox" style="flex:1 1 520px;min-width:0"><table class="t nw"><thead><tr><th>Autista</th><th>Mezzo</th><th>Giro</th><th>Km previsti</th><th>Km fatti</th><th>Litri/100 km</th><th>Controllo</th></tr></thead><tbody>
        ${SAT.map((r,i)=>`<tr class="click" data-act="tSat" data-arg="${i}" style="${t.satSel===i?'background:var(--soft)':''}"><td><b>${r.aut}</b></td><td>${r.mezzo}</td><td>${r.giro}</td><td>${r.kmP}</td><td>${r.kmF>r.kmP*1.1?`<span class="miss">${r.kmF}</span>`:r.kmF}</td><td>${r.litri}</td><td>${r.an.some(a=>a[3]==='red')?pill(r.stato,'red'):pill(r.stato,'ok')}</td></tr>`).join('')}
      </tbody></table></div>
      <div class="glass card stack" style="flex:1 1 380px;min-width:0"><div class="row between"><b>${cur.aut} · oggi</b><span class="lbl">${cur.mezzo}</span></div>${mappa}
        <div class="list">${cur.an.length?cur.an.map(a=>`<div class="li"><span class="row between" style="width:100%"><b>${a[1]}</b>${pill(a[0],a[3]==='red'?'red':'')}</span><span class="lbl">${a[2]}</span></div>`).join(''):'<div class="lbl" style="padding:10px">Nessuna anomalia: ha seguito il giro.</div>'}</div></div>
    </div>
    <p class="lbl" style="margin:0">Il programma confronta ogni giorno il percorso del satellitare con il giro: le strade parallele vicine non contano, le deviazioni lontane e le soste fuori dalle fermate sì. In più: carte carburante contro km, rifornimenti lontani dal giro, motore acceso da fermo, Telepass contro posizione. Il satellitare già montato sui mezzi si collega tramite il suo fornitore [nome da comunicare].</p>`;
}

/* telecamere: una sola sezione per tutto il capannone, visibile solo alla Direzione */
const CAM=['Ingresso','Piazzale','Baie di carico','Corsia S03','Corsia S07','Stage'];
const CAM_AVVISI=[['02:14','Piazzale','Persona vicino al cancello, fuori orario','red'],['03:40','Piazzale','Auto ferma 6 minuti davanti all’ingresso','red'],['05:52','Ingresso','Apertura del magazzino: Magazziniere 1, badge regolare','ok']];
const CAM_SCAN=[['B-0141','S03-2-1','Entrata','Magazziniere 1','06:22','Baie di carico'],['B-0138','S03-2-2','Trasferisci','Mulettista 2','07:05','Corsia S03'],['Collo 3 di 4','—','Uscita','Magazziniere 2','07:41','Baie di carico'],['S07-2-1','S07','Missione','Magazziniere 1','08:10','Corsia S07']];
function telecamere(t){
  const ora0=new Date().toLocaleTimeString('it-IT',{hour:'2-digit',minute:'2-digit'});
  const vivo=(n,i)=>`<button class="tcam ${t.camSel===i?'on':''}" data-act="camSel" data-arg="${i}"><span class="cam-img" aria-hidden="true"></span><span class="cam-top"><span class="dot"></span>Dal vivo</span><span class="cam-nome">${n}</span><span class="cam-ora">${ora0}</span></button>`;
  return `<div class="glass card row between" style="padding:12px 16px"><span><b>Visibile solo alla Direzione</b> <span class="lbl">Tiziano, Sara, Matteo e Pierpaolo. Il commercialista vede i numeri, non le immagini.</span></span>${pill('Rete separata','dark')}</div>
    <div class="camgrid">${CAM.map(vivo).join('')}</div>
    ${t.camSel!==null?`<div class="glass card stack"><div class="row between"><b>${CAM[t.camSel]} · grande</b>${b('Chiudi','camSel',t.camSel,'ghost sm')}</div><div class="tcam big-cam"><span class="cam-img"></span><span class="cam-top"><span class="dot"></span>Dal vivo</span><span class="cam-nome">${CAM[t.camSel]}</span><span class="cam-ora">${ora0}</span></div><div class="lbl">Registrazione degli ultimi [giorni] giorni sul registratore in capannone: si scorre per ora.</div></div>`:''}
    <div class="row" style="align-items:flex-start;gap:16px">
      <div class="glass card stack" style="flex:1 1 360px;min-width:0"><b>Avvisi della notte</b><div class="list">${CAM_AVVISI.map(a=>`<div class="li"><span class="row between" style="width:100%"><b>${a[0]} · ${a[1]}</b>${pill(a[3]==='red'?'Da guardare':'Normale',a[3]==='red'?'red':'ok')}</span><span class="lbl">${a[2]} · foto salvata</span></div>`).join('')}</div><span class="lbl">Gli avvisi arrivano anche sul telefono della Direzione.</span></div>
      <div class="glass tbox" style="flex:2 1 520px;min-width:0"><div style="padding:14px 14px 0;font-weight:700">Foto delle scansioni</div><table class="t nw"><thead><tr><th>Cosa</th><th>Posto</th><th>Movimento</th><th>Chi</th><th>Ora</th><th>Telecamera</th><th></th></tr></thead><tbody>
        ${CAM_SCAN.map(r=>`<tr><td><b>${r[0]}</b></td><td>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td><td>${r[4]}</td><td>${r[5]}</td><td><span class="cam-mini" aria-label="Foto"></span></td></tr>`).join('')}
      </tbody></table><p class="lbl" style="margin:0;padding:0 14px 14px">A ogni scansione la telecamera più vicina salva una foto insieme al movimento: se qualcosa non torna, si apre il movimento e si vede cos’è successo.</p></div>
    </div>`;
}
"""
rep("/* siti vetrina: lo stesso HTML dei siti veri, dentro una finestra */", nuove + "\n/* siti vetrina: lo stesso HTML dei siti veri, dentro una finestra */")

# sezioni nei due gestionali
rep("  if(s==='mezzi'){\n    title='Mezzi';",
    "  if(s==='satellitare'){ title='Satellitare'; hintTxt='tocca un autista: vedi il giro previsto e il percorso fatto, con le deviazioni e le soste da guardare.'; body=satellitare(t); }\n  if(s==='telecamere'){ title='Telecamere'; hintTxt='tocca una telecamera per vederla grande. Sotto: gli avvisi della notte e la foto salvata a ogni scansione del magazzino.'; body=telecamere(t); }\n  if(s==='mezzi'){\n    title='Mezzi';")
rep("  return hint(hintTxt)+shell('Corporation',C_NAV,s,'cGo',title,body,'Cerca');",
    "  if(s==='telecamere'){ title='Telecamere'; hintTxt='la stessa sezione del gestionale Autotrasporti: il capannone è uno solo.'; body=telecamere(S.t); }\n  return hint(hintTxt)+shell('Corporation',C_NAV,s,'cGo',title,body,'Cerca');")

# anomalie: anche il satellitare
rep("  A.push(['Telepass','3 passaggi fuori orario o senza giro','Direzione','Ieri','telepass|']);",
    "  A.push(['Telepass','3 passaggi fuori orario o senza giro','Direzione','Ieri','telepass|']);\n  A.push(['Satellitare','Autista 2: deviazione di 6 km e sosta di 38 minuti fuori giro','Direzione','Oggi','satellitare|']);\n  A.push(['Satellitare','Autista 3: rifornimento a 40 km dal giro','Direzione','Oggi','satellitare|']);")

# stile: selettore Bancale/Collo e telecamere
rep(".browser{border-radius:22px;overflow:hidden;padding:0}", """.seg{display:flex;padding:4px;border-radius:14px;background:var(--soft);gap:4px}
.seg button{flex:1;font:inherit;font-weight:700;font-size:16px;padding:10px;border:0;border-radius:10px;background:transparent;cursor:pointer;color:var(--ink)}
.seg button.on{background:var(--solid);color:var(--on-solid)}
.camgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.tcam{display:block;width:100%;min-height:0;position:relative;aspect-ratio:16/9;border-radius:16px;overflow:hidden;border:0;padding:0;cursor:pointer;background:#1b1d21;color:#fff;font:inherit;text-align:left}
.tcam.on{outline:3px solid var(--solid);outline-offset:3px}
.cam-img{position:absolute;inset:0;background:radial-gradient(120% 90% at 30% 20%,rgba(255,255,255,.16),transparent 60%),linear-gradient(160deg,#2a2d33,#121316)}
.cam-img::after{content:"";position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(255,255,255,.025) 0 2px,transparent 2px 4px)}
.cam-top{position:absolute;left:10px;top:8px;font-size:12px;font-weight:700;display:flex;align-items:center;gap:6px}
.cam-top .dot{width:8px;height:8px;border-radius:99px;background:#e5484d}
.cam-nome{position:absolute;left:10px;bottom:8px;font-weight:700;font-size:14px}
.cam-ora{position:absolute;right:10px;bottom:8px;font-size:12px;opacity:.8}
.big-cam{aspect-ratio:16/8;cursor:default}
.cam-mini{display:inline-block;width:46px;height:28px;border-radius:6px;background:linear-gradient(160deg,#2a2d33,#121316);vertical-align:middle}
@media (max-width:760px){.camgrid{grid-template-columns:1fr 1fr}}
.browser{border-radius:22px;overflow:hidden;padding:0}""")

open(P, 'w', encoding='utf8').write(s)
print('ok', len(s))
