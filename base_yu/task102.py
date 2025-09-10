# best: 150(jailctf merger) / others: 168(2F), 168(biz), 170(xsot ovs att joking mewheni), 173(4atj sisyphus luke Seek mukundan), 178(natte)
# ======================================================================= 150 ========================================================================

p=lambda g,R=range:[exec("for s in g[u:u+m]:s[l:l+m]=[2]*m")for m in R(1,8)for u in R(12-m)for l in R(12-m)if[k:=(5,)*(m+2),*[(5,*[0]*m,5)]*m,k]==[*zip(*g[u-1:u+m+1])][l-1:l+m+1]]*0+g

# port re;p=lambda g,n=5:g*-n or eval(re.sub(f"(?<={(A:='5..'*n)}){f'[^52]{{{n*3-3}}}'.join(['(5.{%s}5, )'%(3*(12-n)+1)]*n)}(?={A})",(" 2,"*~-n).join(rf"\{i+1}"for i in range(n)),str(p(p(g,n-1),n-1))))
# port re;p=lambda g,n=5:g*-n or eval(re.sub(f"(?<={(A:='5..'*n)}){('[^52]'*~-n*3).join(['(5.{%s}5, )'%(37-3*n)]*n)}(?={A})",(" 2,"*~-n).join(rf"\{i+1}"for i in range(n)),str(p(p(g,n-1),n-1))))


# R=range
# def p(g):
#  for m in R(1,8):
#   for u in R(12-m):
#    for l in R(12-m):
#     # x=[*zip(*g[u:d])]
#     # if sum(sum(s[l:r])for s in g[u:d])==(m-1)*4*5 and all(g[d-1][l:r]+g[u][l:r]+[*x[l],*x[r-1]]):
#     # if all(g[d-1][l:r]+g[u][l:r]+[*x[l],*x[r-1]]) and 1-any(any(s[l+1:r-1])for s in g[u+1:d-1]):
#     # if all(g[u+i][l+j]==5*((i%~-m)*(j%~-m)<1)for i in range(m)for j in range(m)):
#     #  for s in g[u+1:u+m-1]:
#     #   s[l+1:l+m-1]=[2]*(m-2)
#     if[k:=(5,)*(m+2),*[(5,*[0]*m,5)]*m,k]==[*zip(*g[u-1:u+m+1])][l-1:l+m+1]:
#     # if all(g[u-1+i][l-1+j]==5*((i%-~m)*(j%-~m)<1)for i in R(m+2)for j in R(m+2)):
#      for s in g[u:u+m]:
#       s[l:l+m]=[2]*m
#  return g
