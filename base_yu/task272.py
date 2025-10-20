# best: 89(jailctf merger) / others: 95(ox jam), 99(Code Golf International), 99(4atj sisyphus luke Seek mukundan), 99(biz), 100(intgrah jimboko awu macaque sammyuri)
# ========================================== 89 =========================================
# p=lambda g,E=enumerate:[[(sum([0,*s,0][j:j+3]+[0,*t,0][i:i+3])==2*s[j]>0)or s[j]for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,E=enumerate:[[sum([0,*s][j:j+3:2]+[0,*t][i:i+3:2])<s[j]or s[j]for j,t in E(zip(*g))]for i,s in E(g)]
# lambda g,E=enumerate:[[sum([0,*s][j:j+3]+[0,*t][i:i+3])<3*s[j]or s[j]for j,t in E(zip(*g))]for i,s in E(g)]
# lambda g,c=35:-c*g or[*zip(*eval(str(p(g,c-1)).replace(*[f"1, {1+c%3}","2","2,2","1"][c<1::2])))][::-1]
p=lambda g,c=7:-c*g or[(l:=0)or[l:=v and[l+v,1+(3<v)][6<c]for v in s]for s in zip(*p(g,c-1))][::-1]
