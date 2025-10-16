# best: 56(jailctf merger, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, intgrah jimboko awu macaque sammyuri, import itertools) / others: 57(ox jam), 58(cubbus), 59(Yuchen20), 60(adakoda), 61(ShadowPrompt Labs)
# ========================= 56 =========================
# p=lambda g:[[v+2*(v>0)*(i%3<1)for i,v in enumerate(s)]for s in g]
p=lambda g:[[v*i/2for v,i in zip(s,b""*9)]for s in g]
