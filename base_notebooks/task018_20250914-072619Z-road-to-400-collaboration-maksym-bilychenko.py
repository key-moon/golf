def T(V,R):U=list(zip(*V));x=int((min(U[1])+max(U[1]))/2);y=int((min(U[2])+max(U[2]))/2);V=list(zip(*[((u,-c+y+x,r-x+y),(u,c-y+x,-r+x+y))if R else((u,2*x-r,c),(u,r,2*y-c))for u,r,c in V]));return V
def p(d):
 R=range;L=len;V=[];U=[];H=L(d);W=L(d[0]);E=[];K=list.extend
 for i in R(H):
  for j in R(W):
   if (c:=d[i][j])and(c,i,j)not in V+U:
    O=[(c,i,j)];C=set()
    while O:
     v=O.pop(0)
     if v not in C:C.add(v);K(O,[(c,x,y)for a,b in[(0,-1),(0,1),(1,0),(-1,0)]if 0<=(x:=v[1]+a)<H if 0<=(y:=v[2]+b)<W if(c:=d[x][y])])
    F=list(C)
    if len(C)>3:E.append(F);V;K(V,F)
    else:K(U,F)
 for O in E:
  for i in R(-H,H):
   for j in R(-W,W):
    Q=[(v[0],v[1]+i,v[2]+j)for v in O];B=T(Q,1);Z=T(Q,0);X=T(B[0],0)+T(B[1],0);Y=T(Z[0],1)+T(Z[1],1);A=[Q]+B+Z+X+Y;S=[I for I in A if len([v for v in I if v not in V and v in U])==3]
    if S:
     for i,(u,r,c) in enumerate(S[0]):d[r][c]=u;d[O[i][1]][O[i][2]]=0
 return d