# best: 99(xsot ovs att joking mewheni) / others: 105(natte), 105(4atj sisyphus luke Seek mukundan), 105(jailctf merger), 106(intgrah jimboko awu macaque sammyuri), 112(jacekwl Potatoman nauti)
# =============================================== 99 ==============================================

def p(g):
 u=sum(g,[])
 C=sorted([(-u.count(v),v)for v in{*u}])
 return[*zip(*[[c]*-v+[0]*(v-min(C)[0])for v,c in C])]




