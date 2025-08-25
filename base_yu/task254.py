# 類題:10
# best: 99(Seek64) / others: 107(sisyphus), 108(mukundan), 110(joking+MWI), 110(joking), 112(natte)
# =============================================== 99 ==============================================
# p=lambda g:[u:=sorted({*zip(*g)}-{(0,)*9},key=sum)]and[*zip(*[[v and(s==u[0])*2+(s==u[-1])for v in s]for s in zip(*g)])]
def p(g):
 _,a,*_,b=sorted({*zip(*g)},key=sum)
 return[*zip(*[[v and(s==a)*2+(s==b)for v in s]for s in zip(*g)])]
#  return[[x and(t==a)*2+(t==b)for x,t in zip(s,zip(*g))]for s in g]
