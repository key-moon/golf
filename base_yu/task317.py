# best: 59(jacekw Potatoman nauti natte, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, HETHAT, natte, import itertools, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 64(MasukenSamba), 64(Yuchen20), 67(JRKX), 67(JRKXK), 67(adakoda)
# =========================== 59 ==========================
# p=lambda g:sum([[sum([[v/5]*3for v in s[1::3]],[])]*3for s in g[1::3]],[])
p=lambda s:sum([[v*0!=0and p(v)or v/5]*3for v in s[1::3]],[])
