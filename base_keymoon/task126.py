# best: 54(ox jam, jailctf merger, xsot ovs att joking mewheni) / others: 56(4atj sisyphus luke Seek mukundan), 56(intgrah jimboko awu macaque sammyuri), 56(HETHAT), 58(JRKX), 58(jacekw Potatoman nauti)
# lambda g:g[:-1]+[[4-4*(sum(r)<1or sum(r)/max(r)>1) for r in zip(*g)]]
# lambda g:g[:-1]+[[4*(len(r)-r.count(0)&1)for r in zip(*g)]]
# lambda g:g[:-1]+[[len(r)-r.count(0)<<2&4for r in zip(*g)]]
# lambda g:g[:-1]+[[4*(r.count(max(r))<2)for r in zip(*g)]]
# lambda g:g[:-1]+[[4*(sum(r)-2*max(r)<0)for r in zip(*g)]]
# lambda g:g[:-1]+[[4*(sum(r)==max(r)>0)for r in zip(*g)]]
# ======================== 54 ========================
p=lambda g:g[:-1]+[[4*(sum(r)==max(r)>0)for r in zip(*g)]]
