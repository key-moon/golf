# best: 103(jailctf merger) / others: 126(4atj sisyphus luke Seek), 127(joking MeWhenI), 128(sisyphus), 148(joking), 155(duckyluuk)
# ================================================ 103 ================================================
# lambda g:g and[[3]*len(g[0]),[(len(g)<3)*3]*(len(g[0])-1)+[3],*zip(*p([*zip(*g[:1:-1])])[::-1])]or g
# lambda g:g and[[3]*(t:=len(g[0])),[(len(g)<3)*3]*~-t+[3],*zip(*p([*zip(*g[:1:-1])])[::-1])]or[]
# lambda g:g and[[3]*(t:=len(g[0])),[(len(g)<3)*3]*~-t+[3],*zip(*p([*zip(*g[:1:-1])])[::-1])]
p=lambda g:g and[[3]*(t:=len(g[0])),[(len(g)<3)*3]*~-t+[3],*zip(*p([*zip(*g[2:])])[::-1])]
