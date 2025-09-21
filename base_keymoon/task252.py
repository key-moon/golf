# best: 57(ox jam, 4atj sisyphus luke Seek mukundan, jailctf merger) / others: 59(intgrah jimboko awu macaque sammyuri), 61(xsot ovs att joking mewheni), 62(JRKX), 62(jacekw Potatoman nauti), 62(jonas ryno kg583 kabutack)
# lambda g,R=[0]*99:[R:=[[c,4][4!=C!=0]for c,C in zip(r,[0]+R)]for r in g]
# lambda g:[g:=[[c,4][C*0==0and 4!=C>0]for c,C in zip(r,[0]+g)]for r in g]
# ========================== 57 =========================
p=lambda g:[g:=[[c,4][0<c==C]for c,C in zip(r,[0]+g)]for r in g]
