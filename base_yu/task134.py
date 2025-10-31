# best: 123(ox jam) / others: 142(jailctf merger), 143(biz), 146(Code Golf International), 158(LogicLynx), 165(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# ========================================================== 123 ==========================================================
def p(g):
 _,n,m={*sum(g,[])}
 if 5<str(g).count(f"{n}, "*2):n,m=m,n
 u=[s for s in g if m in s]
 k=len(u)//3
 return[[n*(v==m)for*t,v in zip(*g,s)if m in t][::k]for s in u[::k]]
