# best: 117(jailctf merger) / others: 119(ox jam), 120(Code Golf International), 132(lv1.dev), 133(intgrah jimboko awu macaque sammyuri), 133(JRKKX)
# ======================================================= 117 =======================================================
# p=lambda g,E=enumerate:[[s[j]or(x:=sum(s[:j]),y:=sum(t[:i]),a:=sum(s),b:=sum(t))and((x==y==0)+(x*2==a and y*2==b)*2+(x==a and y==b)*3)for j,t in E(zip(*g))]for i,s in E(g)]
# p=lambda g,E=enumerate:[[s[j]or sum(-~k*(sum(s[:j])*2==k*sum(s)and sum(t[:i])*2==k*sum(t))for k in range(3))for j,t in E(zip(*g))]for i,s in E(g)]
p=lambda g,E=enumerate:[[s[j]or sum(-~k*(sum(s[:j])*2==k*sum(s))*(sum(t[:i])*2==k*sum(t))for k in(0,1,2))for j,t in E(zip(*g))]for i,s in E(g)]
