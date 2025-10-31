# best: 46(LogicLynx, FuunAgent, ox jam) / others: 52(Code Golf International), 52(jailctf merger), 57(4atj sisyphus luke Seek mukundan), 57(ALE-Agent), 58(intgrah jimboko awu macaque sammyuri)
# lambda g:[[g[i//2|1][j//2|1] for j in range(len(g[0])*2)] for i in range(len(g)*2)]
# lambda g:sum([[[int,p][r*0!=0](r)]*4for r in g[1::2]],[])
# ==================== 46 ====================
p=lambda g:g*0!=0and sum([[p(r)]*4for r in g[1::2]],[])or g
