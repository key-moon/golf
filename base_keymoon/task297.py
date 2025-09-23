# best: 43(4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti, jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 44(ox jam), 44(MasukenSamba), 47(natte), 47(Potatoman), 47(cubbus)
# lambda g:g[:2]+[*zip(*[2*(a:=g[0])]*len(a))]
# lambda g:g[:2]+[*zip(*[g[0]*2]*len(g[0]))]
# =================== 43 ==================
#p=lambda g:g[:2]+[*zip(*[g[0]*2]*len(g[0]))]
#p=lambda g:g[:2]+[*zip(*[g[0]]*len(g[0]))]*2
#p=lambda g:g[:2]+[*zip(*[a:=g[0]]*len(a))]*2
p=lambda g:g[:2]+[*zip(*g[:1]*len(g[0]))]*2
