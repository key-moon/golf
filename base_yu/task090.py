# best: 159(4atj sisyphus luke Seek mukundan) / others: 160(xsot ovs att joking mewheni), 170(jailctf merger), 215(jacekwl Potatoman nauti), 236(MasukenSamba), 237(J&R)
# ============================================================================ 159 ============================================================================
def p(g):
#  _,l,r,t=max(((d-u)*(r-l)-9*sum(sum([*zip(*g[u:d])][l:r],())),l,r,g[u:d])for d in range(len(g)+1)for r in range(len(g[0])+1)for u in range(d-1)for l in range(r))
 _,l,r,t=max(((d-u)*(r-l)-9*sum(sum(s[l:r])for s in g[u:d]),l,r,g[u:d])for d in range(len(g)+1)for r in range(len(g[0])+1)for u in range(d-1)for l in range(r))
 for s in t:
  s[l:r]=[6]*(r-l)
 return g

# def p(g):
#  _,_,l,r,t=max((-sum(sum([*zip(*g[u:d])][l:r],())),(d-u)*(r-l),l,r,g[u:d])for d in range(len(g)+1)for r in range(len(g[0])+1)for u in range(d-1)for l in range(r))
#  for s in t:
#   s[l:r]=[6]*(r-l)
#  return g
