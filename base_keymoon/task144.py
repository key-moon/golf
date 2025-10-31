# best: 53(Code Golf International, lv1.dev, jailctf merger, ox jam) / others: 57(intgrah jimboko awu macaque sammyuri), 59(jacekw Potatoman nauti natte), 59(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 59(4atj sisyphus luke Seek mukundan), 59(LogicLynx)
# lambda g:[eval("(a.pop(0)+b.pop(0)<1)*3,"*4)for a,b in zip(g,g[5:])]
# lambda g:eval("[3-any(a)*3for a in zip(g.pop(0),g[4])],"*4)
# ======================== 53 =======================
p=lambda g:[[3>>a+s.pop(0)for a in g.pop(5)]for s in g[:4]]

# 3>>a+b
# mapping = { (0, 0): 3, (7, 0): 0, (0, 2): 0, (7, 2): 0 }
