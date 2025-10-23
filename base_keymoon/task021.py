# best: 57(jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 58(import itertools), 59(jacekw Potatoman nauti natte), 59(natte), 62(cubbus), 62(ox jam)
# ========================== 57 =========================
# p=lambda g:g*0!=0and[p(g:=r)for r in g if r!=g][::2]or g
p=lambda g:g*-1*-1or[p(g:=r)for r in g if r!=g][::2]
