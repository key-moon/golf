# best: 101(mukundan) / others: 104(joking+MWI), 104(natte), 104(joking/MWI), 104(joking), 105(luke/sisyphus/Seek)
# =============================================== 101 ===============================================

p=lambda g,E=enumerate:[[all([0,*s,0][j:j+3]+[0,*t,0][i:i+3])*8or s[j]for j,t in E(zip(*g))]for i,s in E(g)]
