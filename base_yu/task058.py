# best: 103(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger) / others: 110(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 110(ShadowPrompt Labs), 110(MasukenSamba), 114(ox jam), 123(jonas ryno kg583 kabutack)
# ================================================ 103 ================================================
# lambda g:g and[[3]*len(g[0]),[(len(g)<3)*3]*(len(g[0])-1)+[3],*zip(*p([*zip(*g[:1:-1])])[::-1])]or g
# lambda g:g and[[3]*(t:=len(g[0])),[(len(g)<3)*3]*~-t+[3],*zip(*p([*zip(*g[:1:-1])])[::-1])]or[]
# lambda g:g and[[3]*(t:=len(g[0])),[(len(g)<3)*3]*~-t+[3],*zip(*p([*zip(*g[:1:-1])])[::-1])]
p=lambda g:g and[[3]*(t:=len(g[0])),[(len(g)<3)*3]*~-t+[3],*zip(*p([*zip(*g[2:])])[::-1])]
