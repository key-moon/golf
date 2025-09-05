# best: 101(luke/sisyphus/Seek, sisyphus) / others: 102(joking+MWI), 102(joking/MWI), 102(joking), 104(mukundan), 135(MeWhenI)
# =============================================== 101 ===============================================
# p=lambda g,c=-3:c*g or p([[v or(3in s[:i])*max(s[i:])for i,v in enumerate(s)]for s in zip(*g[::-1])],c+1)
p=lambda g,c=-3:c*g or p([[s[i]or(3in s[:i])*max(s[i:])for i in range(10)]for s in zip(*g[::-1])],c+1)
