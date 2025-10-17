# best: 54(jailctf merger, ox jam) / others: 58(4atj sisyphus luke Seek mukundan), 58(Yuchen20), 58(intgrah jimboko awu macaque sammyuri), 60(ShadowPrompt Labs), 60(2F)
# ======================== 54 ========================
# lambda g:[[any(a)*3for a in zip(*c)]for c in zip(g,g[5:])]
p=lambda g:eval("[any(a)*3for a in zip(g.pop(0),g[4])],"*4)
