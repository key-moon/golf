# best: 194(jailctf merger) / others: 214(4atj sisyphus luke Seek mukundan), 233(ox jam), 237(intgrah jimboko awu macaque sammyuri), 252(jacekw Potatoman nauti natte), 252(import itertools)
def p(g):
 for i in range(len(g)):
  for l in range(len(g)):
   r=l
   while g[i][r:]>[8]:r+=1
   for t in g[i:]:
    for j in range(l,r):t[j]|=1
   for k in range(i-(r-l>>1),i+(r-l>>1)+1):
    for j in range(l-(r-l>>1),r+(r-l>>1)):
     if k in range(len(g))and j in range(len(g))and g[k][j]<9:g[k][j]=3
 return g


# R=range
# def p(g):
#  for i in R(n:=len(g)):
#   s=g[i]
#   for l in R(n):
#    r=l
#    if s[l]>8:
#     while r<n and s[r]>8:r+=1
#     for t in g[i:]:
#      for j in R(l,r):
#       if t[j]<1:t[j]=1
#     for k in R(i-(u:=r-l>>1),i+u+1):
#      for j in R(l-u,r+u):
#       if-1<k<n and-1<j<n and g[k][j]<9:g[k][j]=3
#  return g


# R=range
# def p(g):
#  n=len(g)
#  for i,s in enumerate(g):
#   for l in R(n):
#    if s[l]>8:
#     r=l
#     while r<n and s[r]==9:
#      r+=1
#     for k in R(i,n):
#      for j in R(l,r):
#       if g[k][j]==0:
#        g[k][j]=1
#     u=(r-l)//2
#     for k in R(i-u,i+u+1):
#      for j in R(l-u,r+u):
#       if k in R(n)and j in R(n)and g[k][j]<9:
#        g[k][j]=3
#  return g
