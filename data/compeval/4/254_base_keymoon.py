# 類題:10
# best: 99(luke/sisyphus/Seek, Seek64) / others: 107(sisyphus), 108(mukundan), 110(joking+MWI), 110(joking/MWI), 110(joking)
# =============================================== 99 ==============================================
p=lambda g,Z=zip:[*Z(*[[v and(s==(a:=sorted({*Z(*g)}))[1])*2+(s==a[-1])for v in s]for s in Z(*g)])]

# 101
# def p(g):
#  *a,b=sorted({*zip(*g)})
#  return[*zip(*[[v and(s==a[1])*2+(s==b)for v in s]for s in zip(*g)])]
# #return[[c and(t==a[1])*2+(t==b)for c,t in zip(r,zip(*g))] for r in g]
# #return[[c and(t==[*a[1]])*2+(t==[*b])for*t,c in zip(*g,r)] for r in g]
