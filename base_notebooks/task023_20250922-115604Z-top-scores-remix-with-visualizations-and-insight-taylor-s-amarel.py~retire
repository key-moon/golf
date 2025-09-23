def p(g):
 from itertools import combinations as C;R=range;h,w=len(g),len(g[0])
 S=lambda r,c,i:[(r,c),(r,c+1),(r+1,c),(r+1,c+1)]if i<1 else([(r,c),(r+1,c),(r+2,c)]if i<2 else[(r,c),(r,c+1),(r,c+2)])
 M=lambda B:[g[x].__setitem__(y,(8,2,2)[i]) for r,c,i in B for x,y in S(r,c,i)]
 A=[(r,c,i)for i in R(3)for r in R(h-(1,2,0)[i])for c in R(w-(1,0,2)[i])if all(g[x][y]==5 for x,y in S(r,c,i))]
 G={(r,c)for r in R(h)for c in R(w)if g[r][c]==5}
 for s in R(1,len(A)+1):
  for B in C(A,s):
   P=sum([S(*b)for b in B],[])
   if len(P)==len(set(P))and set(P)==G:
    return M(B) and 0 or g
 B,U=[],set()
 [B.append(s)or U.update(P)for s in sorted(A,key=lambda x:(x[2],*x[:2]))if not(P:=set(S(*s)))&U]
 return M(B) and 0 or g