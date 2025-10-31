# best: 54(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, lv1.dev, LogicLynx, ALE-Agent, FuunAgent, MasukenSamba, jailctf merger, ox jam) / others: 56(4atj sisyphus luke Seek mukundan), 56(HETHAT), 56(intgrah jimboko awu macaque sammyuri), 57(Tony Li), 57(Tony Li & Darren Amadeus Martin)
# lambda g:g[:-1]+[[4-4*(sum(r)<1or sum(r)/max(r)>1) for r in zip(*g)]]
# lambda g:g[:-1]+[[4*(len(r)-r.count(0)&1)for r in zip(*g)]]
# lambda g:g[:-1]+[[len(r)-r.count(0)<<2&4for r in zip(*g)]]
# lambda g:g[:-1]+[[4*(r.count(max(r))<2)for r in zip(*g)]]
# lambda g:g[:-1]+[[4*(sum(r)-2*max(r)<0)for r in zip(*g)]]
# lambda g:g[:-1]+[[4*(sum(r)==max(r)>0)for r in zip(*g)]]
# ======================== 54 ========================
p=lambda g:g[:-1]+[[4*(sum(r)==max(r)>0)for r in zip(*g)]]
