# best: 152(jailctf merger, biz) / others: 173(import itertools), 174(ox jam), 176(HIMAGINE THE FUTURE.), 181(jacekwl Potatoman nauti), 181(jacekw Potatoman nauti natte)
# ======================================================================== 152 =========================================================================
def p(g):
 _,n,m={*sum(g,[])}
 if 5<str(g).count(f"{n}, "*2):n,m=m,n
 u=[s for s in g if m in s]
 k=len(u)//3
 return[[n*(v==m)for*t,v in zip(*g,s)if m in t][::k]for s in u[::k]]
