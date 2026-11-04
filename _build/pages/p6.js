LAB.start({anchor:'C',init:function(){
/* ① 작업증명 */
(function(){var BASE='블록 3|A가 B에게 10,000원을 보냈다|논스 ',S={d:3,n:0,run:false,found:null,h:''},RES={},c1b=$('#c1b');
  slider('r1d',function(v){S.d=v;reset();});
  $('#b1Mine').addEventListener('click',function(){if(S.found)reset();S.run=!S.run;this.textContent=S.run?'❚❚ 멈춤':'▶ 채굴 시작';upd();});
  $('#b1Reset').addEventListener('click',reset);
  function reset(){S.n=0;S.run=false;S.found=null;S.h='';$('#b1Mine').textContent='▶ 채굴 시작';upd();}
  function step(){if(!S.run)return;var z='0'.repeat(S.d),t0=performance.now();
    while(performance.now()-t0<10){var h=SHA256(BASE+S.n);S.h=h;if(h.slice(0,S.d)===z){S.found={n:S.n,h:h,tries:S.n+1};RES[S.d]=S.n+1;S.run=false;$('#b1Mine').textContent='▶ 다시 채굴';break;}S.n++;}upd();}
  function drawB(){var W=fit(c1b,210),H=210,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    var L=170,bw=W-L-110,lmax=Math.log10(65536*6);function bl(v){return Math.max(2,bw*Math.log10(Math.max(1,v))/lmax)}
    var tries=S.found?S.found.tries:S.n,exp=Math.pow(16,S.d),rows=[['찾는 데 든 계산',tries,C.amber],['평균 기대 (16^'+S.d+')',exp,C.stain],['확인하는 데 든 계산',1,C.gfp],['위조: 블록 하나 + 뒤 5개',exp*6,C.eye]];
    rows.forEach(function(r,i){var y=22+i*44;txt(x,r[0],12,y+16,{s:12});x.fillStyle=r[2];rr(x,L,y,bl(r[1]),22,5);x.fill();txt(x,fmt(r[1])+'번',L+bl(r[1])+8,y+16,{s:12,w:700});});
    txt(x,'(로그 눈금)',W-12,H-8,{a:'right',s:10,c:C.muted});stamp(x,W,'실제 SHA-256 · 블록 구성은 단순화');}
  function upd(){var exp=Math.pow(16,S.d),h=S.found?S.found.h:S.h;$('#m1data').textContent=BASE+(S.found?S.found.n:S.n);
    $('#m1hash').innerHTML=h?(S.found?'<mark style="background:rgba(94,227,156,.3);color:#c9ffe0">'+h.slice(0,S.d)+'</mark>'+h.slice(S.d):h):'—';
    kpis($('#k1'),[[S.d+'개','앞자리 0 (난이도)','a'],[fmt(S.found?S.found.tries:S.n),'지금까지 시도',S.found?'g':'m'],[fmt(exp),'평균 기대 시도 16^d','m'],[S.found?'1번':'—','찾은 답 확인에 든 계산','g']]);
    $('#eq1').innerHTML='찾기: SHA-256(<em>블록 내용</em> | <b>논스</b>)의 앞 <i>'+S.d+'</i>자리 = 0 → 평균 <b>16<sup>'+S.d+'</sup> = '+fmt(exp)+'</b>번 · 확인: <b>1</b>번';
    var m=[];if(S.found){var r=S.found.tries/exp;m.push(['g','논스 '+fmt(S.found.n)+'에서 찾았어요. '+fmt(S.found.tries)+'번 시도, 평균 '+fmt(exp)+'번의 '+(r<1?'약 '+Math.round(r*100)+'%로 운이 좋았어요':'약 '+r.toFixed(1)+'배로 운이 나빴어요')+'. 확인은 한 번이면 돼요.']);
      m.push(['a','2-03처럼 블록 하나를 고치면 그 블록과 뒤 블록 5개를 모두 다시 채굴해야 해요(평균 '+fmt(exp*6)+'번).']);}
    else if(S.run)m.push(['m','논스를 0부터 하나씩 올리며 계산 중… 해시를 미리 알 방법이 없어 하나씩 해 보는 수밖에 없어요.']);
    else m.push(['a','"채굴 시작"을 눌러 보세요. 난이도를 1씩 올리면 평균 시도가 16배씩 늘어나요. (난이도 5는 브라우저에서 수십 초가 걸려 뺐어요.)']);
    var done=Object.keys(RES).map(function(k){return '난이도 '+k+': '+fmt(RES[k])+'번'}).join(' · ');if(done)m.push(['m','지금까지 기록 — '+done]);ins($('#ins1'),m);drawB();}
  addMod(c1b,step);addEventListener('resize',drawB);upd();})();

/* ② 채굴 경주 */
function race(shares,blocks,seed){var r=rng(seed),tot=shares.reduce(function(a,b){return a+b},0),wins=shares.map(function(){return 0}),seq=[];
  for(var b=0;b<blocks;b++){var u=r()*tot,acc=0;for(var i=0;i<shares.length;i++){acc+=shares[i];if(u<acc){wins[i]++;seq.push(i);break;}}}return {wins:wins,seq:seq};}
(function(){var c2=$('#c2'),c2b=$('#c2b'),robo=4,other=1,res=null,t=0,NM=['초파리','주판봇','채굴자 C','채굴자 D'],COL=[C.fly,C.robo,C.info,C.stain];
  function shares(){return [1,robo,other,other];}
  slider('r2r',function(v){robo=v;res=null;upd();});slider('r2o',function(v){other=v;res=null;upd();});
  $('#b2Run').addEventListener('click',function(){res=race(shares(),100,26);t=0;upd();});
  function drawA(){var W=fit(c2,220),H=220,x=c2.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var s=shares(),tot=s.reduce(function(a,b){return a+b},0),L=110,bw=(W-L-130)/2;
    txt(x,'계산력 몫',L,24,{s:12,c:C.muted});txt(x,'만든 블록 (100개 중)',L+bw+30,24,{s:12,c:C.muted});
    NM.forEach(function(n,i){var y=38+i*42;txt(x,n,12,y+16,{w:700,s:13,c:COL[i]});x.fillStyle=COL[i];x.globalAlpha=s[i]?1:0.2;rr(x,L,y,Math.max(2,bw*s[i]/tot),20,4);x.fill();x.globalAlpha=1;
      txt(x,(100*s[i]/tot).toFixed(0)+'%',L+Math.max(2,bw*s[i]/tot)+6,y+15,{s:12});
      if(res){x.fillStyle=COL[i];rr(x,L+bw+30,y,Math.max(2,bw*res.wins[i]/100),20,4);x.fill();txt(x,res.wins[i]+'개',L+bw+30+Math.max(2,bw*res.wins[i]/100)+6,y+15,{s:12,w:700});}});
    stamp(x,W,'예시값 · 시드 26');}
  function drawB(dt){t+=dt;var W=fit(c2b,170),H=170,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var shown=res?Math.min(100,REDUCE?100:Math.floor(t*25)):0,cnt=[0,0,0,0];
    if(res)for(var b=0;b<shown;b++)cnt[res.seq[b]]++;
    NM.forEach(function(n,i){var X=50+i*(W-100)/3;txt(x,n,X,H-12,{a:'center',s:12,c:COL[i],w:700});for(var k=0;k<cnt[i];k++){var col=k%5,row=Math.floor(k/5);if(row<12)coin(x,X-20+col*10,H-34-row*9,4);}txt(x,cnt[i]+'',X+34,H-34,{s:12,w:700});});
    txt(x,res?'블록 '+shown+'/100':'"블록 100개 경주"를 눌러 보세요',12,20,{s:12,c:C.muted});stamp(x,W,'설명용 장면');}
  function upd(){var s=shares(),tot=s.reduce(function(a,b){return a+b},0);
    kpis($('#k2'),[[(100*robo/tot).toFixed(0)+'%','주판봇 계산력 몫','a'],[res?res.wins[1]+'개':'—','주판봇이 만든 블록','m'],[(100/tot).toFixed(0)+'%','초파리 계산력 몫','a'],[res?res.wins[0]+'개':'—','초파리가 만든 블록','m']]);
    $('#eq2').innerHTML='블록을 먼저 찾을 확률(i) = <b>계산력(i)</b> ÷ <em>전체 계산력 '+tot+'</em> · 보상: 블록마다 첫 거래로 <i>새 코인</i>';
    var m=[];if(res)m.push(['g','블록 100개 중 주판봇 '+res.wins[1]+'개, 초파리 '+res.wins[0]+'개. 계산력 몫('+(100*robo/tot).toFixed(0)+'% : '+(100/tot).toFixed(0)+'%)과 비슷하게 나뉘었어요.']);
    m.push([robo/tot>0.5?'r':'a',robo/tot>0.5?'주판봇의 계산력 몫이 50%를 넘었어요. 이 상태라면 위조 사슬을 정직한 사슬보다 빨리 늘릴 수도 있어요(2-07, 3장의 51% 공격).':'계산력이 여러 채굴자에게 나뉘어 있으면 한 명이 사슬을 마음대로 바꾸기 어려워요.']);ins($('#ins2'),m);drawA();drawB(0);}
  mod(c2b,drawB,true);addEventListener('resize',upd);upd();})();

Duel({names:{fly:'초파리 (장비 1대)',robo:'주판봇 (장비 4대)'},higherIsBetter:true,drawMargin:0,
  run:function(){var r=race([1,4],100,206);return {fly:r.wins[0],robo:r.wins[1]};},bar:function(v){return v/100;},fmt:function(v){return v+'블록';},
  lesson:'계산력이 많은 쪽이 블록을 더 자주 만든다. 비트코인의 한 표는 계산력이다',
  say:function(r){return '블록 100개 중 초파리 쪽 '+r.fly+'개, 주판봇 쪽 '+r.robo+'개예요. 계산력 몫 20% 대 80%와 비슷해요. 시드 206으로 고정했어요.';}});
}});
