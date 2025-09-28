# best: 59(jacekw Potatoman nauti natte, 4atj sisyphus luke Seek mukundan, HETHAT, natte, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 64(MasukenSamba), 64(Yuchen20), 67(JRKX), 67(Bulmenisaurus), 67(2F)
# =========================== 59 ==========================
# p=lambda g:sum([[sum([[v/5]*3for v in s[1::3]],[])]*3for s in g[1::3]],[])
p=lambda s:sum([[v*0!=0and p(v)or v/5]*3for v in s[1::3]],[])
