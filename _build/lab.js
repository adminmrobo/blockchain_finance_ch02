/* 연구실 해설 대시보드 공용 스크립트 (ai-lab-explainer v1.7 기반) — 블록체인 편 */
/* ===== 도우미 ===== */
function rng(a){return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
function fit(c,h){var d=window.devicePixelRatio||1,w=c.clientWidth||c.parentElement.clientWidth||600;
  if(c.width!==Math.round(w*d)||c.height!==Math.round(h*d)){c.width=Math.round(w*d);c.height=Math.round(h*d);c.style.height=h+'px';}
  var x=c.getContext('2d');x.setTransform(d,0,0,d,0,0);return w;}
function $(s,r){return (r||document).querySelector(s)}
function $$(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))}
function fmt(n){return Math.round(n).toLocaleString('ko-KR')}
var FONT='"IBM Plex Sans KR","Apple SD Gothic Neo","Malgun Gothic",system-ui,sans-serif';
var C={bg:'#161826',panel:'#1c1e2d',panel2:'#25283a',rule:'#363a52',text:'#eceaf3',muted:'#9d9bb8',stain:'#d672d6',gfp:'#5ee39c',eye:'#f0604d',amber:'#f1b646',info:'#82b8ff',accent:'#c48a5a',fly:'#ef5b5b',robo:'#57d0dc'};
var REDUCE=matchMedia('(prefers-reduced-motion: reduce)').matches;
function rr(x,X,Y,W,H,R){x.beginPath();if(x.roundRect)x.roundRect(X,Y,W,H,R);else x.rect(X,Y,W,H);}
function txt(x,s,X,Y,o){o=o||{};x.save();x.font=(o.w||500)+' '+(o.s||13)+'px '+FONT;x.fillStyle=o.c||C.text;x.textAlign=o.a||'left';x.textBaseline=o.b||'alphabetic';x.fillText(s,X,Y);x.restore();}
function grid(x,W,H){x.save();x.strokeStyle='rgba(157,155,184,.06)';x.lineWidth=1;for(var i=0;i<W;i+=24){x.beginPath();x.moveTo(i+.5,0);x.lineTo(i+.5,H);x.stroke();}for(var j=0;j<H;j+=24){x.beginPath();x.moveTo(0,j+.5);x.lineTo(W,j+.5);x.stroke();}x.restore();}
function stamp(ctx,W,t){ctx.save();ctx.font='700 11px '+FONT;var tw=ctx.measureText(t).width+16,x=W-tw-8,y=8;
  ctx.fillStyle='rgba(241,182,70,.14)';ctx.strokeStyle='rgba(241,182,70,.7)';rr(ctx,x,y,tw,20,10);ctx.fill();ctx.stroke();
  ctx.fillStyle='#f1b646';ctx.textAlign='left';ctx.fillText(t,x+8,y+14);ctx.restore();}
function kpis(el,arr){el.innerHTML=arr.map(function(k){return '<div class="kpi '+(k[2]||'')+'"><b>'+k[0]+'</b><span>'+k[1]+'</span></div>'}).join('');}
function ins(el,arr){el.innerHTML=arr.map(function(p){return '<p class="'+p[0]+'">'+p[1]+'</p>'}).join('');}
function press(group,btn){$$(group).forEach(function(x){x.setAttribute('aria-pressed',x===btn)});}
function slider(id,cb,fmtv){var el=$('#'+id),v=$('#'+id.replace(/^r/,'v'));function f(){if(v)v.textContent=fmtv?fmtv(+el.value):el.value;cb(+el.value);}el.addEventListener('input',f);if(v)v.textContent=fmtv?fmtv(+el.value):el.value;return el;}

/* ===== SHA-256 (외부 라이브러리 없이) ===== */
var SHA256=(function(){var K=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
var W=new Int32Array(64), enc=new TextEncoder();
function hex(n){return ('0000000'+(n>>>0).toString(16)).slice(-8);}
return function(str){var m=enc.encode(str), l=m.length, n=((l+9+63)>>6)<<6, b=new Uint8Array(n);
 b.set(m); b[l]=0x80; var bits=l*8; b[n-4]=(bits>>>24)&255; b[n-3]=(bits>>>16)&255; b[n-2]=(bits>>>8)&255; b[n-1]=bits&255;
 if(l>=0x20000000){var hi=Math.floor(l/0x20000000); b[n-8]=(hi>>>24)&255;b[n-7]=(hi>>>16)&255;b[n-6]=(hi>>>8)&255;b[n-5]=hi&255;}
 var h0=0x6a09e667,h1=0xbb67ae85,h2=0x3c6ef372,h3=0xa54ff53a,h4=0x510e527f,h5=0x9b05688c,h6=0x1f83d9ab,h7=0x5be0cd19;
 for(var o=0;o<n;o+=64){for(var i=0;i<16;i++)W[i]=(b[o+4*i]<<24)|(b[o+4*i+1]<<16)|(b[o+4*i+2]<<8)|b[o+4*i+3];
  for(i=16;i<64;i++){var x=W[i-15],y=W[i-2];var s0=((x>>>7)|(x<<25))^((x>>>18)|(x<<14))^(x>>>3);var s1=((y>>>17)|(y<<15))^((y>>>19)|(y<<13))^(y>>>10);W[i]=(W[i-16]+s0+W[i-7]+s1)|0;}
  var a=h0,c=h2,d=h3,e=h4,f=h5,g=h6,h=h7,bb=h1;
  for(i=0;i<64;i++){var S1=((e>>>6)|(e<<26))^((e>>>11)|(e<<21))^((e>>>25)|(e<<7));var ch=(e&f)^(~e&g);var t1=(h+S1+ch+K[i]+W[i])|0;
   var S0=((a>>>2)|(a<<30))^((a>>>13)|(a<<19))^((a>>>22)|(a<<10));var mj=(a&bb)^(a&c)^(bb&c);var t2=(S0+mj)|0;
   h=g;g=f;f=e;e=(d+t1)|0;d=c;c=bb;bb=a;a=(t1+t2)|0;}
  h0=(h0+a)|0;h1=(h1+bb)|0;h2=(h2+c)|0;h3=(h3+d)|0;h4=(h4+e)|0;h5=(h5+f)|0;h6=(h6+g)|0;h7=(h7+h)|0;}
 return hex(h0)+hex(h1)+hex(h2)+hex(h3)+hex(h4)+hex(h5)+hex(h6)+hex(h7);};})();


