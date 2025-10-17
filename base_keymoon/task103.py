# best: 29(jonas ryno kg583, JRKKX, blob2822, jailctf merger, JRK, natte, 2F, cubbus, JRKXK, 4atj sisyphus luke Seek mukundan, Yuchen20, jacekw Potatoman nauti natte, HETHAT, duckyluuk, JRKX, ox jam, MasukenSamba, kambarakun, jonas ryno kg583 kabutack, HashPanda, intgrah jimboko awu macaque sammyuri, cg-klogw, Rafael Pooja, HashPanda Pooja, jacekwl Potatoman nauti, biz, cg-klogw-sekken, adakoda, jacekw Potatoman nauti, import itertools) / others: 30(ShadowPrompt Labs), 30(kabutack), 31(Tony Li), 31(jacekwl), 31(THUNDER THUNDER)
# ============ 29 ===========
# 縦横線対称([[7]]) or 対称性0([[1]])
# だめ: g[0][0]==g[2][2] and g[0][2]==g[2][0]
# {*g[::2]} <- set化
# lambda g:[[1,7][g[0]!=g[2]::2]]
# lambda g:[[1+6*(g[0]!=g[2])]]
# lambda g:[[7**(g[0]==g[2])]]
p=lambda g:[[g[0]==g[2]or 7]]
