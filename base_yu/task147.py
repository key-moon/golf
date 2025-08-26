# best: 84(luke, luke/sisyphus/Seek) / others: 85(4atj), 88(joking+MWI), 88(joking/MWI), 88(joking), 88(sisyphus)
# ======================================= 84 =======================================
p=lambda g,E=enumerate:[[(s[j]and any([0,*s][j:j+3:2]+[0,*t][i:i+3:2]))*8or s[j]for j,t in E(zip(*g))]for i,s in E(g)]
