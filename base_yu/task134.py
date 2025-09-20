# best: 168(biz, jailctf merger) / others: 174(ox jam), 181(jacekwl Potatoman nauti), 186(4atj sisyphus luke Seek mukundan), 208(xsot ovs att joking mewheni), 211(JRKX)
# ================================================================================ 168 =================================================================================
def p(g):
 _,n,m={*sum(g,[])}
 if 5<str(g).count(f"{n}, "*2):n,m=m,n
 u=[s for s in g if m in s]
 k=len(u)//3
 return[[n*(v==m)for*t,v in zip(*g,s)if m in t][::k]for s in u[::k]]
