# best: 52(HIMAGINE THE FUTURE.) / others: 57(jailctf merger), 58(import itertools), 59(jacekw Potatoman nauti natte), 59(natte), 62(cubbus)
# ======================= 52 =======================
# p=lambda g:g*0!=0and[p(g:=r)for r in g if r!=g][::2]or g
p=lambda g:g*-1*-1or[p(g:=r)for r in g if r!=g][::2]
