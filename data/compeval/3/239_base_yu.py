# best: 106(jailctf merger) / others: 108(luke), 108(4atj sisyphus luke Seek), 108(joking MeWhenI), 108(xsot ovs att), 111(ovs)
# ================================================= 106 ==================================================

def p(g):
 u=sum(g,[])
 C=sorted([(-u.count(v),v)for v in{*u}])
 return[*zip(*[[c]*-v+[0]*(v-min(C)[0])for v,c in C])]
