# best: 59(jacekw Potatoman nauti natte, Code Golf International, 4atj sisyphus luke Seek mukundan, HETHAT, natte, import itertools, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 64(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 64(MasukenSamba), 64(Yuchen20), 67(JRKX), 67(JRKXK)
# =========================== 59 ==========================
# lambda s:sum([[v*0!=0and p(v)or v/5]*3for v in s[1::3]],[])
p=lambda g:g*0!=0and sum(zip(*[[*map(p,g[1::3])]]*3),())or g/5
