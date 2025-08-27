# best: 92(4atj sisyphus luke Seek, luke/sisyphus/Seek, sisyphus) / others: 96(4atj), 98(mukundan), 99(joking+MWI), 99(joking/MWI), 99(joking)
# =========================================== 92 ===========================================
# p=lambda g,c=-1:c*g or p([[s[i]or(12<sum(s[:i])+6<sum(s))*3for i in range(len(s))]for s in zip(*g)],c+1)
p=lambda g,c=-1:c*g or p([[s[i]or(8in s[:i])*(8in s[i:])*3for i in range(len(s))]for s in zip(*g)],c+1)
