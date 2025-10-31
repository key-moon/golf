# best: 61(jailctf merger) / others: 62(Code Golf International), 62(4atj sisyphus luke Seek mukundan), 62(ox jam), 63(LogicLynx), 64(intgrah jimboko awu macaque sammyuri)
# ============================ 61 ===========================
# p=lambda g,c=2:c and p(sum([[[*s]]*2for s in zip(*g)if sum(s)],[]),c-1)or g
p=lambda g,c=-1:c*g or p(sum([[[*s]]*2for s in zip(*g)if sum(s)],[]),c+1)
# p=lambda g:len(g[0])%2and p(sum([[[*s]]*2for s in zip(*g)if sum(s)],[]))or g
