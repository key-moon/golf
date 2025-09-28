# best: 50(jonas ryno kg583 kabutack, jacekw Potatoman nauti natte, JRKX, 4atj sisyphus luke Seek mukundan, jonas ryno kg583, HETHAT, natte, kabutack, MasukenSamba, jailctf merger, Yuchen20, ox jam, intgrah jimboko awu macaque sammyuri) / others: 55(jacekwl Potatoman nauti), 55(jacekw Potatoman nauti), 58(JRK), 58(dbdr), 58(duckyluuk)
# lambda g:[(r:=[0,*g[0],0])[1:-1],[*map(max,zip(r[2:],r))]]*3
# lambda g:[r:=g[0],[*map(max,zip((a:=[0,*r,0])[2:],a))]]*3
# lambda g:[r:=g[0],[*map(max,zip(r[1:]+[0],[0]+r))]]*3
# ====================== 50 ======================
#p=lambda g:[r:=g[0],[*map(max,zip(r[1:]+[0],[0]+r))]]*3
p=lambda g:[r:=g[0],[*map(max,r[1:]+[0],[0]+r)]]*3
