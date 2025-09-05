# best: 95(4atj) / others: 96(sisyphus), 98(mukundan), 101(joking+MWI), 101(joking), 111(Seek64)
# ============================================= 95 ============================================
p=lambda g,c=-1:c*g or p([[v or(1in s[:i])*(1in s[i:])*8for i,v in enumerate(s)]for s in zip(*g)],c+1)
