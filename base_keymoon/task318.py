# best: 54(jailctf merger, ox jam) / others: 58(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 58(Code Golf International), 58(4atj sisyphus luke Seek mukundan), 58(Yuchen20), 59(HIMAGINE THE FUTURE.)
# ======================== 54 ========================
# lambda g:[[any(a)*3for a in zip(*c)]for c in zip(g,g[5:])]
p=lambda g:eval("[any(a)*3for a in zip(g.pop(0),g[4])],"*4)
