# best: 55(jailctf merger, 4atj sisyphus luke Seek mukundan) / others: 57(ox jam), 57(intgrah jimboko awu macaque sammyuri), 65(cubbus), 72(jacekw Potatoman nauti natte), 72(import itertools)
# lambda g:[p,list][g==(a:=[*zip(*[g:=r for r in g if g!=r])])](a)
# lambda g:[list,p][g*0==[]]((*zip(*[g:=r for r in g if g!=r]),))
# lambda g,c=-2:g*c or p([*zip(*[g:=r for r in g if g!=r])],c+1)
# lambda g,f=lambda x:[x:=s for s in x if s!=x]:f(zip(*f(g)))
# lambda g,c=2:c and[g:=s for s in p(zip(*g),c-1)if s!=g]or g
# 類題: 218
# ========================= 55 ========================
p=lambda g,c=-1:g*c or[g:=r for r in zip(*p(g,c+1))if g!=r]
