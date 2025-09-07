# best: 59(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, jailctf merger, intgrah jimboko awu macaque sammyuri, HETHAT, xsot ovs att joking mewheni, mukundan) / others: 67(natte), 67(biz), 67(Bulmenisaurus), 68(kabutack), 69(jacekwl Potatoman)
# =========================== 59 ==========================
# p=lambda g:sum([[sum([[v/5]*3for v in s[1::3]],[])]*3for s in g[1::3]],[])
p=lambda s:sum([[v*0!=0and p(v)or v/5]*3for v in s[1::3]],[])
