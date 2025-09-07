# best: 50(mukundan, 4atj sisyphus luke Seek mukundan, xsot ovs att joking mewheni, jonas ryno kg583, HETHAT, 4atj sisyphus luke Seek, kabutack, jailctf merger, MasukenSamba, natte, intgrah jimboko awu macaque sammyuri) / others: 58(kg583), 58(jacekwl Potatoman), 58(duckyluuk), 58(dbdr), 58(JRK)
# lambda g:[(r:=[0,*g[0],0])[1:-1],[*map(max,zip(r[2:],r))]]*3
# lambda g:[r:=g[0],[*map(max,zip((a:=[0,*r,0])[2:],a))]]*3
# lambda g:[r:=g[0],[*map(max,zip(r[1:]+[0],[0]+r))]]*3
# ====================== 50 ======================
p=lambda g:[r:=g[0],[*map(max,zip(r[1:]+[0],[0]+r))]]*3
