# best: 52(jailctf merger, HIMAGINE THE FUTURE.) / others: 58(import itertools), 59(jacekw Potatoman nauti natte), 59(natte), 62(cubbus), 62(ox jam)
# ======================= 52 =======================
# p=lambda g:g*0!=0and[p(g:=r)for r in g if r!=g][::2]or g
p=lambda g:g*-1*-1or[p(g:=r)for r in g if r!=g][::2]
