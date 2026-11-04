LAB.start({anchor:'C',init:function(){
/* 백서 11절 C 코드(AttackerSuccessProbability)를 그대로 옮김 */
function attackerSuccess(q,z){var p=1.0-q;if(p<=q)return 1;var lambda=z*(q/p),sum=1.0,i,k;
  for(k=0;k<=z;k++){var poisson=Math.exp(-lambda);for(i=1;i<=k;i++)poisson*=lambda/i;sum-=poisson*(1-Math.pow(q/p,z-k));}return Math.max(0,Math.min(1,sum));}
function needZ(q,lim){if(q>=0.5)return Infinity;for(var z=0;z<2000;z++)if(attackerSuccess(q,z)<lim)return z;return Infinity;}
var WPT=[[0.1,1,0.2045873],[0.1,6,0.0002428]],WPZ=[[0.10,5],[0.30,24]];
function sig(v){return v>=1e-7?v.toFixed(7):v.toExponential(2);}
function sgn(v){return (v>0?'+':v<0?'−':'')+Math.abs(v);}

/* ① 난이도 조정 */
function retarget(jump,grow){var r=rng(27),H=1,Da=1,out=[];
  for(var k=0;k<30;k++){if(k===10)H*=1+jump/100;else if(k>10)H*=1+grow/100;
    var sa=0,sn=0;for(var b=0;b<50;b++){var e=-Math.log(1-r());sa+=e*10*Da/H;sn+=e*10/H;}
    var ta=sa/50,tn=sn/50;out.push({k:k+1,H:H,D:Da,adj:ta,no:tn});Da=Da*10/ta;}return out;}
(function(){var c1=$('#c1'),c1b=$('#c1b'),jump=200,grow=3,adj=true,R,t=0;
  slider('r1j',function(v){jump=v;upd();},sgn);slider('r1g',function(v){grow=v;upd();});
  $('#b1Adj').addEventListener('click',function(){adj=!adj;this.setAttribute('aria-pressed',adj);this.textContent=adj?'난이도 조정 켬':'난이도 조정 끔';upd();});
  function drawA(){var W=fit(c1,230),H=230,x=c1.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    var L=46,Rr=W-16,T=30,B=H-34,ymax=Math.max(20,Math.ceil(Math.max.apply(null,R.map(function(o){return Math.max(o.no,o.adj)}))/20)*20);
    function X(k){return L+(Rr-L)*(k-1)/29}function Y(v){return B-(B-T)*Math.min(v,ymax)/ymax}
    for(var g=0;g<=ymax;g+=ymax/4){txt(x,Math.round(g)+'분',L-6,Y(g)+4,{a:'right',s:10,c:C.muted});}
    [1,10,20,30].forEach(function(k){txt(x,k+'구간',X(k),H-14,{a:'center',s:10,c:C.muted});});
    x.strokeStyle=C.amber;x.setLineDash([5,4]);x.beginPath();x.moveTo(L,Y(10));x.lineTo(Rr,Y(10));x.stroke();x.setLineDash([]);txt(x,'목표 10분',Rr,Y(10)-6,{a:'right',s:11,c:C.amber});
    x.strokeStyle='rgba(157,155,184,.35)';x.beginPath();x.moveTo(X(10.5),T);x.lineTo(X(10.5),B);x.stroke();txt(x,'계산력 '+sgn(jump)+'%',X(10.5)+4,T+10,{s:11,c:C.muted});
    function line(key,col,w,a){x.globalAlpha=a;x.strokeStyle=col;x.lineWidth=w;x.beginPath();R.forEach(function(o,i){var px=X(o.k),py=Y(o[key]);i?x.lineTo(px,py):x.moveTo(px,py);});x.stroke();x.lineWidth=1;x.globalAlpha=1;}
    line('no',C.eye,adj?1.5:3,adj?0.5:1);if(adj)line('adj',C.gfp,3,1);
    txt(x,'— 조정 없음',L+4,T-12,{s:11,c:C.eye,w:700});if(adj)txt(x,'— 조정 있음',L+90,T-12,{s:11,c:C.gfp,w:700});
    stamp(x,W,'예시값 · 시드 27');}
  function drawB(dt){t+=dt;var W=fit(c1b,150),H=150,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var last=R[R.length-1],L=100,span=120,sweep=REDUCE?span:(t*20)%(span+20);
    var r=rng(7),rows=[['조정 없음',last.no,C.eye],['조정 있음',last.adj,C.gfp]];
    rows.forEach(function(row,i){var Y=44+i*46;txt(x,row[0],12,Y+5,{s:12,w:700,c:row[2]});x.strokeStyle=C.rule;x.beginPath();x.moveTo(L,Y);x.lineTo(W-16,Y);x.stroke();
      var tt=0,n=0;r=rng(7);while(true){tt+=-Math.log(1-r())*row[1];if(tt>span)break;if(tt<=sweep){var px=L+(W-16-L)*tt/span;x.fillStyle=row[2];rr(x,px-5,Y-7,10,14,2);x.fill();n++;}}
      txt(x,n+'블록',12,Y+20,{s:11,c:C.muted});});
    var sx=L+(W-16-L)*Math.min(sweep,span)/span;x.strokeStyle=C.amber;x.beginPath();x.moveTo(sx,26);x.lineTo(sx,H-30);x.stroke();
    txt(x,'30구간째 계산력으로 '+Math.round(Math.min(sweep,span))+'분 / 120분',12,H-12,{s:11,c:C.muted});stamp(x,W,'설명용 장면');}
  function upd(){R=retarget(jump,grow);var last=R[R.length-1];
    kpis($('#k1'),[['×'+last.H.toFixed(2),'30구간째 계산력 (처음 대비)','a'],[last.no.toFixed(1)+'분','조정 없을 때 블록 간격','r'],[adj?last.adj.toFixed(1)+'분':'—','조정 있을 때 블록 간격',adj?'g':'m'],[adj?'×'+last.D.toFixed(2):'×1.00','30구간째 난이도','m']]);
    $('#eq1').innerHTML='간격 = <b>10분</b> × <em>난이도</em> ÷ <i>계산력</i> · 다음 난이도 = 난이도 × 10 ÷ <b>지난 구간 실제 간격</b>';
    var m=[],k11=R[10];m.push([adj?'g':'r',adj?'계산력이 '+sgn(jump)+'% 바뀐 11구간에는 간격이 '+k11.adj.toFixed(1)+'분으로 흔들렸지만, 다음 구간부터 난이도가 따라붙어 10분 근처로 돌아왔어요.':'조정이 없으면 30구간째 간격이 '+last.no.toFixed(1)+'분이에요. 계산력이 바뀐 만큼 간격도 그대로 바뀌어요.']);
    m.push(['a','난이도는 모든 채굴자에게 똑같이 올라요. 위조자의 계산력 몫은 그대로라서, 위조를 막는 일은 다음 칸의 확률 계산이 맡아요.']);ins($('#ins1'),m);drawA();drawB(0);}
  mod(c1b,drawB,true);addEventListener('resize',upd);upd();})();

/* ② 확정 깊이 */
(function(){var c2=$('#c2'),c2b=$('#c2b'),q=0.1,z=6,race=null,seed=1,t=0;
  slider('r2q',function(v){q=v/100;newRace();upd();});slider('r2z',function(v){z=v;newRace();upd();});
  $('#b2Race').addEventListener('click',function(){seed++;newRace();});
  function newRace(){var r=rng(300+seed),h=0,a=0,seq=[],won=false;for(var s=0;s<60;s++){if(r()<q)a++;else h++;seq.push([h,a]);if(h>=z&&a>h){won=true;break;}}race={seq:seq,won:won};t=0;}
  function drawA(){var W=fit(c2,240),H=240,x=c2.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var L=56,Rr=W-20,T=24,B=H-34,lo=-7;
    function X(zz){return L+(Rr-L)*zz/12}function Y(p){var lg=p<=0?lo:Math.max(lo,Math.log10(p));return T+(B-T)*(-lg)/(-lo)}
    for(var e=0;e>=lo;e--){txt(x,e===0?'1':'10'+(e<0?'⁻'+'⁰¹²³⁴⁵⁶⁷'[-e]:''),L-6,Y(Math.pow(10,e))+4,{a:'right',s:10,c:C.muted});x.strokeStyle='rgba(157,155,184,.12)';x.beginPath();x.moveTo(L,Y(Math.pow(10,e)));x.lineTo(Rr,Y(Math.pow(10,e)));x.stroke();}
    for(var zz=0;zz<=12;zz+=2)txt(x,'z='+zz,X(zz),H-14,{a:'center',s:10,c:C.muted});
    x.strokeStyle=C.amber;x.setLineDash([5,4]);x.beginPath();x.moveTo(L,Y(0.001));x.lineTo(Rr,Y(0.001));x.stroke();x.setLineDash([]);txt(x,'0.1%',Rr,Y(0.001)-5,{a:'right',s:10,c:C.amber});
    function curve(qq,col,w,a){x.globalAlpha=a;x.strokeStyle=col;x.lineWidth=w;x.beginPath();for(var k=0;k<=12;k++){var px=X(k),py=Y(attackerSuccess(qq,k));k?x.lineTo(px,py):x.moveTo(px,py);}x.stroke();x.lineWidth=1;x.globalAlpha=1;}
    curve(0.1,C.muted,1.5,0.6);curve(0.3,C.muted,1.5,0.6);txt(x,'q=0.1',X(12)-4,Y(attackerSuccess(0.1,12))-6,{a:'right',s:10,c:C.muted});txt(x,'q=0.3',X(12)-4,Y(attackerSuccess(0.3,12))-6,{a:'right',s:10,c:C.muted});
    curve(q,C.robo,3,1);
    WPT.forEach(function(w){x.strokeStyle=C.amber;x.lineWidth=2;x.beginPath();x.arc(X(w[1]),Y(w[2]),6,0,7);x.stroke();x.lineWidth=1;});txt(x,'○ 백서 표의 값',L+8,B-8,{s:11,c:C.amber});
    var P=attackerSuccess(q,z);x.fillStyle=C.robo;x.beginPath();x.arc(X(z),Y(P),5,0,7);x.fill();txt(x,sig(P),X(z)+8,Y(P)-8,{s:12,w:700});
    stamp(x,W,'백서 11절 식으로 계산');}
  function drawB(dt){t+=dt;var W=fit(c2b,170),H=170,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);if(!race)newRace();
    var n=race.seq.length,shown=REDUCE?n:Math.min(n,Math.floor(t*4)),st=shown?race.seq[shown-1]:[0,0],L=110,cw=Math.min(22,(W-L-30)/Math.max(14,z+6));
    [['정직한 사슬',st[0],C.gfp,50],['공격자 사슬',st[1],C.eye,104]].forEach(function(r){txt(x,r[0],12,r[3]+5,{s:12,w:700,c:r[2]});for(var i=0;i<r[1];i++){var X=L+i*cw;if(X>W-24){txt(x,'…',X,r[3]+5,{s:12});break;}x.fillStyle=r[2];rr(x,X,r[3]-8,cw-4,16,3);x.fill();}});
    var zx=L+z*cw-2;x.strokeStyle=C.amber;x.setLineDash([4,3]);x.beginPath();x.moveTo(zx,32);x.lineTo(zx,122);x.stroke();x.setLineDash([]);txt(x,'z = '+z+' (물건을 내주는 시점)',Math.min(zx+4,W-170),30,{s:11,c:C.amber});
    var msg=shown<n?'경주 중…':(race.won?'공격자가 따라잡음 → 송금이 지워진 사슬이 가장 긴 사슬이 됨':'격차가 벌어져 공격자가 포기 (60블록 안에 못 따라잡음)');
    txt(x,msg,12,H-12,{s:12,w:700,c:shown<n?C.muted:(race.won?C.eye:C.gfp)});stamp(x,W,'설명용 장면 · 무작위 한 번');}
  function upd(){var P=attackerSuccess(q,z),nz=needZ(q,0.001);
    kpis($('#k2'),[[sig(P),'공격 성공 확률 P(q='+q.toFixed(2)+', z='+z+')',P<0.001?'g':(P>=1?'r':'a')],[q<0.5?(q/(1-q)).toFixed(3):'≥ 1','q/p (공격자 대 정직한 쪽 속도 비)','m'],[isFinite(nz)?nz+'블록':'없음','0.1% 미만에 필요한 z',isFinite(nz)?'a':'r'],[(P*100).toPrecision(3)+'%','백분율로','m']]);
    $('#eq2').innerHTML='P = 1 − Σ<sub>k=0..'+z+'</sub> <em>e<sup>−λ</sup>λ<sup>k</sup>/k!</em> × (1 − (<i>q/p</i>)<sup>'+z+'−k</sup>), λ = <b>'+z+'</b> × '+(q<0.5?(q/(1-q)).toFixed(3):'—');
    var chk=WPT.map(function(w){var v=attackerSuccess(w[0],w[1]);return 'q='+w[0]+', z='+w[1]+': 계산 '+v.toFixed(7)+' / 백서 '+w[2].toFixed(7)+(Math.abs(v-w[2])<5e-8?' ✓':' ✗')}).concat(WPZ.map(function(w){var v=needZ(w[0],0.001);return 'q='+w[0].toFixed(2)+'의 필요 z: 계산 '+v+' / 백서 '+w[1]+(v===w[1]?' ✓':' ✗')}));
    var m=[];if(q>=0.5)m.push(['r','q가 0.5 이상이면 공격자가 정직한 쪽만큼 빠르거나 더 빨라요. 몇 블록을 기다려도 확률은 1이에요. 3장 「비트코인」의 51% 공격이에요.']);
    else m.push([P<0.001?'g':'a','공격자 몫 '+Math.round(q*100)+'%에서 '+z+'블록을 기다리면 성공 확률은 '+sig(P)+'. 0.1% 미만으로 낮추려면 '+nz+'블록이 필요해요.']);
    m.push(['m','백서 대조 — '+chk.join(' · ')]);ins($('#ins2'),m);drawA();}
  mod(c2b,drawB,true);addEventListener('resize',upd);newRace();upd();})();

Duel({names:{fly:'초파리 (6블록 확정)',robo:'주판봇 (1블록 확정)'},higherIsBetter:false,drawMargin:0,
  run:function(){return {fly:attackerSuccess(0.1,6),robo:attackerSuccess(0.1,1)};},bar:function(v){return Math.max(0.02,(Math.log10(v)+5)/5);},fmt:function(v){return v.toFixed(7);},
  lesson:'기다린 블록 수만큼 되돌려질 확률이 지수적으로 줄어든다',
  say:function(r){return '공격 성공 확률은 초파리 쪽 '+r.fly.toFixed(7)+', 주판봇 쪽 '+r.robo.toFixed(7)+'이에요. 백서 표와 같고, 약 '+fmt(r.robo/r.fly)+'배 차이예요. 막대는 로그 눈금이에요.';}});
}});
