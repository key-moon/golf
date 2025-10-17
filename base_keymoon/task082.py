# best: 50(kabutack, jonas ryno kg583, JRKKX, THUNDER THUNDER, jailctf merger, natte, JRKXK, 4atj sisyphus luke Seek mukundan, Yuchen20, jacekw Potatoman nauti natte, HETHAT, JRKX, ox jam, MasukenSamba, jonas ryno kg583 kabutack, intgrah jimboko awu macaque sammyuri, adakoda, import itertools) / others: 52(Tony Li), 55(blob2822), 55(kambarakun), 55(jacekwl Potatoman nauti), 55(jacekw Potatoman nauti)
# lambda g:[(r:=[0,*g[0],0])[1:-1],[*map(max,zip(r[2:],r))]]*3
# lambda g:[r:=g[0],[*map(max,zip((a:=[0,*r,0])[2:],a))]]*3
# lambda g:[r:=g[0],[*map(max,zip(r[1:]+[0],[0]+r))]]*3
# ====================== 50 ======================
#p=lambda g:[r:=g[0],[*map(max,zip(r[1:]+[0],[0]+r))]]*3
p=lambda g:[r:=g[0],[*map(max,r[1:]+[0],[0]+r)]]*3
