# best: 89(jailctf merger) / others: 95(xsot ovs att joking mewheni), 99(4atj sisyphus luke Seek mukundan), 101(intgrah jimboko awu macaque sammyuri), 108(natte), 117(kabutack)
# ========================================== 89 =========================================
# p=lambda g,E=enumerate:[[(sum([0,*s,0][j:j+3]+[0,*t,0][i:i+3])==2*s[j]>0)or s[j]for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,E=enumerate:[[sum([0,*s][j:j+3:2]+[0,*t][i:i+3:2])<s[j]or s[j]for j,t in E(zip(*g))]for i,s in E(g)]
# lambda g,E=enumerate:[[sum([0,*s][j:j+3]+[0,*t][i:i+3])<3*s[j]or s[j]for j,t in E(zip(*g))]for i,s in E(g)]
p=lambda g,c=35:-c*g or[*zip(*eval(str(p(g,c-1)).replace(*[f"1, {1+c%3}","2","2,2","1"][c<1::2])))][::-1]












