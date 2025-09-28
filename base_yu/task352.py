# best: 84(4atj sisyphus luke Seek mukundan, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 90(jacekw Potatoman nauti natte), 92(natte), 101(jacekw Potatoman nauti), 108(JRKX), 108(Yuchen20)
# ======================================= 84 =======================================
# p=lambda g,c=4:c and p([[y or 0<x<3for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c-1)or g
p=lambda g,c=-3:c*g or p([[y or 0<x<3for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