/* ===== 보이는 캔버스만 그리는 루프 ===== */
var mods=[],vis=new Set(),io=new IntersectionObserver(function(es){es.forEach(function(e){e.isIntersecting?vis.add(e.target):vis.delete(e.target);});},{rootMargin:'100px'});
function addMod(el,fn){mods.push({el:el,fn:fn});io.observe(el);}
var last=0;function loop(ts){var dt=last?Math.min(0.05,(ts-last)/1000):0.016;last=ts;mods.forEach(function(m){if(vis.has(m.el))m.fn(REDUCE?0:dt);});requestAnimationFrame(loop);}
/* 모듈 등록: draw(dt) 를 resize·첫 로드에 dt=0 으로 부른다 */
function mod(canvas,draw,animate){if(animate)addMod(canvas,draw);addEventListener('resize',function(){draw(0)});return draw;}

/* ===== 픽셀 지도 (부록 A: 행동 캔버스의 작은 캐릭터) ===== */
var PAL={K:'#1d1a22',W:'#eceaf3',R:'#e04a3a',r:'#a8281c',U:'#23467e',Y:'#f1c84a',L:'#5a4636',S:'rgba(0,0,0,.35)',B:'#3fb8f0',F:'#f6d3b8',G:'#1e6e73',P:'#ff86b8',N:'#2b3a7a',V:'#b9a6e8',O:'#d4a54a',T:'#7a6a9a',H:'#4a7ac8',E:'#4a8a5a',M:'#3a3a4a'};
var MAPS={
 robo:['.......Y........','.......S........','....WWWWWWWW....','...WWWWWWWWWW...','..WWKKKKKKKKWW..','..WWKYKKKKYKWW..','..WWKYKKKKYKWW..','..WWKKKYYKKKWW..','..WWKKKKKKKKWW..','...WWWWWWWWWW...','....WWWBBWWW....','...WWWWBBWWWW...','..W.WWWWWWWW.W..','....WWWWWWWW....','.....WWWWWW.....','....SSSSSSSS....'],
 a:['.....KKKK.....','....KKKKKK....','....FFFFFF....','....FKFFKF....','....FFFFFF....','.....FFFF.....','....HHHHHH....','...HHHHHHHH...','...HFHHHHFH...','...HHHHHHHH...','....NN..NN....','....NN..NN....','....KK..KK....'],
 owl:['..K........K..','..KK......KK..','..LLLLLLLLLL..','.LLWWLLLLWWLL.','.LWKKWLLWKKWL.','.LWKKWLLWKKWL.','.LLWWLYYLWWLL.','..LLLLYYLLLL..','..LOOOOOOOOL..','..LOOOOOOOOL..','...LOOOOOOL...','....LL..LL....','....YY..YY....']};
MAPS.b=MAPS.a.map(function(r){return r.replace(/H/g,'T')});MAPS.c=MAPS.a.map(function(r){return r.replace(/H/g,'E')});MAPS.d=MAPS.a.map(function(r){return r.replace(/H/g,'M').replace(/K/g,'L')});
function spriteFromMap(rows,pal){var h=rows.length,w=rows[0].length,cv=document.createElement('canvas');cv.width=w;cv.height=h;var c=cv.getContext('2d');
  rows.forEach(function(r,y){r.split('').forEach(function(ch,x){if(ch==='.')return;c.fillStyle=pal[ch];c.fillRect(x,y,1,1);});});return cv;}
function drawSprite(ctx,cv,x,y,s,flip){ctx.save();ctx.imageSmoothingEnabled=false;ctx.translate(x,y);if(flip)ctx.scale(-1,1);ctx.drawImage(cv,-cv.width*s/2,-cv.height*s/2,cv.width*s,cv.height*s);ctx.restore();}
var SPR={};Object.keys(MAPS).forEach(function(k){SPR[k]=spriteFromMap(MAPS[k],PAL);});
function coin(x,X,Y,r){x.save();x.fillStyle='#d4a54a';x.beginPath();x.arc(X,Y,r,0,7);x.fill();x.fillStyle='#f1c84a';x.beginPath();x.arc(X-r*.15,Y-r*.15,r*.7,0,7);x.fill();x.restore();}
function ledgerIcon(x,X,Y,w,h,col,line){x.fillStyle=col||'#efe6d2';rr(x,X,Y,w,h,4);x.fill();x.strokeStyle=line||'rgba(120,100,80,.45)';for(var i=1;i<4;i++){x.beginPath();x.moveTo(X+4,Y+i*h/4);x.lineTo(X+w-4,Y+i*h/4);x.stroke();}}

/* ===== 캐릭터 (부록 B-4) ===== */
var Cast=(function(){
  var DEFAULT={doc:'doc_e13',asst:'asst_e13',fly:'fly_e13',robo:'robo_e13'};
  function resolve(who,mood){var k=who+'_'+(mood||'');k=SPRITE_ALIAS[k]||k;if(SPRITE[k])return k;return SPRITE[DEFAULT[who]]?DEFAULT[who]:null;}
  function apply(img,who,mood){var k=resolve(who,mood),big=img.closest&&img.closest('.duelhead,.stage'),s=k?((big&&SPRITE192[k])||SPRITE[k]):'';
    if(s){img.src=s;img.style.visibility='';}else{img.removeAttribute('src');img.style.visibility='hidden';}
    if(k)img.dataset.img=k;var want=img.dataset.face,has=(k&&SPRITE_FACING[k])||'front';
    img.style.transform=(want&&has!=='front'&&want!==has)?'scaleX(-1)':'';}
  function set(img,who,mood){img.style.transition='opacity .2s';img.style.opacity=0;setTimeout(function(){apply(img,who,mood);img.style.opacity=1;},REDUCE?0:200);}
  function fill(){$$('img[data-who]').forEach(function(i){apply(i,i.dataset.who,i.dataset.mood||'');});}
  return {set:set,fill:fill,key:resolve};
})();

