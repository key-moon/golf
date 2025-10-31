# best: 65(Code Golf International) / others: 66(4atj sisyphus luke Seek mukundan), 66(jailctf merger), 69(ox jam), 70(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 70(LogicLynx)
# lambda g,A=[0,0,5,0]:[a:=A[1:],b:=[5,5,5],A[:-1],b,a,A[:-1],a,a,b][max(max(g))-1::3]
# lambda g:[a:=[0,5,0],b:=[5,5,5],c:=[0,0,5],b,a,c,a,a,b][max(max(g))-1::3]
# ============================== 65 =============================
p=lambda g:[c:=[0,0,5],c,b:=[5]*3,a:=[0,5,0],a,b,a][6-max(max(g))*2:][:3]
