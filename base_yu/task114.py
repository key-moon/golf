# best: 64(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 65(jacekwl Potatoman nauti), 65(jacekw Potatoman nauti natte), 65(blob2822), 65(jacekwl), 65(ShadowPrompt Labs)
# ============================= 64 =============================
# p=lambda g:(u:=[*zip(*g)])and[[0,*g[0],0],*[*zip(*(u[:1]+u+u[-1:]))],[0,*g[-1],0]]
p=lambda g:[[0,*g[0],0],*[s[:1]+s+s[-1:]for s in g],[0,*g[-1],0]]