/* ===== 히어로 픽셀아트 (앵커별) ===== */
function heroArt(anchor){var cv=$('#heroCv');if(!cv)return;var r=rng(7),t=0,towers=[];for(var i=0;i<7;i++)towers.push({x:0.12+i*0.12,h:3+Math.floor(r()*9)});
  function draw(dt){t+=dt;var hdr=cv.parentNode,H=hdr.clientHeight||420,W=fit(cv,H),x=cv.getContext('2d');x.clearRect(0,0,W,H);
    var s=Math.max(3,Math.round(Math.min(W,H)/110));x.imageSmoothingEnabled=false;
    var g=x.createRadialGradient(W*.62,H*.15,10,W*.62,H*.15,H*.7);g.addColorStop(0,anchor==='C'?'rgba(241,182,70,.22)':'rgba(176,124,255,.18)');g.addColorStop(1,'rgba(0,0,0,0)');x.fillStyle=g;x.fillRect(0,0,W,H);
    var base=H*.86;
    if(anchor==='C'){x.fillStyle='#2b2a3d';x.beginPath();x.arc(W*.86,H*.42,H*.22,0,7);x.fill();x.strokeStyle='#4a4766';x.lineWidth=s*2;x.stroke();
      x.strokeStyle='#6a6488';x.lineWidth=s;for(var k=0;k<6;k++){var a=k*Math.PI/3+t*.1;x.beginPath();x.moveTo(W*.86,H*.42);x.lineTo(W*.86+Math.cos(a)*H*.12,H*.42+Math.sin(a)*H*.12);x.stroke();}
      towers.forEach(function(c){for(var j=0;j<c.h;j++){var y=base-j*s*2.2,X=W*c.x;x.fillStyle=j%2?'#d4a54a':'#f1c84a';x.fillRect(Math.round(X-s*4),Math.round(y),s*8,s*2);}});
      drawSprite(x,SPR.robo,W*.62,H*.3+Math.sin(t*2)*s*1.5,s*1.6);}
    else{ // D: 사무실 책상 + 서류 + 두 사람
      x.fillStyle='#2a2440';x.fillRect(W*.45,H*.62,W*.5,s*4);x.fillStyle='#3a3050';x.fillRect(W*.47,H*.62+s*4,s*3,H*.24);x.fillRect(W*.92,H*.62+s*4,s*3,H*.24);
      for(var p=0;p<4;p++){x.fillStyle='#efe6d2';x.fillRect(W*(.55+p*.08),H*.62-s*(1+p%2),s*12,s*2);}
      x.fillStyle='rgba(130,184,255,.25)';x.fillRect(W*.72,H*.2,W*.2,H*.22);x.strokeStyle='#4a4766';x.lineWidth=s;x.strokeRect(W*.72,H*.2,W*.2,H*.22);
      drawSprite(x,SPR.a,W*.6,H*.5,s*1.4,false);drawSprite(x,SPR.b,W*.8,H*.5,s*1.4,true);
      var ph=(t*0.4)%1;coin(x,W*.6+(W*.2)*ph,H*.38-Math.sin(ph*Math.PI)*H*.08,s*2.4);}
    x.fillStyle='rgba(241,200,74,.8)';for(var q=0;q<10;q++){var px=W*(0.1+0.8*((q*0.37+t*0.03)%1)),py=H*(0.2+0.5*((q*0.61)%1));if((Math.floor(t*2+q))%3===0)x.fillRect(px,py,s,s);}}
  addMod(cv,draw);addEventListener('resize',function(){draw(0)});draw(0);}

/* ===== 데이터 블록 ===== */
function J(id){var e=document.getElementById(id);return e?JSON.parse(e.textContent):null;}

/* ===== 용어 말풍선 ===== */
var Gloss=(function(){var G={},core=[],mode='core',tip,SKIP=['BUTTON','H1','H2','NAV','CANVAS','SCRIPT','STYLE','INPUT','LABEL','A','SUMMARY','CODE','B','PRE'];
  var NOCLS=['kpis','jt','hashbox','quiz','chain','eq','tag','lvtag','glabel','choice'];
  function init(){tip=$('#tip');(J('gloss-data')||[]).forEach(function(g){G[g[0]]=g;if(g[6])core.push(g[0]);});
    document.addEventListener('pointerover',function(e){var t=e.target.closest&&e.target.closest('.jt');if(t)show(t);});
    document.addEventListener('pointerout',function(e){if(e.target.closest&&e.target.closest('.jt'))hide();});
    document.addEventListener('focusin',function(e){if(e.target.classList&&e.target.classList.contains('jt'))show(e.target);});
    document.addEventListener('focusout',hide);
    document.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('.jt');if(t){tip.style.display==='block'?hide():show(t);}else hide();});
    addEventListener('scroll',hide,{passive:true});addEventListener('keydown',function(e){if(e.key==='Escape')hide();});
    $$('.jt').forEach(function(s){s.tabIndex=0;});run();}
  function terms(){var t=mode==='all'?Object.keys(G):mode==='core'?core:[];return t.sort(function(a,b){return b.length-a.length});}
  function clear(){$$('span.jt[data-auto]').forEach(function(s){s.replaceWith(document.createTextNode(s.textContent));});document.body.normalize();
    $$('span.jt').forEach(function(s){s.style.borderBottomStyle=mode==='off'?'none':'';s.style.cursor=mode==='off'?'auto':'';});}
  function run(){clear();var T=terms();if(!T.length)return;
    $$('section.level:not(#kg):not(#export), header.hero').forEach(function(sec){var seen={};$$('.jt',sec).forEach(function(s){seen[s.dataset.t]=1;});
      var w=document.createTreeWalker(sec,NodeFilter.SHOW_TEXT,{acceptNode:function(n){for(var p=n.parentNode;p&&p!==sec;p=p.parentNode){if(SKIP.indexOf(p.tagName)>=0)return NodeFilter.FILTER_REJECT;if(p.classList)for(var c=0;c<NOCLS.length;c++)if(p.classList.contains(NOCLS[c]))return NodeFilter.FILTER_REJECT;}
        return n.nodeValue.trim()?NodeFilter.FILTER_ACCEPT:NodeFilter.FILTER_REJECT;}});
      var nodes=[];while(w.nextNode())nodes.push(w.currentNode);
      nodes.forEach(function(n){T.forEach(function(t){if(seen[t]||!n.parentNode||t.length<2)return;var i=n.nodeValue.indexOf(t);
        while(i>=0&&T.some(function(u){return u.length>t.length&&u.indexOf(t)===0&&n.nodeValue.substr(i,u.length)===u;}))i=n.nodeValue.indexOf(t,i+1);if(i<0)return;
        var after=n.splitText(i);after.splitText(t.length);var s=document.createElement('span');s.className='jt';s.dataset.t=t;s.dataset.auto='1';s.tabIndex=0;s.textContent=t;after.replaceWith(s);seen[t]=1;n=s.nextSibling||n;});});});}
  function show(el){if(mode==='off')return;var g=G[el.dataset.t];if(!g)return;tip.innerHTML='<b>'+g[1]+'</b><small>'+g[2]+'</small><br>'+g[3];tip.style.display='block';
    var r=el.getBoundingClientRect(),tw=Math.min(300,innerWidth-16);tip.style.left=Math.max(8,Math.min(r.left,innerWidth-tw-8))+'px';
    var top=r.bottom+8;tip.style.top=top+'px';var th=tip.offsetHeight;if(top+th>innerHeight-8)tip.style.top=(r.top-th-8)+'px';}
  function hide(){if(tip)tip.style.display='none';}
  return {init:init,cycle:function(){mode=mode==='core'?'all':mode==='all'?'off':'core';run();return mode;}};})();

