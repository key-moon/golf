# best: 50(jonas ryno kg583 kabutack, jacekw Potatoman nauti natte, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, JRKX, Code Golf International, 4atj sisyphus luke Seek mukundan, jonas ryno kg583, HETHAT, natte, kabutack, JRKXK, import itertools, MasukenSamba, jailctf merger, HIMAGINE THE FUTURE., adakoda, Yuchen20, ox jam, THUNDER THUNDER, biz, JRKKX) / others: 52(Tony Li), 52(Tony Li & Darren Amadeus Martin), 55(jacekwl Potatoman nauti), 55(blob2822), 55(jacekw Potatoman nauti)
# lambda g:[(r:=[0,*g[0],0])[1:-1],[*map(max,zip(r[2:],r))]]*3
# lambda g:[r:=g[0],[*map(max,zip((a:=[0,*r,0])[2:],a))]]*3
# lambda g:[r:=g[0],[*map(max,zip(r[1:]+[0],[0]+r))]]*3
# ====================== 50 ======================
#p=lambda g:[r:=g[0],[*map(max,zip(r[1:]+[0],[0]+r))]]*3
p=lambda g:[r:=g[0],[*map(max,r[1:]+[0],[0]+r)]]*3
