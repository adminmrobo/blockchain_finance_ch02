LAB.start({anchor:'D',init:function(){
var CASES={fish:{steps:['어획','가공장','냉장 운송','도매','마트'],field:'상자 식별번호',real:'KR-0417',fake:'KR-9032'},
  beef:{steps:['출생 농장','사육','도축','가공·유통','판매'],field:'개체 식별번호',real:'002-1234',fake:'002-9876'},
  land:{steps:['토지 등록','소유권 이전','담보 설정','은행 조회','매매 계약'],field:'소유자',real:'A',fake:'B'}};
function records(cs,swap,lie){var c=CASES[cs],p='0'.repeat(64),R=[];for(var i=0;i<5;i++){var v=lie?c.fake:c.real;var r={i:i,step:c.steps[i],v:v,prev:p};r.h=SHA256(r.step+'|'+r.v+'|'+p);R.push(r);p=r.h;}
  if(swap){R[3].v=c.fake;R[4].v=c.fake;R[3].h=SHA256(R[3].step+'|'+R[3].v+'|'+R[3].prev);R[4].prev=R[3].h;R[4].h=SHA256(R[4].step+'|'+R[4].v+'|'+R[4].prev);}return R;}
function detect(R){for(var i=1;i<R.length;i++){if(R[i].v!==R[i-1].v)return i+1;}return 0;}

/* ① 단계별 기록 */
(function(){var c1=$('#c1'),c1b=$('#c1b'),cs='fish',swap=false,lie=false,t=0;
  $$('#lv1 [data-case]').forEach(function(b){b.addEventListener('click',function(){cs=b.dataset.case;press('#lv1 [data-case]',b);upd();});});
  $('#b1Swap').addEventListener('click',function(){swap=!swap;this.setAttribute('aria-pressed',swap);upd();});
  $('#b1Lie').addEventListener('click',function(){lie=!lie;this.setAttribute('aria-pressed',lie);upd();});
  function drawA(){var W=fit(c1,210),H=210,x=c1.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var R=records(cs,swap,lie),d=detect(R),c=CASES[cs],bw=(W-60)/5;
    R.forEach(function(r,i){var X=20+i*(bw+5),Y=50,bad=d&&i>=d-1,isFake=r.v===c.fake;if(i>0){x.strokeStyle=bad&&i===d-1?C.eye:C.gfp;x.lineWidth=3;x.beginPath();x.moveTo(X-5,Y+50);x.lineTo(X,Y+50);x.stroke();x.lineWidth=1;}
      x.fillStyle=bad?'rgba(240,96,77,.18)':'#efe6d2';rr(x,X,Y,bw-5,100,8);x.fill();txt(x,(i+1)+'. '+r.step,X+(bw-5)/2,Y-8,{a:'center',s:12,w:700});
      txt(x,c.field,X+10,Y+24,{s:11,c:'#6a5a50'});txt(x,r.v,X+10,Y+46,{s:14,w:700,c:isFake?'#c0301f':'#3a3040'});txt(x,'h '+r.h.slice(0,8),X+10,Y+84,{s:11,c:'#6a5a50'});});
    txt(x,d?d+'단계에서 앞 단계 기록과 어긋남 → 바꿔치기 발견':(lie?'모든 단계가 서로 일치 → 사슬은 정상 (처음 입력이 거짓)':'모든 단계 일치'),20,H-14,{w:700,c:d?C.gfp:(lie?C.eye:C.gfp)});stamp(x,W,'설명용 모형 · 실제 SHA-256');}
  function drawB(dt){t+=dt;var W=fit(c1b,150),H=150,x=c1b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var c=CASES[cs],R=records(cs,swap,lie),ph=REDUCE?4.99:(t*0.6)%6,k=Math.min(4,Math.floor(ph));
    for(var i=0;i<5;i++){var X=60+i*(W-120)/4;x.fillStyle=C.panel2;rr(x,X-40,80,80,26,6);x.fill();txt(x,c.steps[i],X,97,{a:'center',s:11});
      if(i<=k){x.fillStyle=R[i].v===c.fake?'#f3c2bb':'#c9f5dc';rr(x,X-14,110,28,14,3);x.fill();}}
    var bx=60+Math.min(ph,4)*(W-120)/4;x.fillStyle='#d4a54a';rr(x,bx-16,46,32,24,4);x.fill();txt(x,cs==='land'?'등기':'상자',bx,63,{a:'center',s:11,w:700,c:'#13141f'});
    txt(x,'단계를 지날 때마다 기록 블록이 쌓인다',12,20,{s:12,c:C.muted});stamp(x,W,'설명용 장면');}
  function upd(){var R=records(cs,swap,lie),d=detect(R),c=CASES[cs];
    kpis($('#k1'),[['5단계','기록된 이력','a'],[d?d+'단계':'없음','기록이 어긋난 단계',d?'g':'m'],[R[4].v,'최종 '+c.field,R[4].v===c.fake?'r':'g'],[d?'발견':(R[4].v===c.fake?'못 찾음':'—'),'가짜 탐지',d?'g':(R[4].v===c.fake?'r':'a')]]);
    $('#eq1').innerHTML='탐지 = 어떤 단계 <b>i</b>에서 <em>'+c.field+'(i) ≠ '+c.field+'(i−1)</em> 또는 <i>해시 연결 불일치</i>';
    var m=[];if(swap&&!lie)m.push(['g','4단계에서 '+c.field+'이(가) 바뀌어 3단계 기록과 어긋나 바로 드러났어요.']);
    if(lie)m.push(['r','1단계부터 거짓으로 입력하면 모든 단계가 그 거짓을 이어받아 서로 일치해요. 블록체인은 이 거짓도 그대로 지켜요.']);
    if(!swap&&!lie)m.push(['g','지금은 다섯 단계 기록이 모두 일치해요. 바꿔치기나 거짓 입력을 시도해 보세요.']);ins($('#ins1'),m);drawA();drawB(0);}
  mod(c1b,drawB,true);addEventListener('resize',upd);upd();})();

/* ② 즉각 확인 */
(function(){var c2=$('#c2'),c2b=$('#c2b'),n=100,f=0.02,c=0.7,t=0,PAPER=20,LOOK=1;
  slider('r2n',function(v){n=v;upd();});slider('r2f',function(v){f=v/100;upd();});slider('r2c',function(v){c=v/100;upd();});
  function drawA(){var W=fit(c2,200),H=200,x=c2.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);var rows=[['종이 증빙',n*PAPER,n*f*(1-c),C.eye],['블록체인 조회',n*LOOK,0,C.gfp]],L=130,bw=W-L-220,max=500*PAPER;
    rows.forEach(function(r,i){var y=40+i*70;txt(x,r[0],12,y+16,{w:700});x.fillStyle=r[3];rr(x,L,y,Math.max(2,bw*r[1]/max),22,5);x.fill();txt(x,fmt(r[1])+'분',L+Math.max(2,bw*r[1]/max)+8,y+16,{s:12,w:700});
      txt(x,'통과한 위조 서류 '+r[2].toFixed(1)+'건/일',L,y+42,{s:11,c:r[2]>0?C.eye:C.gfp});});
    txt(x,'건당 확인 시간: 종이 20분, 조회 1분 (예시값)',12,H-10,{s:11,c:C.muted});stamp(x,W,'예시값');}
  function drawB(dt){t+=dt;var W=fit(c2b,170),H=170,x=c2b.getContext('2d');x.clearRect(0,0,W,H);grid(x,W,H);
    [['종이 서류 창구',0.15,C.eye],['블록체인 조회 창구',3,C.gfp]].forEach(function(r,i){var Y=40+i*64;txt(x,r[0],12,Y-8,{s:12,w:700,c:r[2]});x.fillStyle=C.panel2;rr(x,W-110,Y,90,36,6);x.fill();txt(x,'창구',W-65,Y+23,{a:'center',s:12});
      var q=REDUCE?0:(t*r[1])%1;for(var k=0;k<8;k++){var X=20+k*((W-160)/8)+q*((W-160)/8);if(X<W-120)drawSprite(x,[SPR.a,SPR.b,SPR.c][k%3],X,Y+18,2);}});
    stamp(x,W,'설명용 장면');}
  function upd(){var pm=n*PAPER,lm=n*LOOK,fake=n*f*(1-c);
    kpis($('#k2'),[[fmt(pm)+'분','종이 증빙 하루 확인 시간','r'],[fmt(lm)+'분','블록체인 조회 하루 확인 시간','g'],[fake.toFixed(1)+'건','통과한 위조 서류/일 (종이)',fake>0?'r':'g'],['0건','기록된 뒤의 위조 통과 (조회)','g']]);
    $('#eq2').innerHTML='통과한 위조 = <b>'+n+'</b> × <i>'+f.toFixed(2)+'</i> × (1 − <em>'+c.toFixed(1)+'</em>) = <b>'+fake.toFixed(2)+'</b>건/일';
    ins($('#ins2'),[['g','블록체인 조회는 기록된 뒤에 바뀌지 않았음이 보장돼, 위조 서류 대조 단계가 없어요. 하루 '+fmt(pm-lm)+'분을 아껴요(예시값).'],['a','하지만 처음 등록할 때 잘못 들어간 정보는 조회로도 걸러지지 않아요(①칸).']]);drawA();drawB(0);}
  mod(c2b,drawB,true);addEventListener('resize',upd);upd();})();

function duelRun(chain){var caught=0;for(var i=0;i<100;i++){var mid=i<60,R=records('fish',mid,!mid);if(chain){if(detect(R))caught++;}else{/* 최종 라벨만: 둘 다 "수입산" 라벨이 그럴듯하게 붙어 있다고 가정 → 통과 */}}return caught;}
Duel({names:{fly:'초파리 (단계별 기록)',robo:'Money-Robo (최종 라벨)'},higherIsBetter:true,drawMargin:0,
  run:function(){return {fly:duelRun(true),robo:duelRun(false)};},bar:function(v){return v/100;},fmt:function(v){return v+'상자';},
  lesson:'단계마다 기록해야 중간 바꿔치기를 잡는다',
  say:function(r){return '찾아낸 가짜 상자는 초파리 쪽 '+r.fly+'상자, Money-Robo 쪽 '+r.robo+'상자예요. 초파리 쪽도 처음부터 거짓으로 입력된 40상자는 못 찾았어요.';}});
}});
