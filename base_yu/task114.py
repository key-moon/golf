# best: 64(4atj sisyphus luke Seek mukundan) / others: 65(mukundan), 65(HashPanda), 65(jacekwl Potatoman), 65(xsot ovs att joking mewheni), 65(Yuchen20)
# ============================= 64 =============================
# p=lambda g:(u:=[*zip(*g)])and[[0,*g[0],0],*[*zip(*(u[:1]+u+u[-1:]))],[0,*g[-1],0]]
p=lambda g:[[0,*g[0],0],*[s[:1]+s+s[-1:]for s in g],[0,*g[-1],0]]
