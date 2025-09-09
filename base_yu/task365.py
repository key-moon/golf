# best: 111(4atj sisyphus luke Seek mukundan) / others: 112(jailctf merger), 128(xsot ovs att joking mewheni), 178(MasukenSamba), 204(natte), 207(intgrah jimboko awu macaque sammyuri)
# ==================================================== 111 ====================================================
# p=lambda g:max((all(y:=sum(x:=[s[l:r]for s in g[u:d]],[])),y.count(2),len(y),x)for r in range(11)for l in range(r)for d in range(11)for u in range(d))[3]
# lambda g:max((all(y:=sum(x:=[s[l:t%11]for s in g[u:t//11]],[])),y.count(2),len(y),x)for t in range(121)for l in range(t%11)for u in range(t//11))[3]
p=lambda g,A=range:max((all(y:=sum(x:=[s[l:r]for s in g[u:d]],[])),y.count(2),len(y),x)for r in A(11)for l in A(r)for d in A(11)for u in A(d))[3]
# def p(g):
#  for r in range(10):
#   for l in range(r):
#    for d in range(10):
#     for u in range(d):
#      y=sum(x:=[s[l:r] for s in g[u:d]],[])
#      -all(y),y.count(2),len(y),x
#  return g

