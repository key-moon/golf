# best: 54(jonas ryno kg583 kabutack, cubbus, jacekwl Potatoman nauti, jacekw Potatoman nauti natte, blob2822, JRKX, 4atj sisyphus luke Seek mukundan, jacekwl, jonas ryno kg583, jacekw Potatoman nauti, cg-klogw-sekken, natte, kabutack, MasukenSamba, cg-klogw, jailctf merger, Yuchen20, ox jam, intgrah jimboko awu macaque sammyuri) / others: 56(HETHAT), 56(duckyluuk), 64(JRK), 64(dbdr), 64(Potatoman)
# p=lambda g:[[v*(i==len(s)//2)for i,v in enumerate(s)]for s in g]
# lambda g:[(a:=[0]*(b:=len(s)//2))+[s[b],*a]for s in g]
# ======================== 54 ========================
p=lambda g:[[0]*(b:=len(s)//2)+[s[b]]+b*[0]for s in g]
