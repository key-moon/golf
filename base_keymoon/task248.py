# best: 67(FuunAgent) / others: 68(LogicLynx), 72(Code Golf International), 72(ALE-Agent), 72(jailctf merger), 73(biz)
# [1,-1][i in(0,len(r)-1)]
# (1-(i in(0,len(r)-1))*2)
# [1,-1][i%(len(r)-1)<1]
# 1-(i%(len(r)-1)<1)*2
# =============================== 67 ==============================
def p(g,i=0,d=1):
 for r in g[::-1]:r[i]=1;i+=d;d*=1-(i%(len(r)-1)<1)*2
 return g
