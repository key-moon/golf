# best: 62(4atj sisyphus luke Seek mukundan, 2F, biz, jailctf merger, xsot ovs att joking mewheni) / others: 65(natte), 67(kabutack), 67(jonas ryno kg583), 68(intgrah jimboko awu macaque sammyuri), 68(HETHAT)
# ============================ 62 ============================
# p=lambda g:[[(1 in s)+3*(3 in s)or(2 in t)*2for t in zip(*g)]for s in g]
p=lambda g:[[max({*s}-{2})or(2 in t)*2for t in zip(*g)]for s in g]
