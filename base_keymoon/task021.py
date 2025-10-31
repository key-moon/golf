# best: 51(LogicLynx, ox jam) / others: 52(Code Golf International), 52(jailctf merger), 52(HIMAGINE THE FUTURE.), 54(lv1.dev), 54(FuunAgent)
# ======================= 51 ======================
# p=lambda g:g*0!=0and[p(g:=r)for r in g if r!=g][::2]or g
p=lambda g:g*-1*-1or[p(g:=r)for r in g if r!=g][::2]
