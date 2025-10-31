# 類題:10
# best: 81(Code Golf International) / others: 84(jailctf merger), 87(import itertools), 91(4atj sisyphus luke Seek mukundan), 91(ox jam), 93(FuunAgent)
# ====================================== 81 =====================================
# p=lambda g:[u:=sorted({*zip(*g)}-{(0,)*9},key=sum)]and[*zip(*[[v and(s==u[0])*2+(s==u[-1])for v in s]for s in zip(*g)])]
def p(g):
 _,a,*_,b=sorted({*zip(*g)})
 return[*zip(*[[v and(s==a)*2+(s==b)for v in s]for s in zip(*g)])]
#  return[[x and(t==a)*2+(t==b)for x,t in zip(s,zip(*g))]for s in g]
