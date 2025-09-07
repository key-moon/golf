# best: 84(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, jailctf merger) / others: 87(xsot ovs att joking mewheni), 92(kabutack), 92(intgrah jimboko awu macaque sammyuri), 93(mukundan), 117(natte)
# ======================================= 84 =======================================
# lambda g,E=enumerate:[[(s[j]and any([0,*s][j:j+3:2]+[0,*t][i:i+3:2]))*8or s[j]for j,t in E(zip(*g))]for i,s in E(g)]
# lambda g,E=enumerate:[[(sum([0,*s][j:j+3]+[0,*t][i:i+3])>2*s[j]>0)*8or s[j]for j,t in E(zip(*g))]for i,s in E(g)]
# lambda g,E=enumerate:[[(sum([0,*s][j:j+3]+[0,*t][i:i+3])>2*s[j]>0)*5+s[j]for j,t in E(zip(*g))]for i,s in E(g)]
# port re;p=lambda g,c=-7:c*g or[*zip(*eval(re.sub("3, [38]","8,8",str(p(g,c+1)))))][::-1]
# lambda g,E=enumerate:[[(sum([0,*s][j:j+3]+[0,*t][i:i+3])>2*s[j]>0)*5+s[j]for j,t in E(zip(*g))]for i,s in E(g)]
# lambda g,c=35:-c*g or[(l:=0)or[l*v*(0<(l:=v))for v in s]for s in zip(*p(g,c-1))][::-1]
p=lambda g,c=35:-c*g or[*zip(*eval(str(p(g,c-1)).replace(f"3, {3+c%7}","8,8")))][::-1]
