# best: 57(jailctf merger) / others: 59(natte), 62(ox jam), 62(cubbus), 62(xsot ovs att joking mewheni), 63(4atj sisyphus luke Seek mukundan)
# ========================== 57 =========================
# p=lambda g:g*0!=0and[p(g:=r)for r in g if r!=g][::2]or g
p=lambda g:g*-1*-1or[p(g:=r)for r in g if r!=g][::2]
