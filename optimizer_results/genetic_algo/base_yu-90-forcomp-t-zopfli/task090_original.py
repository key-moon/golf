A=range
def p(g):
 _,l,r,t=max(((d-u)*(r-l)-9*sum(sum(s[l:r])for s in g[u:d]),l,r,g[u:d])for d in A(len(g)+1)for r in A(len(g[0])+1)for u in A(d-1)for l in A(r))
 for s in t:s[l:r]=[6]*(r-l)
 return g