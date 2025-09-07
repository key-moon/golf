# best: 62(4atj sisyphus luke Seek mukundan, xsot ovs att joking mewheni, jailctf merger) / others: 64(4atj sisyphus luke Seek), 64(intgrah jimboko awu macaque sammyuri), 66(mukundan), 66(biz), 70(natte)
# ============================ 62 ============================
# p=lambda g,c=2:c and p(sum([[[*s]]*2for s in zip(*g)if sum(s)],[]),c-1)or g
p=lambda g,c=-1:c*g or p(sum([[[*s]]*2for s in zip(*g)if sum(s)],[]),c+1)
# p=lambda g:len(g[0])%2and p(sum([[[*s]]*2for s in zip(*g)if sum(s)],[]))or g
