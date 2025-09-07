# best: 84(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 85(4atj sisyphus luke Seek), 86(xsot ovs att joking mewheni), 92(natte), 105(mukundan), 112(kabutack)
# ======================================= 84 =======================================
# p=lambda g,c=4:c and p([[y or 0<x<3for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c-1)or g
p=lambda g,c=-3:c*g or p([[y or 0<x<3for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
