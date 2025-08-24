# best: 55(luke, 4atj, sisyphus) / others: 58(mukundan), 59(joking+MWI), 64(joking), 65(ovs), 75(natte)
# lambda g:[p,list][g==(a:=[*zip(*[g:=r for r in g if g!=r])])](a)
# lambda g:[list,p][g*0==[]]((*zip(*[g:=r for r in g if g!=r]),))
# lambda g,c=-2:g*c or p([*zip(*[g:=r for r in g if g!=r])],c+1)
# ========================= 55 ========================
p=lambda g,f=lambda x:[x:=s for s in x if s!=x]:f(zip(*f(g)))
