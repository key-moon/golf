# best: 29(duckyluuk, 4atj sisyphus luke Seek mukundan, MasukenSamba, HashPanda, 4atj sisyphus luke Seek, biz, jailctf merger, kg583, intgrah jimboko awu macaque sammyuri, nauti, Yuchen20, HETHAT, jacekwl Potatoman nauti, xsot ovs att joking mewheni, jonas ryno kg583, JRK, mukundan) / others: 30(kabutack), 31(natte), 31(jacekwl Potatoman), 31(dbdr), 31(cg)
# ============ 29 ===========
# 縦横線対称([[7]]) or 対称性0([[1]])
# だめ: g[0][0]==g[2][2] and g[0][2]==g[2][0]
# {*g[::2]} <- set化
# lambda g:[[1,7][g[0]!=g[2]::2]]
# lambda g:[[1+6*(g[0]!=g[2])]]
# lambda g:[[7**(g[0]==g[2])]]
p=lambda g:[[g[0]==g[2]or 7]]
