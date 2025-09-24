# best: 29(jonas ryno kg583 kabutack, cubbus, jacekwl Potatoman nauti, JRK, blob2822, JRKX, 4atj sisyphus luke Seek mukundan, jonas ryno kg583, HETHAT, jacekw Potatoman nauti, HashPanda Pooja, natte, HashPanda, Rafael Pooja, MasukenSamba, cg-klogw, jailctf merger, Yuchen20, ox jam, 2F, biz, duckyluuk, intgrah jimboko awu macaque sammyuri) / others: 30(kabutack), 31(jacekwl), 31(dbdr), 31(cg), 38(open source)
# ============ 29 ===========
# 縦横線対称([[7]]) or 対称性0([[1]])
# だめ: g[0][0]==g[2][2] and g[0][2]==g[2][0]
# {*g[::2]} <- set化
# lambda g:[[1,7][g[0]!=g[2]::2]]
# lambda g:[[1+6*(g[0]!=g[2])]]
# lambda g:[[7**(g[0]==g[2])]]
p=lambda g:[[g[0]==g[2]or 7]]
