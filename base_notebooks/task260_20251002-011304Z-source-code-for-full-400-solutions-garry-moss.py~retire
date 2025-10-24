m=len
c=range
g=[[0,0],[0,1],[1,0],[1,1]]
def p(j):
 u,u=m(j),m(j[0]);i=[n for n in set(sum(j,[]))if n not in[0,5]][0]
 for o in c(u-1):
  for l in c(u-1):
   r=[j[o+n][l+q]for(n,q)in g]
   if r.count(5)==1and sum(r)==5:
    for q in c(2):
     for s in c(2):
      if j[q+o][s+l]==5:
       for n in c(-10,10):
        if r[2]==5:
         if 0<=q+o-n-1<u and 0<=s+l-n+1<u:j[q+o-n-1][s+l-n+1]=i
        elif 0<=q+o-n+1<u and 0<=s+l-n-1<u:j[q+o-n+1][s+l-n-1]=i
 j=[[n if n!=5else 0for n in n]for n in j];return j