/* ===== 학습 도우미 + 퀴즈 ===== */
var Study=(function(){var total=0,ok={};
  function init(){var Q=J('quiz-data')||{};
    $$('.quiz').forEach(function(box){var id=box.dataset.quiz,L=Q[id]||[];total+=L.length;
      box.innerHTML='<h4>확인 퀴즈</h4>'+L.map(function(q,i){return '<div class="qq" data-i="'+i+'"><p>'+q.q+'</p><div class="opts">'+q.o.map(function(o,j){return '<button class="opt" data-j="'+j+'">'+o+'</button>'}).join('')+'</div><p class="fb" aria-live="polite"></p></div>'}).join('');
      $$('.qq',box).forEach(function(qq){var q=L[+qq.dataset.i];$$('.opt',qq).forEach(function(b){b.addEventListener('click',function(){
        var j=+b.dataset.j,fb=$('.fb',qq);$$('.opt',qq).forEach(function(x){x.classList.remove('ok','no')});
        if(j===q.a){b.classList.add('ok');fb.textContent='정답. '+q.why;ok[id+qq.dataset.i]=1;}else{b.classList.add('no');fb.textContent='힌트: '+q.hint;}upd();});});});});
    addEventListener('scroll',upd,{passive:true});
    $('#stBtn').addEventListener('click',function(){var m=Gloss.cycle();this.textContent='밑줄: '+({core:'핵심',all:'전체',off:'끄기'})[m];});upd();}
  function upd(){var h=document.documentElement,p=Math.round(100*h.scrollTop/Math.max(1,h.scrollHeight-h.clientHeight));$('#prog').style.width=p+'%';
    $('#stTxt').textContent='읽은 곳 '+p+'% · 퀴즈 '+Object.keys(ok).length+'/'+total;}
  return {init:init};})();

/* ===== 대결 (부록 B-5 일반화) =====
 o = {run:()=>({fly,robo,foul}), lesson, higherIsBetter, drawMargin, fmt:v=>문자열, bar:v=>0~1, names:{fly,robo}, say:(r,res)=>조수 발표, foulRule } */
function Duel(o){var root=$('#duelBox'),shown=false,guess=null;
  var flyImg=$('.duelhead img[data-who=fly]',root),roboImg=$('.duelhead img[data-who=robo]',root),asstImg=$('.say.asst img',root),docImg=$('.say.verdict img',root);
  $$('.guess .bt',root).forEach(function(b){b.addEventListener('click',function(){guess=b.dataset.g;press('#duelBox .guess .bt',b);});});
  function bar(name,v,col){var w=Math.max(0.6,100*(o.bar?o.bar(v):v));return '<div class="barrow"><span>'+name+'</span><div class="track"><div class="fill" style="width:'+Math.min(100,w)+'%;background:'+col+'"></div></div><b>'+o.fmt(v)+'</b></div>';}
  $('.reveal',root).addEventListener('click',function(){
    if(shown){reset();return;}var r=o.run(),f=r.fly,b=r.robo,d=o.higherIsBetter?f-b:b-f,res;
    if(r.foul)res='X';else if(Math.abs(f-b)<=o.drawMargin)res='D';else res=d>0?'F':'R';
    var big=Math.abs((o.bar?o.bar(f)-o.bar(b):f-b))>=0.10;var M={F:['arms','sigh'],R:[big?'cry':'coffee','happy'],D:['coffee','meh'],X:['arms','blush']}[res];
    Cast.set(flyImg,'fly',M[0]);Cast.set(roboImg,'robo',M[1]);Cast.set(asstImg,'asst',res==='X'?'shock':res==='D'?'smile':'spark');Cast.set(docImg,'doc',res==='D'?'scale':'judge');
    $('#scF').textContent=(res==='F'||res==='X')?1:0;$('#scR').textContent=res==='R'?1:0;
    $('.bars',root).innerHTML=bar(o.names.fly,f,C.fly)+bar(o.names.robo,b,C.robo);
    $('.say.asst p',root).textContent=o.say(r,res);
    var who={F:'초파리 승.',R:'Money-Robo 승.',D:'이번 판은 나눠 갖는다.',X:'점수와 상관없이 Money-Robo 실격.'}[res];
    $('.say.verdict p',root).textContent=res==='X'?(o.foulRule+'을 어겼다. '+who):(o.lesson+'. '+who);
    $('#guessFb').textContent=guess?(guess===res?'맞혔어요. 예측이 결과와 같았어요.':'예측과 달랐어요. 위 두 막대를 다시 비교해 보세요.'):'';
    root.classList.add('open');shown=true;this.textContent='다시 닫기';if(o.onReveal)setTimeout(function(){o.onReveal(res);},30);});
  function reset(){Cast.set(flyImg,'fly','point');Cast.set(roboImg,'robo','coin');Cast.set(asstImg,'asst','firm');Cast.set(docImg,'doc','judge');root.classList.remove('open');shown=false;$('.reveal',root).textContent='결과 보기';}
  window.__duel=o;}

