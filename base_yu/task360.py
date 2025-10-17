# best: 45(jonas ryno kg583 kabutack, jacekwl Potatoman nauti, jacekw Potatoman nauti natte, JRK, JRKX, 4atj sisyphus luke Seek mukundan, jonas ryno kg583, ShadowPrompt Labs, HETHAT, jacekw Potatoman nauti, natte, kambarakun, JRKXK, import itertools, MasukenSamba, Potatoman, jailctf merger, Yuchen20, ox jam, intgrah jimboko awu macaque sammyuri, JRKKX) / others: 48(adakoda), 52(cubbus), 52(blob2822), 52(cg-klogw-sekken), 52(kabutack)
# ==================== 45 ===================
# 3456789012345678901234567890123456789012345
# p=lambda g:[[s[j]|s[8-j]for j in range(4)]for s in g]
# p=lambda g:[[*map(max,zip(s[:4],s[::-1]))]for s in g]
# p=lambda g:[[*map(max,zip(s,s[:4:-1]))]for s in g]
p=lambda g:[[*map(max,s,s[:4:-1])]for s in g]
