# best: 66(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 69(ox jam), 76(jacekwl Potatoman nauti), 76(jacekw Potatoman nauti natte), 76(jacekw Potatoman nauti), 76(import itertools)
# lambda g,A=[0,0,5,0]:[a:=A[1:],b:=[5,5,5],A[:-1],b,a,A[:-1],a,a,b][max(max(g))-1::3]
# lambda g:[a:=[0,5,0],b:=[5,5,5],c:=[0,0,5],b,a,c,a,a,b][max(max(g))-1::3]
# ============================== 66 ==============================
p=lambda g:[c:=[0,0,5],c,b:=[5]*3,a:=[0,5,0],a,b,a][6-max(max(g))*2:][:3]
