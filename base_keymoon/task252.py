# best: 53(ox jam) / others: 55(Code Golf International), 57(4atj sisyphus luke Seek mukundan), 57(jailctf merger), 59(jacekw Potatoman nauti natte), 59(lv1.dev)
# lambda g,R=[0]*99:[R:=[[c,4][4!=C!=0]for c,C in zip(r,[0]+R)]for r in g]
# lambda g:[g:=[[c,4][C*0==0and 4!=C>0]for c,C in zip(r,[0]+g)]for r in g]
# ======================== 53 =======================
p=lambda g:[g:=[[c,4][0<c==C]for c,C in zip(r,[0]+g)]for r in g]
