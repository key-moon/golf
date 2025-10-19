# best: 65(ShadowPrompt Labs, Tony Li, JRKKX, blob2822, THUNDER THUNDER, jailctf merger, Ty Woods, jacekw Potatoman nauti natte, rucin93, Ali, kambarakun, biz, cg-klogw-sekken, adakoda, import itertools, Ravi Annaswamy, today) / others: 74(4atj sisyphus luke Seek mukundan), 74(Code Golf International), 75(ox jam), 77(intgrah jimboko awu macaque sammyuri), 102(Yuchen20)
# ============================== 65 =============================
# p=lambda g:(u:=[*zip(*g)])and[*map(list,zip(*[u[i%(8-2*(u[3:6]in(u[:3],u[2::-1])))] for i in range(15)]))]
# p=lambda g:(u:=[*zip(*g)])and[*map(list,zip(*(u[:8-2*(u[3:6]in(u[:3],u[2::-1]))]*3)[:15]))]
# p=lambda g:[*map(list,zip(*((u:=[*zip(*g)])[:8-2*(u[3:6]in(u[:3],u[2::-1]))]*3)[:15]))]
# p=lambda g:(u:=[*zip(*g)])and[(s[:8-2*(u[3:6]in(u[:3],u[2::-1]))]*3)[:15]for s in g]
# p=lambda g:[(s[:8-2*((u:=[*zip(*g)])[3:6]in(u[:3],u[2::-1]))]*3)[:15]for s in g]
p=lambda g:[(r[:6+2*(r[:4]in(r[4:8],r[8:12]))]*3)[:15]for r in g]