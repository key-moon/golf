# best: 59(jacekw Potatoman nauti natte, 4atj sisyphus luke Seek mukundan, HETHAT, natte, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 64(MasukenSamba), 64(Yuchen20), 67(JRKX), 67(JRKXK), 67(Bulmenisaurus)
# =========================== 59 ==========================
# lambda s:sum([[v*0!=0and p(v)or v/5]*3for v in s[1::3]],[])
p=lambda g:g*0!=0and sum(zip(*[[*map(p,g[1::3])]]*3),())or g/5
