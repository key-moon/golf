# best: 59(jailctf merger, natte, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, HETHAT, ox jam, intgrah jimboko awu macaque sammyuri, import itertools) / others: 64(Yuchen20), 64(MasukenSamba), 67(JRKKX), 67(THUNDER THUNDER), 67(Bulmenisaurus)
# =========================== 59 ==========================
# lambda s:sum([[v*0!=0and p(v)or v/5]*3for v in s[1::3]],[])
p=lambda g:g*0!=0and sum(zip(*[[*map(p,g[1::3])]]*3),())or g/5
