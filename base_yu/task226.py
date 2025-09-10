# best: 142(jailctf merger) / others: 149(4atj sisyphus luke Seek mukundan), 159(xsot ovs att joking mewheni), 160(natte), 169(MasukenSamba), 175(jacekwl)
# =================================================================== 142 ====================================================================
# p=lambda g,E=enumerate:[[s[j]or(x:=sum(s[:j]),y:=sum(t[:i]),a:=sum(s),b:=sum(t))and((x==y==0)+(x*2==a and y*2==b)*2+(x==a and y==b)*3)for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,E=enumerate:[[s[j]or sum(-~k*(sum(s[:j])*2==k*sum(s)and sum(t[:i])*2==k*sum(t))for k in range(3))for j,t in E(zip(*g))]for i,s in E(g)]
p=lambda g,E=enumerate:[[s[j]or sum(-~k*(sum(s[:j])*2==k*sum(s))*(sum(t[:i])*2==k*sum(t))for k in(0,1,2))for j,t in E(zip(*g))]for i,s in E(g)]










