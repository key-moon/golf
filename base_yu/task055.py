# best: 87(4atj) / others: 93(mukundan), 101(luke), 101(luke/sisyphus/Seek), 104(joking+MWI), 104(joking/MWI)
# ========================================= 87 ========================================
# p=lambda g,E=enumerate:[[s[j]or[0,2,0,4,6,3,0,1,0][(sum(s[:j])+sum(t[:i])*3)//8] for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,E=enumerate:[[s[j]or[0,4,0,2,6,1,0,3,0][(sum(s[:j])*3+sum(t[:i]))//8]for j,t in E(zip(*g))]for i,s in E(g)]
p=lambda g,E=enumerate:[[s[j]or b""[(sum(s[:j])*3+sum(t[:i]))//8]-1for j,t in E(zip(*g))]for i,s in E(g)]

# 020
# 463
# 010
