# best: 56(jailctf merger) / others: 57(4atj sisyphus luke Seek mukundan), 58(intgrah jimboko awu macaque sammyuri), 58(xsot ovs att joking mewheni), 64(natte), 64(2F)
# lambda g:[[g[i//2|1][j//2|1] for j in range(len(g[0])*2)] for i in range(len(g)*2)]
# lambda g:sum([[[int,p][r*0!=0](r)]*4for r in g[1::2]],[])
# ========================= 56 =========================
p=lambda g:g*0!=0and sum([[p(r)]*4for r in g[1::2]],[])or g