/* ===== 제2부: 지식 색인 (O1) ===== */
var TYPE_KO={Concept:'개념',Method:'방법',Task:'문제',Metric:'지표',Claim:'주장',Term:'용어',Question:'질문',Analogy:'비유',Limitation:'한계',Simulation:'실험',Work:'문헌',QuizItem:'퀴즈'};
var TYPE_COL={Concept:'#82b8ff',Method:'#5ee39c',Task:'#c48a5a',Metric:'#f1b646',Claim:'#d672d6',Term:'#9ab8ff',Question:'#f0604d',Analogy:'#ff86b8',Limitation:'#ff8f80',Simulation:'#57d0dc',Work:'#b9a6e8',QuizItem:'#7a7a99'};
var P_KO={'lab:prerequisiteOf':'선수','lab:hasLimitation':'한계','lab:addressedBy':'해결','lab:partOf':'부분','lab:broader':'상위','lab:contrastsWith':'대비','lab:analogyOf':'비유','lab:supports':'근거','lab:assertedIn':'출처','lab:demonstratedBy':'실험','lab:assesses':'퀴즈','lab:raises':'질문','lab:solves':'푼다','lab:evaluatedBy':'지표','lab:relatedTo':'관련'};
var KG,REF,META;
function kgIndex(){var byId={};KG.nodes.forEach(function(n){byId[n.id]=n;});
  var CHIPS=['Concept','Method','Task','Metric','Claim','Term','Question','Analogy','Limitation'],on={};CHIPS.forEach(function(c){on[c]=true;});
  $('#kgChips').innerHTML=CHIPS.filter(function(c){return KG.nodes.some(function(n){return n.type===c})}).map(function(c){return '<button class="chip" data-c="'+c+'" aria-pressed="true">'+TYPE_KO[c]+'</button>'}).join(' ');
  $$('#kgChips .chip').forEach(function(b){b.addEventListener('click',function(){on[b.dataset.c]=!on[b.dataset.c];b.setAttribute('aria-pressed',on[b.dataset.c]);list();});});
  var deg={};KG.edges.forEach(function(e){deg[e.s]=(deg[e.s]||0)+1;deg[e.o]=(deg[e.o]||0)+1;});
  var types={};KG.nodes.forEach(function(n){types[n.type]=(types[n.type]||0)+1;});
  $('#kgStats').textContent='노드 '+KG.nodes.length+'개 · 관계 '+KG.edges.length+'개 · '+Object.keys(types).map(function(t){return (TYPE_KO[t]||t)+' '+types[t]}).join(', ')+' · 외부 매핑 확인 0개';
  function evc(n){return KG.edges.filter(function(e){return e.p==='lab:supports'&&e.o===n.id;}).length;}
  function list(hl){var q=$('#kgQ').value.trim().toLowerCase();
    var items=KG.nodes.filter(function(n){if(CHIPS.indexOf(n.type)<0||!on[n.type])return false;if(!q)return true;
      var s=[n.label.ko,n.label.en,(n.definition||{}).ko||'',((n.altLabel||{}).ko||[]).join(' ')].join(' ').toLowerCase();return s.indexOf(q)>=0;});
    $('#kgList').innerHTML=items.map(function(n){return '<div class="kgitem'+(n.id===hl?' hl':'')+'" id="kgi-'+n.id.replace(/[^a-z0-9]/gi,'_')+'"><span class="t" style="background:'+TYPE_COL[n.type]+'">'+TYPE_KO[n.type]+'</span><b>'+n.label.ko+'</b> <span class="glabel">'+n.label.en+'</span>'+
      (n.definition?'<p>'+n.definition.ko+'</p>':'')+(n.source?'<p>출처: '+n.source.map(function(s){return s.cite+' '+s.loc}).join('; ')+'</p>':'')+
      '<p><a href="'+n.anchor+'">설명 보러 가기 →</a> · 근거 '+evc(n)+'개 · 연결 '+(deg[n.id]||0)+'개</p></div>'}).join('')||'<p class="sub">찾는 항목이 없어요.</p>';
    if(hl){var el=document.getElementById('kgi-'+hl.replace(/[^a-z0-9]/gi,'_'));if(el)el.scrollIntoView({block:'nearest'});}}
  $('#kgQ').addEventListener('input',function(){list();});
  var ladder=KG.ladder||[];
  $('#kgPath').innerHTML=ladder.map(function(id,i){var lim=KG.edges.filter(function(e){return e.s===id&&e.p==='lab:hasLimitation';})[0];
    return '<span class="s done">'+(i+1)+' '+byId[id].label.ko+'</span>'+(lim?'<span class="s" style="color:var(--eye)">한계: '+byId[lim.o].label.ko+'</span>':'');}).join('<span class="s">→</span>');
  $('#kgOpen').innerHTML=KG.nodes.filter(function(n){return n.type==='Question'}).map(function(n){return '<li><a href="'+n.anchor+'">'+n.label.ko+'</a></li>'}).join('');
  $('#kgLegend').innerHTML=Object.keys(TYPE_COL).filter(function(t){return t!=='QuizItem'&&types[t]}).map(function(t){return '<span><i style="background:'+TYPE_COL[t]+'"></i>'+TYPE_KO[t]+'</span>'}).join('');
  var GN=KG.nodes.filter(function(n){return n.type!=='QuizItem'&&n.type!=='Section';}),idx={};GN.forEach(function(n,i){idx[n.id]=i;});
  var GE=KG.edges.filter(function(e){return idx[e.s]!==undefined&&idx[e.o]!==undefined;});
  var r=rng(42),P=GN.map(function(){return {x:r()*2-1,y:r()*2-1,vx:0,vy:0};});
  for(var it=0;it<200;it++){var a=0.02*(1-it/200)+0.002;
    for(var i=0;i<P.length;i++)for(var j=i+1;j<P.length;j++){var dx=P[i].x-P[j].x,dy=P[i].y-P[j].y,d2=dx*dx+dy*dy+0.01,f=0.004/d2;P[i].vx+=dx*f;P[i].vy+=dy*f;P[j].vx-=dx*f;P[j].vy-=dy*f;}
    GE.forEach(function(e){var A=P[idx[e.s]],B=P[idx[e.o]],dx=B.x-A.x,dy=B.y-A.y,d=Math.sqrt(dx*dx+dy*dy)+1e-6,f=(d-0.3)*0.05;A.vx+=dx/d*f;A.vy+=dy/d*f;B.vx-=dx/d*f;B.vy-=dy/d*f;});
    P.forEach(function(p){p.vx-=p.x*0.01;p.vy-=p.y*0.01;p.x+=p.vx*a*20;p.y+=p.vy*a*20;p.vx*=0.6;p.vy*=0.6;});}
  var xs=P.map(function(p){return p.x}),ys=P.map(function(p){return p.y}),mx=Math.min.apply(0,xs),Mx=Math.max.apply(0,xs),my=Math.min.apply(0,ys),My=Math.max.apply(0,ys);
  var cv=$('#kgCv'),sel=null,scr=[];
  function draw(){var W=fit(cv,400),H=400,x=cv.getContext('2d');x.clearRect(0,0,W,H);
    scr=P.map(function(p){return [24+(W-48)*(p.x-mx)/(Mx-mx||1),24+(H-48)*(p.y-my)/(My-my||1)];});
    GE.forEach(function(e){var A=scr[idx[e.s]],B=scr[idx[e.o]],hl=sel&&(e.s===sel||e.o===sel);x.strokeStyle=hl?'rgba(241,182,70,.9)':e.p==='lab:prerequisiteOf'?'rgba(94,227,156,.55)':'rgba(157,155,184,.22)';x.lineWidth=hl?1.6:1;
      x.beginPath();x.moveTo(A[0],A[1]);x.lineTo(B[0],B[1]);x.stroke();
      var ang=Math.atan2(B[1]-A[1],B[0]-A[0]),ex=B[0]-Math.cos(ang)*7,ey=B[1]-Math.sin(ang)*7;x.fillStyle=x.strokeStyle;x.beginPath();x.moveTo(ex,ey);x.lineTo(ex-Math.cos(ang-0.4)*6,ey-Math.sin(ang-0.4)*6);x.lineTo(ex-Math.cos(ang+0.4)*6,ey-Math.sin(ang+0.4)*6);x.fill();});
    GN.forEach(function(n,i){var s=scr[i],rad=4+Math.min(6,(deg[n.id]||0)*0.6);x.fillStyle=TYPE_COL[n.type];x.beginPath();x.arc(s[0],s[1],rad,0,7);x.fill();
      if(n.id===sel){x.strokeStyle='#fff';x.lineWidth=2;x.stroke();x.lineWidth=1;}
      if((deg[n.id]||0)>=5||n.id===sel)txt(x,n.label.ko.length>12?n.label.ko.slice(0,12)+'…':n.label.ko,s[0]+rad+3,s[1]+4,{s:11,c:C.text});});
    txt(x,'초록 선 = 선수 관계',8,H-8,{s:11,c:C.muted});}
  cv.addEventListener('pointerdown',function(ev){var rc=cv.getBoundingClientRect(),px=ev.clientX-rc.left,py=ev.clientY-rc.top,best=-1,bd=196;
    scr.forEach(function(s,i){var d=(s[0]-px)*(s[0]-px)+(s[1]-py)*(s[1]-py);if(d<bd){bd=d;best=i;}});
    if(best>=0){sel=GN[best].id;var n=GN[best];if(CHIPS.indexOf(n.type)>=0&&!on[n.type]){on[n.type]=true;var cb=$('#kgChips .chip[data-c='+n.type+']');if(cb)cb.setAttribute('aria-pressed',true);}$('#kgQ').value='';list(sel);draw();}});
  addEventListener('resize',draw);list();draw();
  $('#kgJson').addEventListener('click',function(){download(new Blob([JSON.stringify(KG,null,2)],{type:'application/json'}),'kg_'+META.number+'.json');});
  $('#kgMmd').addEventListener('click',function(){download(new Blob([toMermaid(KG)],{type:'text/plain'}),'kg_'+META.number+'.mmd');});}

