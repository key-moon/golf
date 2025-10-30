# best: 67(open source, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Krige, Code Golf International, 4atj sisyphus luke Seek mukundan, ShadowPrompt Labs, rucin93, today, cg-klogw-sekken, kambarakun, import itertools, Tony Li, jailctf merger, Tony Li & Darren Amadeus Martin, HIMAGINE THE FUTURE., adakoda, ox jam, THUNDER THUNDER, biz, JRKKX) / others: 68(Ty Woods), 72(jacekw Potatoman nauti natte), 72(Ravi Annaswamy), 74(JRKX), 74(HETHAT)
# lambda g,a=[0]*3,S=[0]*6:[S:=[*map(max,s+a,[0]+S)]for s in g+[a]*3]
# f p(g):S=(b:=[0])*6;return[S:=[*map(max,s+b*3,b+S)]for s in g+[b*3]*3]
# lambda g,S=[0]*6:[S:=[*map(max,s+[0]*9,[0]+S)][:6]for s in g+[S]*3]
# lambda g,S=(b:=[0])*6:[S:=[*map(max,s+b*3,b+S)]for s in g+[b*3]*3]
# =============================== 67 ==============================
p=lambda g,S=(a:=[0]*3)*2:[S:=[*map(max,s+a,[0]+S)]for s in g+[a]*3]
