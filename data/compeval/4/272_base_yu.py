# best: 101(ovs) / others: 103(mukundan), 108(natte), 109(luke/sisyphus/Seek), 109(sisyphus), 113(Seek64)
# =============================================== 101 ===============================================
# p=lambda g,E=enumerate:[[(sum([0,*s,0][j:j+3]+[0,*t,0][i:i+3])==2*s[j]>0)or s[j]for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,E=enumerate:[[sum([0,*s][j:j+3:2]+[0,*t][i:i+3:2])<s[j]or s[j]for j,t in E(zip(*g))]for i,s in E(g)]
p=lambda g,E=enumerate:[[sum([0,*s][j:j+3]+[0,*t][i:i+3])<3*s[j]or s[j]for j,t in E(zip(*g))]for i,s in E(g)]