/* ===== 제2부: 꾸러미 (O2, 부록 O-B) ===== */
var CRC=(function(){var t=[],c;for(var n=0;n<256;n++){c=n;for(var k=0;k<8;k++)c=c&1?0xEDB88320^(c>>>1):c>>>1;t[n]=c>>>0;}
  return function(u8){var x=0xFFFFFFFF;for(var i=0;i<u8.length;i++)x=t[(x^u8[i])&255]^(x>>>8);return (x^0xFFFFFFFF)>>>0;};})();
function makeZip(files){var enc=new TextEncoder(),parts=[],central=[],off=0;
  function u16(v){return [v&255,(v>>8)&255]}function u32(v){return [v&255,(v>>8)&255,(v>>16)&255,(v>>>24)&255]}
  files.forEach(function(f){var name=enc.encode(f.name),data=enc.encode(f.text),crc=CRC(data);
    var head=[].concat(u32(0x04034b50),u16(20),u16(0x0800),u16(0),u16(0),u16(0),u32(crc),u32(data.length),u32(data.length),u16(name.length),u16(0));
    parts.push(new Uint8Array(head),name,data);
    central.push([].concat(u32(0x02014b50),u16(20),u16(20),u16(0x0800),u16(0),u16(0),u16(0),u32(crc),u32(data.length),u32(data.length),u16(name.length),u16(0),u16(0),u16(0),u16(0),u32(0),u32(off)),name);
    off+=head.length+name.length+data.length;});
  var cdStart=off,cdLen=0;central.forEach(function(c){if(Array.isArray(c)){parts.push(new Uint8Array(c));cdLen+=c.length;}else{parts.push(c);cdLen+=c.length;}});
  parts.push(new Uint8Array([].concat(u32(0x06054b50),u16(0),u16(0),u16(files.length),u16(files.length),u32(cdLen),u32(cdStart),u16(0))));
  return new Blob(parts,{type:'application/zip'});}
function download(blob,name){var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;document.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(a.href);a.remove();},500);
  if(blob.type.indexOf('zip')<0&&blob.text){blob.text().then(function(t){var box=$('#dlBox');if(!box)return;$('#dlName').textContent=name;$('#dlText').textContent=t.replace(/^﻿/,'');box.classList.add('on');});}}
var BIBT={'article-journal':'article','paper-conference':'inproceedings','book':'book','chapter':'incollection','webpage':'misc','dataset':'misc','report':'techreport','thesis':'phdthesis','software':'misc','article-newspaper':'article'};
var RIST={'article-journal':'JOUR','paper-conference':'CPAPER','book':'BOOK','chapter':'CHAP','webpage':'ELEC','dataset':'DATA','report':'RPRT','thesis':'THES','software':'COMP','article-newspaper':'NEWS'};
function names(a){return (a||[]).map(function(p){return p.literal||(p.family+(p.given?', '+p.given:''));});}
function yr(r){return r.issued&&r.issued['date-parts'][0][0];}
function toBib(r){var f=[],add=function(k,v){if(v!==undefined&&v!==null&&v!=='')f.push('  '+k+' = {'+v+'}');};
  add('title',r.title);add('author',names(r.author).map(function(n){return n==='et al.'?'others':n;}).join(' and '));add('year',yr(r));
  add(r.type==='article-journal'||r.type==='article-newspaper'?'journal':(r.type==='webpage'?'howpublished':'booktitle'),r['container-title']);add('volume',r.volume);add('number',r.issue);
  add('pages',r.page);add('publisher',r.publisher);add('doi',r.DOI);add('url',r.URL);if(r.lab&&r.lab.note)add('note',r.lab.note);
  return '@'+(BIBT[r.type]||'misc')+'{'+r.id+',\n'+f.join(',\n')+'\n}';}
