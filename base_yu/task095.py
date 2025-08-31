# best: 80(sisyphus) / others: 81(luke), 86(4atj), 87(mukundan), 90(natte), 92(joking+MWI)
# ===================================== 80 =====================================
# p=lambda g,c=-3:c*g or p([[y or x>0for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
p=lambda g,c=-3,l=0:c*g or p([[(l>0)|(l:=y)for y in s]for s in zip(*g[::-1])],c+1)
