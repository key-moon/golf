# best: 71(jacekw Potatoman nauti natte, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, Team JYCDT, lv1.dev, LogicLynx, ALE-Agent, santa2024, FuunAgent, natte, import itertools, jailctf merger, HIMAGINE THE FUTURE., adakoda, ox jam) / others: 72(kambarakun), 74(Tony Li & Darren Amadeus Martin), 75(jacekwl Potatoman nauti), 75(jacekwl), 75(jacekw Potatoman nauti)
# ================================= 71 ================================
# p=lambda g:(u:=[*filter(int,map(max,zip(*g)))]+[0]*9)and[u[:3],u[5:2:-1],u[6:9]]
p=lambda g:[(u:=[*filter(int,map(max,*g))]+[0]*9)[:3],u[5:2:-1],u[6:9]]
