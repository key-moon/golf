# best: 54(jailctf merger, ox jam) / others: 60(ShadowPrompt Labs), 60(JRKKX), 60(JRKXK), 60(4atj sisyphus luke Seek mukundan), 60(Yuchen20)
# lambda g:eval("[1.5*(x^y)for x,y in zip(g.pop(0),g[6])],"*6)
# ======================== 54 ========================
# lambda g:eval("[3/2*(x^y)for x,y in zip(g.pop(0),g[6])],"*6)
p=lambda g:[[3/2*(s.pop(0)^y)for y in g.pop(7)]for s in g[:6]]
