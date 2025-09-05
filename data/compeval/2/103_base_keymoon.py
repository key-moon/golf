# best: 29(kg583, mukundan, HashPanda, biz, luke, 4atj, duckyluuk, xsot ovs, joking MeWhenI, HETHAT, 4atj sisyphus luke Seek, nauti, MeWhenI, xsot, ovs, att, sisyphus) / others: 30(kabutack), 30(MasukenSamba), 31(cg), 31(dbdr), 31(natte)
# ============ 29 ===========
# 縦横線対称([[7]]) or 対称性0([[1]])
# だめ: g[0][0]==g[2][2] and g[0][2]==g[2][0]
# {*g[::2]} <- set化
# lambda g:[[1,7][g[0]!=g[2]::2]]
# lambda g:[[1+6*(g[0]!=g[2])]]
# lambda g:[[7**(g[0]==g[2])]]
p=lambda g:[[g[0]==g[2]or 7]]
