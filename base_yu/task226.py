# best: 133(jailctf merger, JRKKX) / others: 139(HIMAGINE THE FUTURE.), 143(import itertools), 143(biz), 147(THUNDER THUNDER), 149(Code Golf International)
# =============================================================== 133 ===============================================================
# p=lambda g,E=enumerate:[[s[j]or(x:=sum(s[:j]),y:=sum(t[:i]),a:=sum(s),b:=sum(t))and((x==y==0)+(x*2==a and y*2==b)*2+(x==a and y==b)*3)for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,E=enumerate:[[s[j]or sum(-~k*(sum(s[:j])*2==k*sum(s)and sum(t[:i])*2==k*sum(t))for k in range(3))for j,t in E(zip(*g))]for i,s in E(g)]
p=lambda g,E=enumerate:[[s[j]or sum(-~k*(sum(s[:j])*2==k*sum(s))*(sum(t[:i])*2==k*sum(t))for k in(0,1,2))for j,t in E(zip(*g))]for i,s in E(g)]
