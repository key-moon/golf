# best: 123(mukundan) / others: 130(xsot ovs att joking mewheni), 141(jailctf merger), 196(Jonas), 223(jacekw), 224(jacekwl)
# ========================================================== 123 ==========================================================
# def p(g):
#  for w in range(6):
#   x,y=w%3,w//3+2
#   u=[([0]*(i//y*x)+g[i%y])[:10]for i in range(10)]
#   if g==u[:len(g)]:
#    return u

p=lambda g,c=5:((u:=[([0]*(i//(y:=c%2+2)*(c//2))+g[i%y])[:10]for i in range(10)])[:len(g)]==g)*u or p(g,c-1)


# def p(g):
#  h=len(g)
#  for x in range(4):
#   for y in range(2,4):
#    ok=1
#    for i in range(y,h):
#     for j in range(x,10):
#      ok&=g[i][j]==g[i-y][j-x]
#    if ok:
#     for i in range(h,10):
#      g+=[[0]*(i//y*x)+g[i%y][:10-i//y*x]]
#     return g
