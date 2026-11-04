LAB.start({anchor:'C',init:function(){
var HDR=80;
/* ① 묶기 */
(function(){var c1=$('#c1'),c1b=$('#c1b'),size=100,tx=250,T=1000,t=0,fill=0,chain=0,coins=[];
  slider('r1s',function(v){size=v;fill=0;chain=0;coins=[];upd();});slider('r1t',function(v){tx=v;upd();});
  function nb(){return Math.ceil(T/size);}
  function drawA(){var W=fit(c1,220),H=220,x=c1.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var B=nb(),hb=B*HDR,tb=T*tx,tot=hb+tb;
    var L=20,bw=W-40;txt(x,'총 저장량 '+fmt(tot)+'바이트',L,30,{w:700});x.fillStyle=C.info;rr(x,L,42,bw*tb/tot,26,5);x.fill();x.fillStyle=C.amber;rr(x,L+bw*tb/tot,42,Math.max(2,bw*hb/tot),26,5);x.fill();
    txt(x,'거래 '+fmt(tb),L,88,{s:12,c:C.info});txt(x,'머리글 '+fmt(hb)+' ('+(100*hb/tot).toFixed(1)+'%)',W-20,88,{a:'right',s:12,c:C.amber});
    var show=Math.min(B,200),cols=Math.min(50,show),cw=Math.min(16,(W-40)/50);for(var i=0;i<show;i++){var cx=L+(i%50)*cw,cy=110+Math.floor(i/50)*(cw+2);x.fillStyle='#efe6d2';x.fillRect(cx,cy,cw-2,cw-2);x.fillStyle=C.amber;x.fillRect(cx,cy,cw-2,3);}
    txt(x,'블록 '+fmt(B)+'개'+(B>200?' (200개까지만 표시)':''),L,H-10,{s:12,c:C.muted});stamp(x,W,'예시값');}
  function drawB(dt){t+=dt;var W=fit(c1b,190),H=190,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var cap=Math.min(size,24);
    if(dt>0&&Math.random()<dt*6)coins.push({x:20,y:40+Math.random()*60,p:0});
    var px=W*.55,py=30;coins.forEach(function(c){c.p+=dt*1.2;coin(x,c.x+(px-c.x)*c.p,c.y+(py+40-c.y)*c.p,6);if(c.p>=1){fill++;c.done=1;}});coins=coins.filter(function(c){return !c.done});
    if(REDUCE)fill=Math.floor(cap/2);
    if(fill>=cap){fill=0;chain=Math.min(chain+1,12);}
    x.fillStyle='#efe6d2';rr(x,px-40,py,80,100,6);x.fill();x.fillStyle=C.amber;x.fillRect(px-40,py,80,12);
    for(var i=0;i<fill;i++){x.fillStyle='#3a3040';x.fillRect(px-32+(i%4)*17,py+20+Math.floor(i/4)*12,13,6);}
    txt(x,'담는 중 '+fill+'/'+size+(size>24?' (그림은 24칸까지)':''),px,py+118,{a:'center',s:11});
    for(var j=0;j<chain;j++){var bx=20+j*((W-40)/12),by=H-36;x.fillStyle='#efe6d2';rr(x,bx,by,(W-40)/12-8,24,4);x.fill();x.fillStyle=C.amber;x.fillRect(bx,by,(W-40)/12-8,5);if(j>0){x.strokeStyle=C.gfp;x.beginPath();x.moveTo(bx-8,by+12);x.lineTo(bx,by+12);x.stroke();}}
    txt(x,'봉인된 블록',20,H-44,{s:11,c:C.muted});stamp(x,W,'설명용 장면');}
  function upd(){var B=nb(),hb=B*HDR,tot=hb+T*tx;
    kpis($('#k1'),[[fmt(B)+'개','블록 수 (거래 1,000건)','a'],[fmt(hb)+'B','머리글 총량 (80바이트 × 블록 수)','m'],[(100*hb/tot).toFixed(1)+'%','머리글이 차지하는 몫',hb/tot>0.1?'r':'g'],[fmt(tot)+'B','총 저장량','a']]);
    $('#eq1').innerHTML='총 저장량 = ⌈1000 ÷ <b>'+size+'</b>⌉ × <i>80</i> + 1000 × <em>'+tx+'</em> = <b>'+fmt(tot)+'</b>바이트';
    ins($('#ins1'),[[hb/tot>0.1?'r':'g','블록 하나에 '+size+'건씩이면 블록 '+fmt(B)+'개, 머리글이 전체의 '+(100*hb/tot).toFixed(1)+'%를 차지해요.'],['a','묶을수록 머리글 몫은 줄지만, 블록 하나가 커지면 퍼뜨리고 검증하는 데 시간이 더 걸려요.']]);drawA();}
  mod(c1b,drawB,true);addEventListener('resize',drawA);upd();})();

/* ② 잇기 */
(function(){var c2=$('#c2'),c2b=$('#c2b'),mode='sum',target=2,edit=false,smart=false,red=1;
  var BASE=[[3000,5000,7000],[2000,4000,9000],[1000,6000,8000],[5000,5000,2000],[4000,3000,6000]];
  slider('r2b',function(v){target=v;red=0;upd();});
  $$('#lv2 [data-sum]').forEach(function(b){b.addEventListener('click',function(){mode=b.dataset.sum;press('#lv2 [data-sum]',b);red=0;upd();});});
  $('#b2Edit').addEventListener('click',function(){edit=!edit;if(edit){smart=false;$('#b2Smart').setAttribute('aria-pressed',false);}this.setAttribute('aria-pressed',edit);red=0;upd();});
  $('#b2Smart').addEventListener('click',function(){smart=!smart;if(smart){edit=false;$('#b2Edit').setAttribute('aria-pressed',false);}this.setAttribute('aria-pressed',smart);red=0;upd();});
  function summ(b){return mode==='sum'?String(b.reduce(function(a,c){return a+c},0)):b.join('+');}
  function state(){var orig=BASE.map(function(b){return b.slice()}),cur=BASE.map(function(b){return b.slice()}),j=target-1;
    if(edit)cur[j][0]+=5000;if(smart){cur[j][0]+=2000;cur[j][1]-=2000;}
    var stored=[null];for(var i=1;i<5;i++)stored.push(summ(orig[i-1]));
    // 위조자는 고친 블록만 바꿨다. 다음 블록에 적힌 요약은 그대로
    var bad=[];for(i=1;i<5;i++)if(summ(cur[i-1])!==stored[i])bad.push(i+1);
    var copyLen=0;for(i=0;i<4;i++)copyLen+=3;return {cur:cur,stored:stored,bad:bad,copyLen:copyLen};}
  function drawA(){var W=fit(c2,220),H=220,x=c2.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var s=state(),bw=(W-40)/5-10;
    s.cur.forEach(function(b,i){var X=20+i*(bw+10),Y=50,isT=(edit||smart)&&i===target-1,isB=s.bad.indexOf(i+1)>=0;
      x.fillStyle=isB?'rgba(240,96,77,.18)':'#efe6d2';rr(x,X,Y,bw,140,6);x.fill();x.fillStyle=isB?C.eye:C.amber;x.fillRect(X,Y,bw,22);
      txt(x,i?'앞: '+(mode==='sum'?s.stored[i]:'거래 '+(i*3)+'건'):'첫 블록',X+bw/2,Y+15,{a:'center',s:11,w:700,c:'#13141f'});
      txt(x,'블록 '+(i+1),X+bw/2,Y-8,{a:'center',w:700});b.forEach(function(v,k){txt(x,fmt(v)+'원',X+10,Y+46+k*22,{s:13,c:isT&&(k===0||(smart&&k===1))?'#c0301f':'#3a3040'});});
      txt(x,'합계 '+fmt(b.reduce(function(a,c){return a+c},0)),X+10,Y+128,{s:11,c:'#6a5a50'});
      if(i<4){x.strokeStyle=s.bad.indexOf(i+2)>=0?C.eye:C.gfp;x.lineWidth=3;x.beginPath();x.moveTo(X+bw,Y+70);x.lineTo(X+bw+10,Y+70);x.stroke();x.lineWidth=1;}});
    stamp(x,W,'설명용 장난감');}
  function drawB(dt){red=Math.min(1,red+dt*1.5);if(REDUCE)red=1;var W=fit(c2b,140),H=140,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var s=state(),bw=(W-60)/5;
    for(var i=0;i<5;i++){var X=20+i*(bw+5),bad=s.bad.indexOf(i+1)>=0,lit=bad&&red>=(i-target)/4;x.fillStyle=lit?'rgba(240,96,77,.3)':'rgba(94,227,156,.14)';x.strokeStyle=lit?C.eye:C.gfp;rr(x,X,40,bw-10,50,8);x.fill();x.stroke();txt(x,'블록 '+(i+1),X+(bw-10)/2,70,{a:'center',w:700});}
    txt(x,s.bad.length?'연결이 어긋난 블록: '+s.bad.join('·')+'번 — 숨기려면 그 뒤를 전부 고쳐야 한다':(edit||smart)?'위조가 요약에 걸리지 않았다':'모든 연결 정상',20,H-14,{s:12,w:700,c:s.bad.length?C.eye:(edit||smart)?C.amber:C.gfp});stamp(x,W,'설명용 장난감');}
  function upd(){var s=state();
    kpis($('#k2'),[[s.bad.length?s.bad.join('·')+'번':'없음','앞 블록 요약과 어긋난 블록',s.bad.length?'r':((edit||smart)?'r':'g')],[(edit||smart)?(s.bad.length?'드러남':'숨겨짐'):'—','위조',(edit||smart)?(s.bad.length?'g':'r'):'a'],[mode==='sum'?'숫자 하나':'거래 '+s.copyLen+'건','5번 블록 머리글에 적을 양',mode==='sum'?'g':'r'],[mode==='sum'?'합계':'전체 복사','요약 방식','m']]);
    $('#eq2').innerHTML='검사: 요약(<b>지금의 블록 n−1</b>) = <em>블록 n에 적힌 요약</em> · 방식 <i>'+(mode==='sum'?'합계':'전체 복사')+'</i>';
    var m=[];if(smart&&mode==='sum')m.push(['r','합계가 같게 두 건을 맞바꾸자 요약이 그대로라 위조가 숨겨졌어요. 합계는 너무 둔한 요약이에요.']);
    else if((edit||smart)&&s.bad.length)m.push(['g','고친 블록 바로 뒤('+s.bad.join('·')+'번)에서 어긋남이 드러났어요.']);
    if(mode==='list')m.push(['a','전부 옮겨 적으면 어떤 위조도 드러나지만, 5번 블록 머리글에는 앞 블록 거래 '+s.copyLen+'건이 들어가요. 블록이 쌓일수록 끝없이 길어져요.']);
    if(!m.length)m.push(['g','지금은 모든 연결이 맞아요. 금액을 고쳐 보세요.']);ins($('#ins2'),m);drawA();drawB(0);}
  mod(c2b,drawB,true);addEventListener('resize',upd);upd();})();

function bytes(perBlock){return Math.ceil(1000/perBlock)*HDR+1000*250;}
Duel({names:{fly:'초파리 (1건씩)',robo:'주판봇 (100건씩)'},higherIsBetter:false,drawMargin:0,
  run:function(){return {fly:bytes(1),robo:bytes(100)};},bar:function(v){return v/1e6;},fmt:function(v){return fmt(v)+'B';},
  lesson:'묶으면 머리글 하나로 여러 거래를 지킨다',
  say:function(r){return '총 저장량은 초파리 쪽 '+fmt(r.fly)+'바이트, 주판봇 쪽 '+fmt(r.robo)+'바이트예요. 차이 '+fmt(r.fly-r.robo)+'바이트는 전부 머리글이에요(990개 × 80바이트).';}});
}});
