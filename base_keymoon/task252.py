# best: 57(luke) / others: 62(kg583), 62(mukundan), 62(Seek64), 62(nauti), 63(dbdr)
# lambda g,R=[0]*99:[R:=[[c,4][4!=C!=0]for c,C in zip(r,[0]+R)]for r in g]
# lambda g:[g:=[[c,4][C*0==0and 4!=C>0]for c,C in zip(r,[0]+g)]for r in g]
# ========================== 57 =========================
p=lambda g:[g:=[[c,4][0<c==C]for c,C in zip(r,[0]+g)]for r in g]
