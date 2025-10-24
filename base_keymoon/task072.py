# best: 54(jailctf merger, ox jam) / others: 60(jonas ryno kg583 kabutack), 60(jacekw Potatoman nauti natte), 60(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 60(JRKX), 60(Code Golf International)
# lambda g:eval("[1.5*(x^y)for x,y in zip(g.pop(0),g[6])],"*6)
# ======================== 54 ========================
# lambda g:eval("[3/2*(x^y)for x,y in zip(g.pop(0),g[6])],"*6)
p=lambda g:[[3/2*(s.pop(0)^y)for y in g.pop(7)]for s in g[:6]]
