# best: 71(ShadowPrompt Labs, jailctf merger, natte, 4atj sisyphus luke Seek mukundan, jacekw Potatoman nauti natte, adakoda, import itertools) / others: 72(ox jam), 72(kambarakun), 75(jacekwl), 75(2F), 75(Yuchen20)
# ================================= 71 ================================
# p=lambda g:(u:=[*filter(int,map(max,zip(*g)))]+[0]*9)and[u[:3],u[5:2:-1],u[6:9]]
p=lambda g:[(u:=[*filter(int,map(max,*g))]+[0]*9)[:3],u[5:2:-1],u[6:9]]
