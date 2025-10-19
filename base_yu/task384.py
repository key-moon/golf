# best: 62(jailctf merger, 4atj sisyphus luke Seek mukundan, Code Golf International, ox jam) / others: 64(intgrah jimboko awu macaque sammyuri), 66(2F), 66(biz), 68(jacekw Potatoman nauti natte), 68(import itertools)
# ============================ 62 ============================
# p=lambda g,c=2:c and p(sum([[[*s]]*2for s in zip(*g)if sum(s)],[]),c-1)or g
p=lambda g,c=-1:c*g or p(sum([[[*s]]*2for s in zip(*g)if sum(s)],[]),c+1)
# p=lambda g:len(g[0])%2and p(sum([[[*s]]*2for s in zip(*g)if sum(s)],[]))or g
