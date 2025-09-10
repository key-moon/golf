# best: 47(jailctf merger) / others: 49(xsot ovs att joking mewheni), 53(intgrah jimboko awu macaque sammyuri), 55(4atj sisyphus luke Seek mukundan), 55(HETHAT), 59(dbdr)
# 転地佐伯テクだけでこんだけ食うから転地佐伯ではない
# lambda g:5>len(g)and[*map(list,zip(*g))]or []
# lambda g,s=0:[(s:=r)*0!=r*0and p(r)or r for r in g if r!=s]
# lambda g,s=0:[(s:=r)*0!=0and p(r)or r for r in g if r!=s]
# lambda g:[[int,p][(g:=r)*0!=0](r)for r in g if r!=g]
# ===================== 47 ====================
# p=lambda g:g*0!=0and[p(g:=r)for r in g if r!=g]or g
p=lambda g:g*-1*-1or[p(g:=r)for r in g if r!=g]








