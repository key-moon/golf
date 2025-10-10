# best: 57(4atj sisyphus luke Seek mukundan, jailctf merger, ox jam) / others: 59(jacekw Potatoman nauti natte), 59(import itertools), 59(intgrah jimboko awu macaque sammyuri), 62(jonas ryno kg583 kabutack), 62(jacekwl Potatoman nauti)
# lambda g,R=[0]*99:[R:=[[c,4][4!=C!=0]for c,C in zip(r,[0]+R)]for r in g]
# lambda g:[g:=[[c,4][C*0==0and 4!=C>0]for c,C in zip(r,[0]+g)]for r in g]
# ========================== 57 =========================
p=lambda g:[g:=[[c,4][0<c==C]for c,C in zip(r,[0]+g)]for r in g]
