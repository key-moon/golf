# best: 67(4atj sisyphus luke Seek mukundan, rucin93, today, kambarakun, import itertools, Tony Li, jailctf merger, ox jam, biz, JRKKX) / others: 68(Ty Woods), 69(cg-klogw-sekken), 72(jacekw Potatoman nauti natte), 72(Ravi Annaswamy), 72(adakoda)
# lambda g,a=[0]*3,S=[0]*6:[S:=[*map(max,s+a,[0]+S)]for s in g+[a]*3]
# f p(g):S=(b:=[0])*6;return[S:=[*map(max,s+b*3,b+S)]for s in g+[b*3]*3]
# lambda g,S=[0]*6:[S:=[*map(max,s+[0]*9,[0]+S)][:6]for s in g+[S]*3]
# lambda g,S=(b:=[0])*6:[S:=[*map(max,s+b*3,b+S)]for s in g+[b*3]*3]
# =============================== 67 ==============================
p=lambda g,S=(a:=[0]*3)*2:[S:=[*map(max,s+a,[0]+S)]for s in g+[a]*3]
