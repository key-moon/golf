def p(g):
 R=[r for r in g if any(r)]
 i=next(x for x,v in enumerate(R[0])if v)
 j=len(R[0])-next(x for x,v in enumerate(R[0][::-1])if v)-1
 R=[r[i:j+1]for r in R]
 k=len(R);a,b=R[0][0],R[1][1]
 return[[b if min(x,y,k-1-x,k-1-y)<1 else a for y in range(k)]for x in range(k)]
