# best: 43(4atj sisyphus luke Seek, jailctf merger, 4atj sisyphus luke Seek mukundan) / others: 44(xsot ovs att joking mewheni), 44(MasukenSamba), 47(Potatoman), 47(jacekwl Potatoman), 47(Yuchen20)
# lambda g:g[:2]+[*zip(*[2*(a:=g[0])]*len(a))]
# lambda g:g[:2]+[*zip(*[g[0]*2]*len(g[0]))]
# =================== 43 ==================
#p=lambda g:g[:2]+[*zip(*[g[0]*2]*len(g[0]))]
#p=lambda g:g[:2]+[*zip(*[g[0]]*len(g[0]))]*2
#p=lambda g:g[:2]+[*zip(*[a:=g[0]]*len(a))]*2
p=lambda g:g[:2]+[*zip(*g[:1]*len(g[0]))]*2
