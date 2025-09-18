# 類題:10
# best: 84(jailctf merger) / others: 91(4atj sisyphus luke Seek mukundan), 101(intgrah jimboko awu macaque sammyuri), 103(ox jam), 103(xsot ovs att joking mewheni), 104(MasukenSamba)
# ======================================= 84 =======================================
# p=lambda g:[u:=sorted({*zip(*g)}-{(0,)*9},key=sum)]and[*zip(*[[v and(s==u[0])*2+(s==u[-1])for v in s]for s in zip(*g)])]
def p(g):
 _,a,*_,b=sorted({*zip(*g)})
 return[*zip(*[[v and(s==a)*2+(s==b)for v in s]for s in zip(*g)])]
#  return[[x and(t==a)*2+(t==b)for x,t in zip(s,zip(*g))]for s in g]
