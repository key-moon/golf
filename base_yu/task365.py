# best: 112(mukundan, jailctf merger) / others: 134(xsot ovs att joking mewheni), 138(joking), 138(joking MeWhenI), 161(4atj sisyphus luke Seek), 161(Seek64)
# ==================================================== 112 =====================================================
# p=lambda g:max((all(y:=sum(x:=[s[l:r]for s in g[u:d]],[])),y.count(2),len(y),x)for r in range(11)for l in range(r)for d in range(11)for u in range(d))[3]
p=lambda g:max((all(y:=sum(x:=[s[l:t%11]for s in g[u:t//11]],[])),y.count(2),len(y),x)for t in range(121)for l in range(t%11)for u in range(t//11))[3]

# def p(g):
#  for r in range(10):
#   for l in range(r):
#    for d in range(10):
#     for u in range(d):
#      y=sum(x:=[s[l:r] for s in g[u:d]],[])
#      -all(y),y.count(2),len(y),x
#  return g
