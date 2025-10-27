# best: 71(jacekw Potatoman nauti natte, Code Golf International, 4atj sisyphus luke Seek mukundan, ShadowPrompt Labs, natte, import itertools, jailctf merger, HIMAGINE THE FUTURE., adakoda) / others: 72(kambarakun), 72(ox jam), 74(Tony Li & Darren Amadeus Martin), 75(jacekwl Potatoman nauti), 75(jacekwl)
# ================================= 71 ================================
# p=lambda g:(u:=[*filter(int,map(max,zip(*g)))]+[0]*9)and[u[:3],u[5:2:-1],u[6:9]]
p=lambda g:[(u:=[*filter(int,map(max,*g))]+[0]*9)[:3],u[5:2:-1],u[6:9]]
