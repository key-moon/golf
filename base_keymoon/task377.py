# best: 55(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 57(intgrah jimboko awu macaque sammyuri), 57(xsot ovs att joking mewheni), 73(jacekwl Potatoman nauti), 75(natte), 92(jonas ryno kg583)
# lambda g:[p,list][g==(a:=[*zip(*[g:=r for r in g if g!=r])])](a)
# lambda g:[list,p][g*0==[]]((*zip(*[g:=r for r in g if g!=r]),))
# lambda g,c=-2:g*c or p([*zip(*[g:=r for r in g if g!=r])],c+1)
# lambda g,f=lambda x:[x:=s for s in x if s!=x]:f(zip(*f(g)))
# lambda g,c=2:c and[g:=s for s in p(zip(*g),c-1)if s!=g]or g
# 類題: 218
# ========================= 55 ========================
p=lambda g,c=-1:g*c or[g:=r for r in zip(*p(g,c+1))if g!=r]










