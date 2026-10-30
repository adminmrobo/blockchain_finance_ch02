LAB.start({anchor:'D',init:function(){
function bits(h){var s='';for(var i=0;i<64;i++)s+=('000'+parseInt(h[i],16).toString(2)).slice(-4);return s;}
/* ① 지문 */
(function(){var DEF='A가 B에게 10,000원을 보냈다',inp=$('#t1'),prev=null,cur=SHA256(DEF),c1b=$('#c1b');
  var LONG=' '+'블록체인은 거래의 이력을 시간 순서대로 쌓는 장부다. '.repeat(70);
  function hx(){prev=cur;cur=SHA256(inp.value);render();}
  inp.addEventListener('input',hx);
  $('#b1Comma').addEventListener('click',function(){inp.value+=',';hx();});
  $('#b1Long').addEventListener('click',function(){inp.value+=LONG;hx();});
  $('#b1Undo').addEventListener('click',function(){inp.value=DEF;hx();});
  function diffs(){if(!prev)return [null,null];var d=0,b=0,pb=bits(prev),cb=bits(cur);for(var i=0;i<64;i++)if(prev[i]!==cur[i])d++;for(i=0;i<256;i++)if(pb[i]!==cb[i])b++;return [d,b];}
  function drawB(){var W=fit(c1b,170),H=170,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var cb=bits(cur),pb=prev?bits(prev):cb,cw=Math.min(16,(W-40)/64);
    for(var i=0;i<256;i++){var cx=20+(i%64)*cw,cy=36+Math.floor(i/64)*(cw+4);x.fillStyle=pb[i]!==cb[i]?C.eye:(cb[i]==='1'?'rgba(130,184,255,.6)':'rgba(130,184,255,.15)');x.fillRect(cx,cy,cw-2,cw);}
    var d=diffs();txt(x,prev?'바뀐 비트 '+d[1]+' / 256':'처음 계산한 해시 (파랑 = 1, 옅은 파랑 = 0)',20,24,{w:700,c:prev?C.eye:C.muted});stamp(x,W,'실제 SHA-256 계산');}
  function render(){$('#h1prev').textContent=prev||'— (아직 없음)';var s='';for(var i=0;i<64;i++)s+=(prev&&prev[i]!==cur[i])?'<mark>'+cur[i]+'</mark>':cur[i];$('#h1now').innerHTML=s;
    var d=diffs(),len=new TextEncoder().encode(inp.value).length;
    kpis($('#k1'),[[fmt(len)+'B','입력 크기 (UTF-8)','a'],['64자','해시 길이 (항상 같음)','g'],[d[0]===null?'—':d[0]+' / 64','바뀐 16진수 자리','m'],[d[1]===null?'—':d[1]+' / 256','바뀐 비트','r']]);
    $('#eq1').innerHTML='SHA-256(<em>입력 '+fmt(len)+'바이트</em>) → <b>256비트 = 64자</b>'+(d[1]!==null?' · 바뀐 비트 <i>'+d[1]+'</i> (평균 기대 128)':'');
    var m=[];if(d[1]!==null)m.push(['m','입력이 조금 바뀌었는데 비트 '+d[1]+'개, 16진수 '+d[0]+'자가 달라졌어요. 무작위라면 평균 128비트(64자 중 60자)예요.']);
    m.push(['g','입력이 '+fmt(len)+'바이트여도 해시는 64자예요. 그래서 블록 머리글에 짧게 적을 수 있어요.']);ins($('#ins1'),m);drawB();}
  addEventListener('resize',drawB);render();})();

/* ② 단방향 */
(function(){var c2b=$('#c2b'),pin=4719,s=0,run=false,n=0,found=-1,rate=0,t0=0,AL='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  function salt(){var r=rng(77),o='';for(var i=0;i<s;i++)o+=AL[Math.floor(r()*62)];return o;}
  function p4(i){return ('000'+i).slice(-4);}
  function target(){return SHA256(p4(pin)+salt());}
  function space(){return 10000*Math.pow(62,s);}
  slider('r2p',function(v){pin=v;reset();},function(v){return p4(v);});slider('r2s',function(v){s=v;reset();});
  $('#b2Go').addEventListener('click',function(){if(found>=0||n>=10000)reset();run=!run;if(run)t0=performance.now();this.textContent=run?'❚❚ 멈춤':'▶ 대입 시작';});
  $('#b2Reset').addEventListener('click',reset);
  function reset(){run=false;n=0;found=-1;$('#b2Go').textContent='▶ 대입 시작';$('#h2target').textContent='목표 해시: '+target();upd();}
  function step(){if(!run)return;var T=target(),st=performance.now();
    while(performance.now()-st<12&&n<10000){var g=SHA256(p4(n)+(s?'':''));if(s===0&&g===T){found=n;run=false;break;}n++;}
    rate=n/Math.max(0.001,(performance.now()-t0)/1000);
    if(n>=10000&&found<0){run=false;}if(!run)$('#b2Go').textContent='▶ 다시 시작';upd();}
  function years(){var sec=space()/Math.max(1,rate||150000);return sec/31557600;}
  function drawB(){var W=fit(c2b,220),H=220,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var side=Math.min(H-50,(W-260)),cell=side/100,X0=20,Y0=34;
    x.fillStyle='rgba(157,155,184,.12)';x.fillRect(X0,Y0,side,side);
    var tried=Math.min(n,10000);for(var r=0;r<Math.floor(tried/100);r++){x.fillStyle='rgba(157,155,184,.45)';x.fillRect(X0,Y0+r*cell,side,cell);}x.fillRect(X0,Y0+Math.floor(tried/100)*cell,(tried%100)*cell,cell);
    if(found>=0){x.fillStyle=C.gfp;x.fillRect(X0+(found%100)*cell-2,Y0+Math.floor(found/100)*cell-2,cell+4,cell+4);}
    txt(x,'후보 0000~9999 ('+(s?'덧붙인 문자 없이 시도':'전체')+')',X0,24,{s:12,c:C.muted});
    var tx=X0+side+20;txt(x,'시도 '+fmt(n)+'번',tx,60,{w:700,s:15});txt(x,'속도 약 '+fmt(rate)+'회/초',tx,86,{s:12,c:C.muted});
    txt(x,found>=0?'찾았다: '+p4(found):(s&&n>=10000?'만 번을 다 해도 못 찾음':''),tx,118,{w:700,c:found>=0?C.gfp:C.eye});
    if(s)txt(x,'전체 후보 '+space().toExponential(2)+'개 → 이 속도로 약 '+years().toExponential(1)+'년',tx,150,{s:12,c:C.amber});stamp(x,W,'실제 SHA-256 계산');}
  function upd(){kpis($('#k2'),[[s?space().toExponential(2):fmt(space()),'후보 수','a'],[fmt(n),'시도한 후보','m'],[found>=0?p4(found):'—','찾은 원문',found>=0?'r':'g'],[s?'약 '+years().toExponential(1)+'년':(rate?(10000/rate).toFixed(2)+'초':'—'),'전부 시도하는 데 걸릴 시간',s?'g':'r']]);
    $('#eq2').innerHTML='후보 수 = 10<sup>4</sup> × 62<sup><i>'+s+'</i></sup> = <b>'+(s?space().toExponential(2):fmt(space()))+'</b> · 찾을 확률 = min(1, 시도 ÷ 후보)';
    var m=[];if(found>=0)m.push(['r','4자리 비밀번호는 '+fmt(found+1)+'번째 시도에서 찾았어요. 해시를 거꾸로 계산한 게 아니라 하나씩 해시해서 비교했어요.']);
    else if(s)m.push(['g','공격자가 모르는 문자 '+s+'자를 덧붙이자 후보가 '+space().toExponential(2)+'개가 됐어요. 같은 방법으로는 사실상 끝나지 않아요.']);
    else m.push(['a','"대입 시작"을 눌러 보세요. 후보가 만 개뿐이라 금방 끝나요.']);ins($('#ins2'),m);drawB();}
  addMod(c2b,step);addEventListener('resize',drawB);reset();})();

function prob(tries,space){return Math.min(1,tries/space);}
Duel({names:{fly:'초파리 (비밀 16자 덧붙임)',robo:'Money-Robo (6자리 그대로)'},higherIsBetter:false,drawMargin:0,
  run:function(){return {fly:prob(1e6,1e6*Math.pow(62,16)),robo:prob(1e6,1e6)};},bar:function(v){return v;},fmt:function(v){return v>=0.001?(100*v).toFixed(1)+'%':v.toExponential(1);},
  lesson:'해시는 거꾸로 계산할 수 없지만, 후보가 적으면 다 대입해 볼 수 있다',
  say:function(r){return '100만 번 대입으로 원문을 찾을 확률은 초파리 쪽 '+r.fly.toExponential(1)+', Money-Robo 쪽 '+(100*r.robo).toFixed(0)+'%예요. 6자리 숫자는 후보가 딱 100만 개라 반드시 찾아요.';}});
}});
