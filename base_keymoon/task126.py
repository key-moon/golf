# best: 56(luke) / others: 57(att), 58(joking+MWI), 58(kg583), 58(mukundan), 58(joking)
# lambda g:g[:-1]+[[4-4*(sum(r)<1or sum(r)/max(r)>1) for r in zip(*g)]]
# lambda g:g[:-1]+[[4*(len(r)-r.count(0)&1)for r in zip(*g)]]
# lambda g:g[:-1]+[[len(r)-r.count(0)<<2&4for r in zip(*g)]]
# lambda g:g[:-1]+[[4*(r.count(max(r))<2)for r in zip(*g)]]
# lambda g:g[:-1]+[[4*(sum(r)-2*max(r)<0)for r in zip(*g)]]
# lambda g:g[:-1]+[[4*(sum(r)==max(r)>0)for r in zip(*g)]]
# ========================= 56 =========================
p=lambda g:g[:-1]+[[4*(sum(r)==max(r)>0)for r in zip(*g)]]