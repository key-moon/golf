# best: 159(Code Golf International, 4atj sisyphus luke Seek mukundan) / others: 160(ox jam), 170(jailctf merger), 205(MasukenSamba), 207(jacekw Potatoman nauti natte), 207(import itertools)
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
