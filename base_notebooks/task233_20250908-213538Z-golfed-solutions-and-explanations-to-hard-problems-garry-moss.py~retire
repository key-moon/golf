# def p(g):
#  R=range;N=R(9);b=tuple;S={};E=lambda M:[*map(list,zip(*filter(any,M)))];W=lambda f:[f(r,c,[g[r+i//3][c+i%3]for i in N])for r in R(len(g)-2)for c in R(len(g[0])-2)]
#  def A(r,c,B):
#   if len(C:={*B})==2and C&{0,2}=={2}:
#    K=b(x==2for x in B);D={K:sum(C)-2}
#    for i in R(4):S[K]=D;K=b(K[j%3*3+2-j//3]for j in N)
#    for k in N:g[r+k//3][c+k%3]=0
#  W(A);g=E(E(g));[W(lambda r,c,B:(D:=S.get(P:=b(x<1for x in B)))and(k or P in D)and(V:=D.popitem()[1],[g[r+j//3].__setitem__(c+j%3,(V,2)[P[j]])for j in N]))for k in R(2)];return g

def p(u):
 i=range(9);c={};f=lambda a:[a(p,s,[u[p+a//3][s+a%3]for a in i])for p in range(len(u)-2)for s in range(len(u[0])-2)]
 def p(p,s,n):
  if len(r:={*n})==2and r&{0,2}=={2}:
   n=tuple(a==2for a in n);k={n:sum(r)-2}
   for a in range(4):c[n]=k;n=tuple(n[a%3*3+2-a//3]for a in i)
   for a in i:u[p+a//3][s+a%3]=0
 f(p);u=[*map(list,zip(*filter(any,[*map(list,zip(*filter(any,u)))])))];[f(lambda p,s,n:(t:=c.get(n:=tuple(a==0for a in n)))and(a or n in t)and(r:=t.popitem()[1],[u[p+a//3].__setitem__(s+a%3,(r,2)[n[a]])for a in i]))for a in range(2)];return u