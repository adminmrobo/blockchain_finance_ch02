LAB.start({anchor:'D',init:function(){
var NM=['A','B','C'];
/* ① 데이터베이스 */
(function(){var c1=$('#c1'),c1b=$('#c1b'),bal,ops,admin,flash=null,t=0;
  function reset(){bal=[10000,10000,10000];ops=0;admin=false;flash=null;upd();}
  $$('#lv1 [data-tx]').forEach(function(b){b.addEventListener('click',function(){var p=b.dataset.tx.split(',').map(Number);if(bal[p[0]]<p[2])return;var old=bal.slice();bal[p[0]]-=p[2];bal[p[1]]+=p[2];ops++;flash={old:old,t:0};upd();});});
  $('#b1Admin').addEventListener('click',function(){var old=bal.slice();bal[2]+=5000;admin=true;flash={old:old,t:0};upd();});
  $('#b1Reset').addEventListener('click',reset);
  function drawA(){var W=fit(c1,210),H=210,x=c1.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var cw=Math.min(150,(W*0.5-40)/3);
    txt(x,'잔액 표 (데이터베이스)',20,30,{w:700});NM.forEach(function(n,i){var X=20+i*(cw+10);x.fillStyle=C.panel2;rr(x,X,44,cw,70,8);x.fill();txt(x,n,X+12,66,{s:12,c:C.muted});txt(x,fmt(bal[i])+'원',X+cw/2,100,{a:'center',s:18,w:700});});
    var QX=W*0.55;txt(x,'감사 질문',QX,30,{w:700});[['지금 잔액은?',true],['어제 잔액은?',false],['누가 C를 바꿨나?',false],['관리자 변경 흔적?',false]].forEach(function(q,i){txt(x,(q[1]?'✓ ':'✗ ')+q[0],QX,62+i*28,{s:14,c:q[1]?C.gfp:C.eye});});
    txt(x,'저장 칸 3개 · 거래 '+ops+'번',20,H-14,{s:12,c:C.muted});stamp(x,W,'예시값');}
  function drawB(dt){t+=dt;if(flash)flash.t+=dt;var W=fit(c1b,150),H=150,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var cw=(W-80)/3;
    NM.forEach(function(n,i){var X=20+i*(cw+20);x.fillStyle=C.panel2;rr(x,X,40,cw,60,8);x.fill();txt(x,n,X+10,58,{s:12,c:C.muted});
      if(flash&&flash.old[i]!==bal[i]){var a=Math.max(0,1-flash.t);x.globalAlpha=REDUCE?0:a;txt(x,fmt(flash.old[i]),X+cw/2,84,{a:'center',s:16,c:C.eye});x.globalAlpha=REDUCE?1:1-a;txt(x,fmt(bal[i]),X+cw/2,84,{a:'center',s:16,w:700});x.globalAlpha=1;}
      else txt(x,fmt(bal[i]),X+cw/2,84,{a:'center',s:16,w:700});});
    txt(x,flash?'덮어쓴 이전 값은 사라진다':'거래 버튼을 눌러 보세요',20,H-16,{s:12,c:flash?C.eye:C.muted});stamp(x,W,'설명용 장면');}
  function upd(){kpis($('#k1'),[['3칸','저장하는 칸 (거래 수와 무관)','g'],['1줄','잔액 조회에 읽는 줄','g'],['0줄','남은 과거 기록','r'],[admin?'흔적 없음':'—','관리자 변경',admin?'r':'a']]);
    $('#eq1').innerHTML='잔액[<b>보낸 사람</b>] ← 잔액 − 금액, 잔액[<em>받은 사람</em>] ← 잔액 + 금액 (이전 값은 <i>덮어씀</i>)';
    var m=[['g','잔액 조회는 칸 하나만 읽으면 돼요. 몇 번을 거래해도 저장 칸은 3개예요.']];if(admin)m.push(['r','관리자가 C 잔액을 바꿨지만 표에는 아무 흔적도 없어요. 거래였는지 손으로 고친 건지 구별할 수 없어요.']);ins($('#ins1'),m);drawA();drawB(0);}
  mod(c1b,drawB,true);addEventListener('resize',function(){drawA();drawB(0);});reset();})();

/* ② 이력 장부 */
(function(){var c2=$('#c2'),c2b=$('#c2b'),L,last=null,tam=false,scan=null,t=0;
  var INIT=[[0,1,2000],[2,0,1000],[1,2,4000],[0,2,3000]];
  function link(L){var p='0'.repeat(64);L.forEach(function(e){e.prev=p;e.h=SHA256(e.s+'>'+e.r+':'+e.a+'|'+p);p=e.h;});}
  function reset(){L=INIT.map(function(e){return {s:e[0],r:e[1],a:e[2]}});link(L);tam=false;last=null;scan=null;upd();}
  function verify(){var p='0'.repeat(64),bad=[];L.forEach(function(e,i){var h=SHA256(e.s+'>'+e.r+':'+e.a+'|'+e.prev);if(e.prev!==p||h!==e.h)bad.push(i+1);p=e.h;});return bad;}
  function balances(){var b=[10000,10000,10000];L.forEach(function(e){b[e.s]-=e.a;b[e.r]+=e.a;});return b;}
  $$('#lv2 [data-rq]').forEach(function(btn){btn.addEventListener('click',function(){var q=btn.dataset.rq.split(',').map(Number),b=balances(),bad=verify();
    var ok=!bad.length&&b[q[0]]>=q[2];last={q:q,ok:ok,why:bad.length?'이력이 변조되어 검토 중단':(ok?'잔액 충분':'잔액 부족 ('+NM[q[0]]+' '+fmt(b[q[0]])+'원)'),rows:L.length};
    if(ok){var e={s:q[0],r:q[1],a:q[2]};e.prev=L[L.length-1].h;e.h=SHA256(e.s+'>'+e.r+':'+e.a+'|'+e.prev);L.push(e);}scan={p:0,ok:ok};upd();});});
  $('#b2Old').addEventListener('click',function(){if(L.length>=3){L[2].a+=5000;tam=true;}upd();});
  $('#b2Reset').addEventListener('click',reset);
  function drawA(){var W=fit(c2,250),H=250,x=c2.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var bad=verify(),b=balances(),show=L.slice(-8),off=L.length-show.length;
    txt(x,'거래 이력 (시간 순서, 지우지 않음)',20,24,{w:700});
    show.forEach(function(e,i){var n=off+i+1,Y=36+i*24,isBad=bad.indexOf(n)>=0;x.fillStyle=isBad?'rgba(240,96,77,.18)':C.panel2;rr(x,20,Y,W*0.55,20,4);x.fill();
      txt(x,n+'. '+NM[e.s]+' → '+NM[e.r]+'  '+fmt(e.a)+'원',28,Y+15,{s:12,c:isBad?C.eye:C.text});txt(x,'h '+e.h.slice(0,8)+(isBad?' ✗':' ✓'),20+W*0.55-8,Y+15,{a:'right',s:11,c:isBad?C.eye:C.gfp});});
    var BX=W*0.62;txt(x,'이력에서 계산한 잔액',BX,24,{w:700});NM.forEach(function(n,i){txt(x,n+': '+fmt(b[i])+'원',BX,56+i*26,{s:14});});
    if(last)txt(x,'요청 '+NM[last.q[0]]+' → '+NM[last.q[1]]+' '+fmt(last.q[2])+': '+(last.ok?'승인':'거절')+' ('+last.why+')',BX,150,{s:12,w:700,c:last.ok?C.gfp:C.eye});
    stamp(x,W,'예시값 · 실제 SHA-256');}
  function drawB(dt){t+=dt;var W=fit(c2b,150),H=150,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var n=L.length,cw=Math.min(60,(W-180)/Math.max(1,n));
    for(var i=0;i<n;i++){var X=20+i*cw;x.fillStyle='#efe6d2';rr(x,X,50,cw-6,40,4);x.fill();txt(x,i+1,X+(cw-6)/2,75,{a:'center',s:11,c:'#3a3040'});}
    if(scan){scan.p=Math.min(1,scan.p+dt*0.8);if(REDUCE)scan.p=1;var sx=20+scan.p*(n*cw);x.strokeStyle=C.amber;x.lineWidth=2;x.beginPath();x.moveTo(sx,40);x.lineTo(sx,100);x.stroke();x.lineWidth=1;
      if(scan.p>=1)txt(x,scan.ok?'검토 통과 → 맨 끝에 덧붙임':'검토에서 거절',20+n*cw+16,75,{w:700,c:scan.ok?C.gfp:C.eye});}
    txt(x,'요청마다 이력 '+n+'줄을 처음부터 검토',20,H-14,{s:12,c:C.muted});stamp(x,W,'설명용 장면');}
  function upd(){var bad=verify();kpis($('#k2'),[[L.length+'줄','쌓인 이력',''],[bad.length?bad[0]+'번부터 어긋남':'정상','이력 사슬',bad.length?'r':'g'],[L.length+'줄','잔액 계산·검토에 읽는 줄','m'],[last?(last.ok?'승인':'거절'):'—','마지막 송금 요청',last?(last.ok?'g':'r'):'a']]);
    $('#eq2').innerHTML='잔액[X] = <b>10,000</b> + Σ(받은 금액) − Σ(보낸 금액) · 승인 조건: <em>이력 사슬 정상</em> 그리고 <i>잔액 ≥ 요청 금액</i>';
    var m=[];if(tam)m.push(['r','3번째 이력의 금액을 고치자 그 줄부터 해시 연결이 어긋났어요. 이력이 변조되면 새 요청은 검토 단계에서 멈춰요.']);
    if(last&&!tam)m.push([last.ok?'g':'r','요청 '+NM[last.q[0]]+' → '+NM[last.q[1]]+' '+fmt(last.q[2])+'원: '+(last.ok?'이력을 검토해 승인하고 맨 끝에 덧붙였어요.':'이력으로 계산한 잔액이 모자라 거절했어요.')]);
    m.push(['a','이력은 거래가 쌓일수록 길어져요. 지금은 요청 하나에 '+L.length+'줄을 읽어요.']);ins($('#ins2'),m);drawA();drawB(0);}
  mod(c2b,drawB,true);addEventListener('resize',upd);reset();})();

function rows(replay){var s=0;for(var k=1;k<=1000;k++)s+=replay?10*k:1;return s;}
Duel({names:{fly:'초파리 (이력 다시 더하기)',robo:'주판봇 (DB 칸 읽기)'},higherIsBetter:false,drawMargin:0,
  run:function(){return {fly:rows(true),robo:rows(false)};},bar:function(v){return Math.log10(v)/7;},fmt:function(v){return fmt(v)+'줄';},
  lesson:'대량 데이터를 빠르게 다루는 일은 데이터베이스가 낫다',
  say:function(r){return '조회 1,000번에 읽은 줄은 초파리 쪽 '+fmt(r.fly)+'줄, 주판봇 쪽 '+fmt(r.robo)+'줄이에요. 약 '+fmt(r.fly/r.robo)+'배 차이예요. 막대는 로그 눈금이에요.';}});
}});