function toRis(r){var L=['TY  - '+(RIST[r.type]||'GEN')],add=function(t,v){if(v)L.push(t+'  - '+v);};
  add('TI',r.title);names(r.author).forEach(function(n){add('AU',n);});add('PY',yr(r));add('T2',r['container-title']);add('VL',r.volume);add('IS',r.issue);add('DO',r.DOI);add('UR',r.URL);if(r.lab&&r.lab.note)add('N1',r.lab.note);L.push('ER  - ');return L.join('\r\n');}
function refText(r){var a=names(r.author);var au=a.length?a.join(', '):'(저자 표기 없음)';return au+' ('+(yr(r)||'n.d.')+'). '+r.title+'.'+(r['container-title']?' '+r['container-title']+'.':'')+(r.URL?' '+r.URL:'');}
function csvq(v){v=(v===undefined||v===null)?'':String(v);return /[",\n]/.test(v)?'"'+v.replace(/"/g,'""')+'"':v;}
function toNodesCsv(g){return 'id,type,label_ko,label_en,status,level,family,page,anchor\r\n'+g.nodes.map(function(n){return [n.id,n.type,n.label.ko,n.label.en,n.status,n.level||'',n.family||'',n.page,n.anchor].map(csvq).join(',')}).join('\r\n');}
function toEdgesCsv(g){return 'source,predicate,target,anchor,confidence\r\n'+g.edges.map(function(e){return [e.s,e.p,e.o,e.anchor,e.confidence].map(csvq).join(',')}).join('\r\n');}
function toProvCsv(g,R){var rows=['item,kind,work,loc,factCard,confidence,verified,pageAnchor'];
  g.nodes.forEach(function(n){(n.source||[]).forEach(function(s){var ref=R.filter(function(r){return r.id===s.cite})[0];rows.push([n.id,'node',s.cite,s.loc,(n.evidence||[]).join(' '),n.confidence,ref&&ref.lab.verified.title?'true':'false',n.anchor].map(csvq).join(','));});});
  g.edges.filter(function(e){return e.p==='lab:assertedIn'}).forEach(function(e){rows.push([e.s+' assertedIn '+e.o,'edge',e.o.replace('lab:work/',''),'',(e.evidence||[]).join(' '),e.confidence,'true',e.anchor].map(csvq).join(','));});
  return rows.join('\r\n');}
function ttlEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,' ');}
function iri(id){return '<'+id.replace(/^lab:/,'urn:lab:')+'>';}
var PMAP={'lab:broader':'skos:broader','lab:partOf':'dct:isPartOf','lab:relatedTo':'skos:related','lab:assertedIn':'schema:citation'};
function toTurtle(g){var L=['@prefix skos: <http://www.w3.org/2004/02/skos/core#> .','@prefix schema: <https://schema.org/> .','@prefix dct: <http://purl.org/dc/terms/> .','@prefix lab: <urn:lab:> .',''];
  g.nodes.forEach(function(n){var s=[iri(n.id)+' a skos:Concept, lab:'+n.type+' ;','  skos:prefLabel "'+ttlEsc(n.label.ko)+'"@ko, "'+ttlEsc(n.label.en)+'"@en'];
    if(n.definition)s.push('  skos:definition "'+ttlEsc(n.definition.ko)+'"@ko');
    g.edges.filter(function(e){return e.s===n.id}).forEach(function(e){s.push('  '+e.p+' '+iri(e.o));if(PMAP[e.p])s.push('  '+PMAP[e.p]+' '+iri(e.o));});
    L.push(s.join(' ;\n')+' .');});return L.join('\n');}
function toJsonLd(g){var ctx={skos:'http://www.w3.org/2004/02/skos/core#',schema:'https://schema.org/',dct:'http://purl.org/dc/terms/',prov:'http://www.w3.org/ns/prov#',lab:'urn:lab:'};
  return {'@context':ctx,'@graph':g.nodes.map(function(n){var o={'@id':n.id,'@type':['skos:Concept','lab:'+n.type],'skos:prefLabel':[{'@value':n.label.ko,'@language':'ko'},{'@value':n.label.en,'@language':'en'}]};
    if(n.definition)o['skos:definition']={'@value':n.definition.ko,'@language':'ko'};
    g.edges.filter(function(e){return e.s===n.id}).forEach(function(e){(o[e.p]=o[e.p]||[]).push({'@id':e.o});if(PMAP[e.p])(o[PMAP[e.p]]=o[PMAP[e.p]]||[]).push({'@id':e.o});});return o;})};}
