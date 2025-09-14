# best: 29(duckyluuk, 4atj sisyphus luke Seek mukundan, MasukenSamba, HashPanda, 2F, biz, jailctf merger, intgrah jimboko awu macaque sammyuri, Yuchen20, HETHAT, cg-klogw, jacekwl Potatoman nauti, xsot ovs att joking mewheni, jonas ryno kg583, JRK) / others: 30(kabutack), 31(natte), 31(dbdr), 31(cg), 31(jacekwl)
# ============ 29 ===========
# 縦横線対称([[7]]) or 対称性0([[1]])
# だめ: g[0][0]==g[2][2] and g[0][2]==g[2][0]
# {*g[::2]} <- set化
# lambda g:[[1,7][g[0]!=g[2]::2]]
# lambda g:[[1+6*(g[0]!=g[2])]]
# lambda g:[[7**(g[0]==g[2])]]
p=lambda g:[[g[0]==g[2]or 7]]
