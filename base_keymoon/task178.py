# best: 47(Code Golf International, LogicLynx, jailctf merger, HIMAGINE THE FUTURE., ox jam, intgrah jimboko awu macaque sammyuri) / others: 50(lv1.dev), 50(FuunAgent), 51(santa2024), 52(import itertools), 53(ALE-Agent)
# 転地佐伯テクだけでこんだけ食うから転地佐伯ではない
# lambda g:5>len(g)and[*map(list,zip(*g))]or []
# lambda g,s=0:[(s:=r)*0!=r*0and p(r)or r for r in g if r!=s]
# lambda g,s=0:[(s:=r)*0!=0and p(r)or r for r in g if r!=s]
# lambda g:[[int,p][(g:=r)*0!=0](r)for r in g if r!=g]
# ===================== 47 ====================
# p=lambda g:g*0!=0and[p(g:=r)for r in g if r!=g]or g
p=lambda g:g*-1*-1or[p(g:=r)for r in g if r!=g]
