# best: 45(ShadowPrompt Labs, jonas ryno kg583, JRKKX, jailctf merger, JRK, natte, JRKXK, 4atj sisyphus luke Seek mukundan, Yuchen20, Potatoman, jacekw Potatoman nauti natte, HETHAT, Code Golf International, JRKX, ox jam, MasukenSamba, kambarakun, jonas ryno kg583 kabutack, intgrah jimboko awu macaque sammyuri, jacekwl Potatoman nauti, jacekw Potatoman nauti, import itertools) / others: 48(adakoda), 51(Tony Li), 52(kabutack), 52(blob2822), 52(THUNDER THUNDER)
# ==================== 45 ===================
# 3456789012345678901234567890123456789012345
# p=lambda g:[[s[j]|s[8-j]for j in range(4)]for s in g]
# p=lambda g:[[*map(max,zip(s[:4],s[::-1]))]for s in g]
# p=lambda g:[[*map(max,zip(s,s[:4:-1]))]for s in g]
p=lambda g:[[*map(max,s,s[:4:-1])]for s in g]
