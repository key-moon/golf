# best: 49(xsot ovs att joking mewheni, xsot ovs att, jailctf merger) / others: 55(luke), 55(4atj), 55(HETHAT), 55(4atj sisyphus luke Seek), 55(sisyphus)
# 転地佐伯テクだけでこんだけ食うから転地佐伯ではない
# lambda g:5>len(g)and[*map(list,zip(*g))]or []
# lambda g,s=0:[(s:=r)*0!=r*0and p(r)or r for r in g if r!=s]
# lambda g,s=0:[(s:=r)*0!=0and p(r)or r for r in g if r!=s]
# lambda g:[[int,p][(g:=r)*0!=0](r)for r in g if r!=g]
# ====================== 49 =====================
# p=lambda g:g*0!=0and[p(g:=r)for r in g if r!=g]or g
p=lambda g:g*-1and g or[p(g:=r)for r in g if r!=g]
