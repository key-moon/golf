# best: 85(sisyphus) / others: 92(natte), 94(luke), 105(mukundan), 112(kabutack), 114(xsot)
# ======================================== 85 =======================================
# p=lambda g,c=4:c and p([[y or 0<x<3for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c-1)or g
p=lambda g,c=-3:c*g or p([[y or 0<x<3for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
