# best: 64(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, jailctf merger) / others: 67(dbdr), 67(xsot ovs att joking mewheni), 69(biz), 69(mukundan), 72(kabutack)
# ============================= 64 =============================
# p=lambda g:(n:=len(g)//2)and[[g[n][g[n].index(v)+n]for v in s]for s in g]
p=lambda g:[[g[n:=len(g)//2][s.index(v)+n]for v in s]for s in g]