function toMermaid(g){var keep=g.nodes.filter(function(n){return ['Method','Limitation','Concept'].indexOf(n.type)>=0}).slice(0,40),ids={};keep.forEach(function(n,i){ids[n.id]='n'+i;});
  var L=['graph LR'];keep.forEach(function(n){L.push('  '+ids[n.id]+'["'+n.label.ko.replace(/"/g,"'")+'"]');});
  g.edges.forEach(function(e){if(ids[e.s]&&ids[e.o])L.push('  '+ids[e.s]+' -- '+(P_KO[e.p]||e.p)+' --> '+ids[e.o]);});return L.join('\n');}
function filterScope(g,scope){if(scope==='all')return g;var keepT={concepts:['Concept','Method','Term','Task','Metric'],claims:['Claim','Work'],prereq:['Method','Concept','Limitation']}[scope];
  var ns=g.nodes.filter(function(n){return keepT.indexOf(n.type)>=0}),ids={};ns.forEach(function(n){ids[n.id]=1;});
  var es=g.edges.filter(function(e){if(!ids[e.s]||!ids[e.o])return false;if(scope==='prereq')return ['lab:prerequisiteOf','lab:hasLimitation','lab:addressedBy'].indexOf(e.p)>=0;return true;});
  if(scope!=='concepts'){var used={};es.forEach(function(e){used[e.s]=used[e.o]=1;});ns=ns.filter(function(n){return used[n.id]});}
  return {version:g.version,page:g.page,scope:scope,nodes:ns,edges:es};}
function todo(){var L=[];REF.forEach(function(r){var v=r.lab.verified;Object.keys(v).forEach(function(k){if(!v[k])L.push(r.id+': '+k+' 확인 필요'+(r.lab.note?' ('+r.lab.note+')':''));});});
  L.push('page_meta: 라이선스·공개 주소 채워 넣을 것');L.push('kg: 외부 온톨로지(Wikidata 등) 대응 ID 미확인 — 모두 비워 둠');return L;}
function readme(M,g,R){return ['온톨로지·서지 꾸러미 — '+M.title,'','페이지: '+M.series+' '+M.number+' (v'+M.version+', '+M.date+')','저자: '+M.creator.map(function(c){return c.name}).join(', '),'','권장 인용: '+M.suggestedCitation,'',
  '파일: manifest.json, page_meta.json, kg.json(원본), kg.jsonld, kg.ttl, nodes.csv, edges.csv, references.csl.json(원본), references.bib, references.ris, provenance.csv','',
  '노드 '+g.nodes.length+' · 관계 '+g.edges.length+' · 문헌 '+R.length,'','확인 필요:'].concat(todo().map(function(t){return ' - '+t})).concat(['','lab: 접두어 IRI는 urn:lab: (공개 주소가 정해지면 바꿀 것).','출처 없는 주장은 넣지 않았다.']).join('\n');}
function buildPackage(scope){var g=filterScope(KG,scope);
  var files=[{name:'page_meta.json',text:JSON.stringify(META,null,2)},{name:'kg.json',text:JSON.stringify(g,null,2)},{name:'kg.jsonld',text:JSON.stringify(toJsonLd(g),null,2)},
    {name:'kg.ttl',text:toTurtle(g)},{name:'nodes.csv',text:'﻿'+toNodesCsv(g)},{name:'edges.csv',text:'﻿'+toEdgesCsv(g)},
    {name:'references.csl.json',text:JSON.stringify(REF,null,2)},{name:'references.bib',text:REF.map(toBib).join('\n\n')},{name:'references.ris',text:REF.map(toRis).join('\r\n')},
    {name:'provenance.csv',text:'﻿'+toProvCsv(g,REF)},{name:'README.txt',text:readme(META,g,REF)}];
  files.unshift({name:'manifest.json',text:JSON.stringify({package:'lab-kg',version:META.version,page:META.number,created:META.date,scope:scope,registry:KG.registry,
    counts:{nodes:g.nodes.length,edges:g.edges.length,refs:REF.length},files:files.map(function(f){return f.name})},null,2)});return files;}
function exportSection(){var scope='all',cf='text';
  var claims=KG.nodes.filter(function(n){return n.type==='Claim'}),withSrc=claims.filter(function(n){return n.source&&n.source.length});
  var verRefs=REF.filter(function(r){return r.lab.verified.title&&r.lab.verified.year}).length;
  kpis($('#exK'),[[KG.nodes.length,'노드','g'],[KG.edges.length,'관계','m'],[REF.length,'문헌','a'],[verRefs+'/'+REF.length,'제목·연도 확인된 문헌','g'],[withSrc.length+'/'+claims.length,'출처 있는 주장','g']]);
  var selfRef={id:META.citekey,type:'webpage',title:META.title,author:[{family:'안',given:'상선'}],issued:{'date-parts':[[2026,10,29]]},'container-title':META.series+' '+META.number};
  function cite(){$('#exCite').textContent=cf==='text'?META.suggestedCitation:cf==='bib'?toBib(selfRef):toRis(selfRef);}
  $$('[data-cf]').forEach(function(b){b.addEventListener('click',function(){cf=b.dataset.cf;press('[data-cf]',b);cite();});});
  function copy(btn,el,lab){var t=el.textContent;(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){btn.textContent='복사됨';setTimeout(function(){btn.textContent=lab},1200);},function(){var s=getSelection(),rg=document.createRange();rg.selectNodeContents(el);s.removeAllRanges();s.addRange(rg);btn.textContent='선택됨 — Ctrl+C';});}
  $('#exCopy').addEventListener('click',function(){copy(this,$('#exCite'),'복사');});
  $('#dlCopy').addEventListener('click',function(){copy(this,$('#dlText'),'내용 복사');});$('#dlClose').addEventListener('click',function(){$('#dlBox').classList.remove('on')});
  var ROLE={primary:'주 자료',background:'배경',data:'수치',figure:'그림',software:'소프트웨어'};
  $('#exRefs').innerHTML=REF.map(function(r){var v=r.lab.verified,ok=v.title&&v.year;return '<div class="ref">'+refText(r)+' <span class="badge role">'+ROLE[r.lab.role]+'</span><span class="badge '+(ok?'ok':'no')+'">'+(ok?'제목·연도 확인됨':'확인 필요')+'</span>'+
    '<details><summary class="glabel" style="cursor:pointer">뒷받침하는 항목 '+r.lab.supports.length+'개</summary><ul>'+r.lab.supports.map(function(s){var n=KG.nodes.filter(function(x){return x.id===s})[0];return '<li><a href="#kg" data-kg="'+s+'">'+(n?n.label.ko:s)+'</a></li>'}).join('')+'</ul><p class="glabel">'+r.lab.checkedBy+(r.lab.note?' · '+r.lab.note:'')+'</p></details></div>'}).join('');
  $$('#exRefs [data-kg]').forEach(function(a){a.addEventListener('click',function(){$('#kgQ').value=a.textContent;$('#kgQ').dispatchEvent(new Event('input'));});});
  $$('[data-sc]').forEach(function(b){b.addEventListener('click',function(){scope=b.dataset.sc;press('[data-sc]',b);files();});});
  function files(){var F=buildPackage(scope);$('#exFiles').innerHTML=F.map(function(f,i){return '<button class="bt" data-fi="'+i+'">'+f.name+'</button>'}).join('');
    $$('#exFiles [data-fi]').forEach(function(b){b.addEventListener('click',function(){var f=buildPackage(scope)[+b.dataset.fi];download(new Blob([f.text],{type:'text/plain;charset=utf-8'}),f.name);});});}
  $('#exZip').addEventListener('click',function(){download(makeZip(buildPackage(scope)),'kg_'+META.number+'_'+scope+'.zip');});
  var T=todo();$('#exTodo').innerHTML=T.map(function(t){return '<li>'+t+'</li>'}).join('');
  $('#exSay').textContent='출처 없는 주장은 꾸러미에 넣지 않았어요. 확인할 항목 '+T.length+'개는 위에 있어요.';
  $('#exVer').textContent='꾸러미 v'+META.version+' · 만든 날 '+META.date+' · 등록부: '+KG.registry;cite();files();}

/* ===== 시작 ===== */
var LAB={start:function(o){KG=J('kg-raw');REF=J('refs-csl');META=J('page-meta');Cast.fill();heroArt(o&&o.anchor||'C');
  if(o&&o.init)o.init();Gloss.init();Study.init();kgIndex();exportSection();requestAnimationFrame(loop);}};
