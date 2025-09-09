# best: 57(jailctf merger) / others: 62(xsot ovs att joking mewheni), 63(4atj sisyphus luke Seek mukundan), 66(intgrah jimboko awu macaque sammyuri), 71(biz), 74(HETHAT)
# ========================== 57 =========================
# p=lambda g:g*0!=0and[p(g:=r)for r in g if r!=g][::2]or g
p=lambda g:g*-1*-1or[p(g:=r)for r in g if r!=g][::2]

