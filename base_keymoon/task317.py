# best: 59(mukundan, 4atj sisyphus luke Seek mukundan, xsot ovs att joking mewheni, HETHAT, 4atj sisyphus luke Seek, jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 67(Bulmenisaurus), 67(biz), 67(natte), 68(kabutack), 69(jacekwl Potatoman)
# =========================== 59 ==========================
# lambda s:sum([[v*0!=0and p(v)or v/5]*3for v in s[1::3]],[])
p=lambda g:g*0!=0and sum(zip(*[[*map(p,g[1::3])]]*3),())or g/5
