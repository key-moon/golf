# best: 43(ShadowPrompt Labs, jailctf merger, natte, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, kambarakun, intgrah jimboko awu macaque sammyuri, biz, adakoda, jacekw Potatoman nauti, import itertools) / others: 44(ox jam), 44(MasukenSamba), 44(Ravi Annaswamy), 47(kabutack), 47(Tony Li)
# lambda g:g[:2]+[*zip(*[2*(a:=g[0])]*len(a))]
# lambda g:g[:2]+[*zip(*[g[0]*2]*len(g[0]))]
# =================== 43 ==================
#p=lambda g:g[:2]+[*zip(*[g[0]*2]*len(g[0]))]
#p=lambda g:g[:2]+[*zip(*[g[0]]*len(g[0]))]*2
#p=lambda g:g[:2]+[*zip(*[a:=g[0]]*len(a))]*2
p=lambda g:g[:2]+[*zip(*g[:1]*len(g[0]))]*2
