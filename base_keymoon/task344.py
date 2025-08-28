# best: 78(sisyphus) / others: 87(mukundan), 87(luke), 95(natte), 99(Seek64), 116(joking+MWI)
# ==================================== 78 ====================================
# p=lambda g,c=4:c and p([[y or(x==1)for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c-1)or g
# import re;p=lambda g,c=4:c and p([*zip(*eval(re.sub("3, 2","8,0",str(g)))[::-1])],c-1)or g
p=lambda g,c=-3:c*g or p([*zip(*eval(str(g).replace("3, 2","8,0"))[::-1])],c+1)
