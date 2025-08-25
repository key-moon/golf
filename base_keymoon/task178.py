# best: 55(luke, 4atj, sisyphus) / others: 59(dbdr), 64(joking), 65(ovs), 66(mukundan), 71(natte)
# 転地佐伯テクだけでこんだけ食うから転地佐伯ではない
# lambda g:5>len(g)and[*map(list,zip(*g))]or []
# lambda g,s=0:[(s:=r)*0!=r*0and p(r)or r for r in g if r!=s]
# lambda g,s=0:[(s:=r)*0!=0and p(r)or r for r in g if r!=s]
# lambda g:[[int,p][(g:=r)*0!=0](r)for r in g if r!=g]
# ========================= 55 ========================
p=lambda g:g*0!=0and[p(g:=r)for r in g if r!=g]or g
