LAB.start({anchor:'C',init:function(){
var DATA=['창세 블록','A → B 10,000원','B → C 3,000원','C → A 2,000원','A → D 7,000원','D → B 1,000원'];
function H(b){return SHA256(b.n+'|'+b.d+'|'+b.prev);}
function make(){var B=[],p='0'.repeat(64);DATA.forEach(function(d,i){var b={n:i+1,d:d,prev:p};b.stored=H(b);B.push(b);p=b.stored;});return B;}
function check(B){var ok=0,bad=[];B.forEach(function(b,i){b.actual=H(b);b.selfBad=b.actual!==b.stored;b.linkBad=i>0&&b.prev!==B[i-1].actual;if(b.selfBad||b.linkBad)bad.push(b.n);else ok++;});return {ok:ok,bad:bad};}
function tamper(B,j){B[j-1].d=B[j-1].d.replace(/[\d,]+원/,function(m){return '9'+m;});}
function recompute(B){var n=0;for(var i=0;i<B.length;i++){if(i>0)B[i].prev=B[i-1].stored;var a=H(B[i]);if(a!==B[i].stored){B[i].stored=a;n++;}}return n;}
function forged(){var B=make();tamper(B,2);recompute(B);return B;}

/* ① 사슬 */
(function(){var B=make(),j=2,tam=false,fixed=0,red=1,c1b=$('#c1b');
  slider('r1b',function(v){j=v;B=make();tam=false;fixed=0;$('#b1Tamper').setAttribute('aria-pressed',false);upd();});
  $('#b1Tamper').addEventListener('click',function(){tam=!tam;B=make();if(tam)tamper(B,j);fixed=0;red=0;this.setAttribute('aria-pressed',tam);upd();});
  $('#b1Fix').addEventListener('click',function(){fixed=recompute(B);red=0;upd();});
  $('#b1Reset').addEventListener('click',function(){B=make();tam=false;fixed=0;$('#b1Tamper').setAttribute('aria-pressed',false);upd();});
  function html(){var r=check(B);$('#chain1').innerHTML=B.map(function(b){var bad=b.selfBad||b.linkBad;return '<div class="blk'+(bad?' bad':'')+'"><b>블록 '+b.n+'</b> '+(bad?'<span style="color:#ff8f80">✗</span>':'<span style="color:var(--gfp)">✓</span>')+
    '<div>거래: '+b.d+'</div><div class="h'+(b.linkBad?' bad':'')+'">이전 해시: '+b.prev.slice(0,12)+'…'+(b.linkBad?' (앞과 다름)':'')+'</div><div class="h'+(b.selfBad?' bad':'')+'">적힌 해시: '+b.stored.slice(0,12)+'…'+(b.selfBad?'<br>실제: '+b.actual.slice(0,12)+'…':'')+'</div></div>';}).join('');$('#chain1').style.gridTemplateColumns='repeat(6,minmax(170px,1fr))';return r;}
  function drawB(dt){red=Math.min(1,red+dt*1.5);if(REDUCE)red=1;var W=fit(c1b,150),H=150,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);check(B);var bw=(W-60)/6,bh=60;
    B.forEach(function(b,i){var X=20+i*(bw+4),Y=40,bad=b.selfBad||b.linkBad;if(i>0){x.strokeStyle=b.linkBad&&red>0.3?C.eye:C.gfp;x.lineWidth=3;x.beginPath();x.moveTo(X-6,Y+bh/2);x.lineTo(X+2,Y+bh/2);x.stroke();x.lineWidth=1;}
      x.fillStyle=bad?'rgba(240,96,77,.25)':'rgba(94,227,156,.14)';x.strokeStyle=bad?C.eye:C.gfp;rr(x,X,Y,bw-4,bh,8);x.fill();x.stroke();txt(x,'블록 '+b.n,X+(bw-4)/2,Y+24,{a:'center',w:700});txt(x,b.stored.slice(0,8)+'…',X+(bw-4)/2,Y+44,{a:'center',s:11,c:C.muted});});
    txt(x,'초록 = 앞 블록 해시와 일치, 빨강 = 불일치',20,H-12,{s:12,c:C.muted});stamp(x,W,'실제 SHA-256 · 블록 구성은 단순화');}
  function upd(){var r=html();kpis($('#k1'),[['64자','이전 해시 길이 (블록 수와 무관)','a'],[r.bad.length?r.bad.join('·')+'번':'없음','검사에 걸린 블록',r.bad.length?'r':'g'],[r.ok+'/6','검사 통과 블록',r.ok===6?'g':'r'],[fixed+'개','방금 다시 계산한 블록','m']]);
    $('#eq1').innerHTML='h<sub>n</sub> = SHA-256( <b>n</b> | <em>거래<sub>n</sub></em> | <i>h<sub>n−1</sub></i> ) · 검사: 적힌 해시 = 실제 해시, 이전 해시 = 앞 블록 실제 해시';
    var m=[];if(r.bad.length)m.push(['r',r.bad.join('·')+'번 블록이 걸렸어요. 고친 블록은 해시가 달라지고, 바로 뒤 블록은 적어 둔 이전 해시가 맞지 않아요.']);
    else if(fixed)m.push(['a','뒤 블록 '+fixed+'개를 다시 계산하자 사슬이 다시 전부 초록이 됐어요. 사슬 혼자서는 이 위조를 가려내지 못해요.']);
    else m.push(['g','사슬이 정상이에요. 블록을 골라 금액을 고쳐 보세요.']);ins($('#ins1'),m);drawB(0);}
  mod(c1b,drawB,true);addEventListener('resize',function(){drawB(0)});upd();})();

/* ② 사본 대조 */
function tips(k,on){var good=make()[5].stored,bad=forged()[5].stored,L=[];for(var i=0;i<9;i++)L.push(on&&i<k?bad:good);return {L:L,good:good,bad:bad};}
function majority(L){var c={};L.forEach(function(t){c[t]=(c[t]||0)+1;});var best=null;Object.keys(c).forEach(function(t){if(!best||c[t]>c[best])best=t;});return {tip:best,count:c[best]};}
(function(){var c2=$('#c2'),c2b=$('#c2b'),k=1,on=true,t=0;
  slider('r2k',function(v){k=v;upd();});
  $('#b2Rew').addEventListener('click',function(){on=!on;this.setAttribute('aria-pressed',on);upd();});
  function drawA(){var W=fit(c2,210),H=210,x=c2.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var T=tips(k,on),M=majority(T.L),cw=(W-40)/9;
    T.L.forEach(function(tip,i){var X=20+i*cw,isBad=tip===T.bad;ledgerIcon(x,X+cw/2-22,58,44,30,isBad?'#f3c2bb':'#c9f5dc');txt(x,'노드 '+(i+1),X+cw/2,50,{a:'center',s:11,c:C.muted});
      txt(x,tip.slice(0,8),X+cw/2,114,{a:'center',s:12,w:700,c:isBad?C.eye:C.gfp});txt(x,tip===M.tip?'다수':'소수',X+cw/2,136,{a:'center',s:11,c:tip===M.tip?C.gfp:C.eye});});
    txt(x,'다수 끝 해시: '+M.tip.slice(0,16)+'… ('+M.count+'/9) → '+(M.tip===T.good?'원본 사슬':'위조 사슬'),20,H-20,{w:700,c:M.tip===T.good?C.gfp:C.eye});stamp(x,W,'실제 SHA-256 · 노드 9개 모형');}
  function drawB(dt){t+=dt;var W=fit(c2b,160),H=160,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var T=tips(k,on),ph=REDUCE?1:Math.min(1,(t%4)/2);
    T.L.forEach(function(tip,i){var sx=20+i*(W-60)/8,tx=tip===T.good?W*.3:W*.75,X=sx+(tx-sx)*ph+(i%3)*6,Y=40+(1-ph)*0+(i%4)*14;x.fillStyle=tip===T.good?'rgba(94,227,156,.8)':'rgba(240,96,77,.8)';rr(x,X,Y,40,14,3);x.fill();txt(x,tip.slice(0,4),X+20,Y+11,{a:'center',s:10,c:'#13141f',w:700});});
    if(ph>=1){txt(x,'원본 끝 해시 '+T.L.filter(function(s){return s===T.good}).length+'개',W*.3+20,H-14,{a:'center',w:700,c:C.gfp});txt(x,'위조 끝 해시 '+T.L.filter(function(s){return s===T.bad}).length+'개',W*.75+20,H-14,{a:'center',w:700,c:C.eye});}stamp(x,W,'설명용 장면');}
  function upd(){var T=tips(k,on),M=majority(T.L),fr=check(forged());
    kpis($('#k2'),[[on?fr.ok+'/6':'—','위조 사슬의 자기 검사 통과','a'],[on?k+'/9':'0/9','위조 끝 해시를 가진 노드',on&&k>4?'r':'m'],[M.tip===T.good?'원본':'위조','다수가 인정한 사슬',M.tip===T.good?'g':'r'],['64자','대조에 쓰는 길이','g']]);
    $('#eq2').innerHTML='인정 = <b>끝 해시</b>가 다수(<em>'+M.count+'/9</em>)와 같은 사슬 · 위조 끝 해시 <i>'+T.bad.slice(0,8)+'</i> vs 원본 <b>'+T.good.slice(0,8)+'</b>';
    var m=[];if(!on)m.push(['g','위조가 없으면 아홉 사본의 끝 해시가 모두 같아요.']);
    else if(M.tip===T.good)m.push(['g','위조 사슬은 스스로는 6블록 모두 통과했지만, 끝 해시가 다수 사본과 달라 걸러졌어요.']);
    else m.push(['r','위조자가 사본 '+k+'개를 함께 고쳐 위조가 다수가 됐어요. 해시 다시 계산이 공짜라 생기는 문제예요(1-07의 과반 문제).']);ins($('#ins2'),m);drawA();drawB(0);}
  mod(c2b,drawB,true);addEventListener('resize',upd);upd();})();

Duel({names:{fly:'초파리 (원본)',robo:'Money-Robo (재계산 위조)'},higherIsBetter:true,drawMargin:0,
  run:function(){var o=check(make()),f=check(forged()),T=tips(1,true),M=majority(T.L);return {fly:o.ok,robo:f.ok,foul:forged()[5].stored!==M.tip};},
  bar:function(v){return v/6;},fmt:function(v){return v+'/6블록';},
  lesson:'검사 통과가 아니라 다수 사본과 같은 사슬이 진짜다',foulRule:'"망의 다수 사본과 같은 사슬만 인정한다"는 규칙',
  say:function(r){return '내부 검사 통과는 초파리 쪽 '+r.fly+'블록, Money-Robo 쪽 '+r.robo+'블록으로 같아요. 하지만 Money-Robo 사슬의 끝 해시는 아홉 사본 중 여덟과 달라요. 2번 블록을 고친 사슬이에요.';}});
}});
