# 類題:10
# best: 84(jailctf merger) / others: 91(4atj sisyphus luke Seek mukundan), 95(ox jam), 101(intgrah jimboko awu macaque sammyuri), 102(jacekw Potatoman nauti natte), 102(biz)
# ======================================= 84 =======================================
p=lambda g,Z=zip:[*Z(*[[v and(s==(a:=sorted({*Z(*g)}))[1])*2+(s==a[-1])for v in s]for s in Z(*g)])]

# 101
# def p(g):
#  *a,b=sorted({*zip(*g)})
#  return[*zip(*[[v and(s==a[1])*2+(s==b)for v in s]for s in zip(*g)])]
# #return[[c and(t==a[1])*2+(t==b)for c,t in zip(r,zip(*g))] for r in g]
# #return[[c and(t==[*a[1]])*2+(t==[*b])for*t,c in zip(*g,r)] for r in g]
