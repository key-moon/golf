# best: 71(natte, 4atj sisyphus luke Seek mukundan, jailctf merger) / others: 72(ox jam), 75(jacekw Potatoman nauti), 75(2F), 75(biz), 75(intgrah jimboko awu macaque sammyuri)
# ================================= 71 ================================
# p=lambda g:(u:=[*filter(int,map(max,zip(*g)))]+[0]*9)and[u[:3],u[5:2:-1],u[6:9]]
p=lambda g:[(u:=[*filter(int,map(max,*g))]+[0]*9)[:3],u[5:2:-1],u[6:9]]
