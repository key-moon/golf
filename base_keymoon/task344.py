# best: 78(sisyphus) / others: 87(mukundan), 87(luke), 95(natte), 99(Seek64), 116(joking+MWI)
# ==================================== 78 ====================================
p=lambda g,c=-3:c*g or p([*zip(*eval(str(g).replace("3, 2","8,0"))[::-1])],c+1)
