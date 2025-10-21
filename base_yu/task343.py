# best: 65(jacekw Potatoman nauti natte, Ali, blob2822, Krige, ShadowPrompt Labs, rucin93, today, cg-klogw-sekken, Ravi Annaswamy, kambarakun, import itertools, Ty Woods, Tony Li, jailctf merger, Tony Li & Darren Amadeus Martin, adakoda, THUNDER THUNDER, biz, JRKKX) / others: 74(Code Golf International), 74(4atj sisyphus luke Seek mukundan), 75(ox jam), 77(intgrah jimboko awu macaque sammyuri), 102(Yuchen20)
# ============================== 65 =============================
# p=lambda g:(u:=[*zip(*g)])and[*map(list,zip(*[u[i%(8-2*(u[3:6]in(u[:3],u[2::-1])))] for i in range(15)]))]
# p=lambda g:(u:=[*zip(*g)])and[*map(list,zip(*(u[:8-2*(u[3:6]in(u[:3],u[2::-1]))]*3)[:15]))]
# p=lambda g:[*map(list,zip(*((u:=[*zip(*g)])[:8-2*(u[3:6]in(u[:3],u[2::-1]))]*3)[:15]))]
# p=lambda g:(u:=[*zip(*g)])and[(s[:8-2*(u[3:6]in(u[:3],u[2::-1]))]*3)[:15]for s in g]
# p=lambda g:[(s[:8-2*((u:=[*zip(*g)])[3:6]in(u[:3],u[2::-1]))]*3)[:15]for s in g]
p=lambda g:[(r[:6+2*(r[:4]in(r[4:8],r[8:12]))]*3)[:15]for r in g]