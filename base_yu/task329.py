# best: 54(ShadowPrompt Labs, kabutack, jonas ryno kg583, JRKKX, jacekwl, blob2822, THUNDER THUNDER, jailctf merger, natte, cubbus, JRKXK, 4atj sisyphus luke Seek mukundan, Yuchen20, jacekw Potatoman nauti natte, JRKX, ox jam, MasukenSamba, jonas ryno kg583 kabutack, intgrah jimboko awu macaque sammyuri, cg-klogw, jacekwl Potatoman nauti, cg-klogw-sekken, adakoda, jacekw Potatoman nauti, import itertools) / others: 55(Ravi Annaswamy), 56(HETHAT), 56(duckyluuk), 58(Tony Li), 64(JRK)
# p=lambda g:[[v*(i==len(s)//2)for i,v in enumerate(s)]for s in g]
# lambda g:[(a:=[0]*(b:=len(s)//2))+[s[b],*a]for s in g]
# ======================== 54 ========================
p=lambda g:[[0]*(b:=len(s)//2)+[s[b]]+b*[0]for s in g]
