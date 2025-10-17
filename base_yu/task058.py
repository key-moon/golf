# best: 103(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 110(MasukenSamba), 114(ox jam), 123(jonas ryno kg583 kabutack), 123(JRKX), 123(jonas ryno kg583)
# ================================================ 103 ================================================
# lambda g:g and[[3]*len(g[0]),[(len(g)<3)*3]*(len(g[0])-1)+[3],*zip(*p([*zip(*g[:1:-1])])[::-1])]or g
# lambda g:g and[[3]*(t:=len(g[0])),[(len(g)<3)*3]*~-t+[3],*zip(*p([*zip(*g[:1:-1])])[::-1])]or[]
# lambda g:g and[[3]*(t:=len(g[0])),[(len(g)<3)*3]*~-t+[3],*zip(*p([*zip(*g[:1:-1])])[::-1])]
p=lambda g:g and[[3]*(t:=len(g[0])),[(len(g)<3)*3]*~-t+[3],*zip(*p([*zip(*g[2:])])[::-1])]
