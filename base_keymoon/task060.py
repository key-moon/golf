# best: 47(import itertools, jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 48(cubbus), 48(jacekw Potatoman nauti natte), 48(Code Golf International), 48(4atj sisyphus luke Seek mukundan), 48(natte)
# def p(g):
#  *l,=zip(*g)
#  return[*map(list,zip(*(l[:1]*5+[[(0<c)*5 for c in l[0]]]+l[-1:]*5)))]
# 55
# any(r)
# 1<r[0]
# p=lambda g:[[r,[*r[:1]*5,5,*r[-1:]*5]][any(r)]for r in g]
# p=lambda g:[[r,r[:1]*5+[5]+r[-1:]*5][0<r[0]]for r in g]
# 52
# p=lambda g:[[*r[:1]*5,any(r)*5,*r[-1:]*5]for r in g]
# 50
p=lambda g:[r[:1]*5+[(0<b)*5]+[b]*5for*r,b in g]
