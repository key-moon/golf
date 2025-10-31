# 類題:10
# best: 81(Code Golf International) / others: 84(jailctf merger), 87(import itertools), 91(4atj sisyphus luke Seek mukundan), 91(ox jam), 93(FuunAgent)
# ====================================== 81 =====================================
p=lambda g,Z=zip:[*Z(*[[v and(s==(a:=sorted({*Z(*g)}))[1])*2+(s==a[-1])for v in s]for s in Z(*g)])]

# 101
# def p(g):
#  *a,b=sorted({*zip(*g)})
#  return[*zip(*[[v and(s==a[1])*2+(s==b)for v in s]for s in zip(*g)])]
# #return[[c and(t==a[1])*2+(t==b)for c,t in zip(r,zip(*g))] for r in g]
# #return[[c and(t==[*a[1]])*2+(t==[*b])for*t,c in zip(*g,r)] for r in g]
