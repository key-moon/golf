# best: 64(jailctf merger, 4atj sisyphus luke Seek mukundan, import itertools) / others: 65(ShadowPrompt Labs), 65(Tony Li), 65(JRKKX), 65(jacekwl), 65(blob2822)
# ============================= 64 =============================
# p=lambda g:(u:=[*zip(*g)])and[[0,*g[0],0],*[*zip(*(u[:1]+u+u[-1:]))],[0,*g[-1],0]]
p=lambda g:[[0,*g[0],0],*[s[:1]+s+s[-1:]for s in g],[0,*g[-1],0]]
