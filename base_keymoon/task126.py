# best: 54(MasukenSamba, jailctf merger, ox jam) / others: 56(4atj sisyphus luke Seek mukundan), 56(HETHAT), 56(intgrah jimboko awu macaque sammyuri), 57(ShadowPrompt Labs), 57(Tony Li)
# lambda g:g[:-1]+[[4-4*(sum(r)<1or sum(r)/max(r)>1) for r in zip(*g)]]
# lambda g:g[:-1]+[[4*(len(r)-r.count(0)&1)for r in zip(*g)]]
# lambda g:g[:-1]+[[len(r)-r.count(0)<<2&4for r in zip(*g)]]
# lambda g:g[:-1]+[[4*(r.count(max(r))<2)for r in zip(*g)]]
# lambda g:g[:-1]+[[4*(sum(r)-2*max(r)<0)for r in zip(*g)]]
# lambda g:g[:-1]+[[4*(sum(r)==max(r)>0)for r in zip(*g)]]
# ======================== 54 ========================
p=lambda g:g[:-1]+[[4*(sum(r)==max(r)>0)for r in zip(*g)]]
