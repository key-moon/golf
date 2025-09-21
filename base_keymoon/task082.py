# best: 50(natte, ox jam, 4atj sisyphus luke Seek mukundan, JRKX, MasukenSamba, kabutack, jailctf merger, intgrah jimboko awu macaque sammyuri, jonas ryno kg583 kabutack, Yuchen20, HETHAT, xsot ovs att joking mewheni, jonas ryno kg583) / others: 55(jacekw Potatoman nauti), 55(jacekwl Potatoman nauti), 58(duckyluuk), 58(J&R), 58(dbdr)
# lambda g:[(r:=[0,*g[0],0])[1:-1],[*map(max,zip(r[2:],r))]]*3
# lambda g:[r:=g[0],[*map(max,zip((a:=[0,*r,0])[2:],a))]]*3
# lambda g:[r:=g[0],[*map(max,zip(r[1:]+[0],[0]+r))]]*3
# ====================== 50 ======================
#p=lambda g:[r:=g[0],[*map(max,zip(r[1:]+[0],[0]+r))]]*3
p=lambda g:[r:=g[0],[*map(max,r[1:]+[0],[0]+r)]]*3
