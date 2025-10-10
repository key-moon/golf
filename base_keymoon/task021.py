# best: 57(jailctf merger) / others: 59(jacekw Potatoman nauti natte), 59(natte), 59(import itertools), 60(intgrah jimboko awu macaque sammyuri), 62(cubbus)
# ========================== 57 =========================
# p=lambda g:g*0!=0and[p(g:=r)for r in g if r!=g][::2]or g
p=lambda g:g*-1*-1or[p(g:=r)for r in g if r!=g][::2]
