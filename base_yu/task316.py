# best: 71(jacekw Potatoman nauti natte, 4atj sisyphus luke Seek mukundan, natte, jailctf merger) / others: 72(ox jam), 75(jacekwl Potatoman nauti), 75(jacekwl), 75(jacekw Potatoman nauti), 75(Yuchen20)
# ================================= 71 ================================
# p=lambda g:(u:=[*filter(int,map(max,zip(*g)))]+[0]*9)and[u[:3],u[5:2:-1],u[6:9]]
p=lambda g:[(u:=[*filter(int,map(max,*g))]+[0]*9)[:3],u[5:2:-1],u[6:9]]
