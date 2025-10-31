# best: 43(jacekw Potatoman nauti natte, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, lv1.dev, LogicLynx, ALE-Agent, jacekw Potatoman nauti, FuunAgent, natte, kambarakun, import itertools, jailctf merger, HIMAGINE THE FUTURE., adakoda, ox jam, biz, intgrah jimboko awu macaque sammyuri) / others: 44(Ravi Annaswamy), 44(MasukenSamba), 44(Tony Li & Darren Amadeus Martin), 47(jonas ryno kg583 kabutack), 47(cubbus)
# lambda g:g[:2]+[*zip(*[2*(a:=g[0])]*len(a))]
# lambda g:g[:2]+[*zip(*[g[0]*2]*len(g[0]))]
# =================== 43 ==================
#p=lambda g:g[:2]+[*zip(*[g[0]*2]*len(g[0]))]
#p=lambda g:g[:2]+[*zip(*[g[0]]*len(g[0]))]*2
#p=lambda g:g[:2]+[*zip(*[a:=g[0]]*len(a))]*2
p=lambda g:g[:2]+[*zip(*g[:1]*len(g[0]))]*2
