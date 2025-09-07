# best: 73(jailctf merger) / others: 76(4atj sisyphus luke Seek mukundan), 77(mukundan), 79(xsot ovs att joking mewheni), 80(4atj sisyphus luke Seek), 90(natte)
# p=lambda g,c=-3:c*g or p([[y or x>0for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
# ================================== 73 =================================
p=lambda g,c=-3:c*g or[[(c>0)|(c:=y)for y in s]for s in zip(*p(g,c+1)[::-1])]

