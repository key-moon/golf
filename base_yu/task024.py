# best: 62(mukundan, 4atj sisyphus luke Seek mukundan, biz, xsot ovs att joking mewheni, 4atj sisyphus luke Seek, jailctf merger) / others: 65(natte), 67(jonas ryno kg583), 67(kabutack), 68(HETHAT), 70(cg)
# ============================ 62 ============================
# p=lambda g:[[(1 in s)+3*(3 in s)or(2 in t)*2for t in zip(*g)]for s in g]
p=lambda g:[[max({*s}-{2})or(2 in t)*2for t in zip(*g)]for s in g]
