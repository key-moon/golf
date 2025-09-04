# best: 150(jailctf merger) / others: 168(biz), 170(xsot ovs att joking mewheni), 173(4atj sisyphus luke Seek), 178(natte), 187(mukundan)
# ======================================================================= 150 ========================================================================
R=range
def p(g):
 for m in R(1,8):
  for u in R(12-m):
   for l in R(12-m):
    # x=[*zip(*g[u:d])]
    # if sum(sum(s[l:r])for s in g[u:d])==(m-1)*4*5 and all(g[d-1][l:r]+g[u][l:r]+[*x[l],*x[r-1]]):
    # if all(g[d-1][l:r]+g[u][l:r]+[*x[l],*x[r-1]]) and 1-any(any(s[l+1:r-1])for s in g[u+1:d-1]):
    # if all(g[u+i][l+j]==5*((i%~-m)*(j%~-m)<1)for i in range(m)for j in range(m)):
    #  for s in g[u+1:u+m-1]:
    #   s[l+1:l+m-1]=[2]*(m-2)
    if[k:=(5,)*(m+2),*[(5,*[0]*m,5)]*m,k]==[*zip(*g[u-1:u+m+1])][l-1:l+m+1]:
    # if all(g[u-1+i][l-1+j]==5*((i%-~m)*(j%-~m)<1)for i in R(m+2)for j in R(m+2)):
     for s in g[u:u+m]:
      s[l:l+m]=[2]*m
 return g
