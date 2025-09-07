# best: 71(mukundan, 4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, jailctf merger, natte) / others: 72(xsot ovs att joking mewheni), 75(biz), 75(jacekwl Potatoman), 75(nauti), 75(intgrah jimboko awu macaque sammyuri)
# ================================= 71 ================================
# p=lambda g:(u:=[*filter(int,map(max,zip(*g)))]+[0]*9)and[u[:3],u[5:2:-1],u[6:9]]
p=lambda g:[(u:=[*filter(int,map(max,*g))]+[0]*9)[:3],u[5:2:-1],u[6:9]]
