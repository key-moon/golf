# best: 84(4atj sisyphus luke Seek, jailctf merger) / others: 87(xsot ovs att joking mewheni), 92(kabutack), 93(mukundan), 117(natte), 119(MasukenSamba)
# ======================================= 84 =======================================
# lambda g,E=enumerate:[[(s[j]and any([0,*s][j:j+3:2]+[0,*t][i:i+3:2]))*8or s[j]for j,t in E(zip(*g))]for i,s in E(g)]
# lambda g,E=enumerate:[[(sum([0,*s][j:j+3]+[0,*t][i:i+3])>2*s[j]>0)*8or s[j]for j,t in E(zip(*g))]for i,s in E(g)]
# lambda g,E=enumerate:[[(sum([0,*s][j:j+3]+[0,*t][i:i+3])>2*s[j]>0)*5+s[j]for j,t in E(zip(*g))]for i,s in E(g)]
# lambda g,c=99:-c*g or[*zip(*eval(str(p(g,c-1)).replace(f"3, {1+c%9}",f"8,{1+c%9}")))][::-1]
import re;p=lambda g,c=-7:c*g or[*zip(*eval(re.sub("3, [38]","8,8",str(p(g,c+1)))))][::-1]
