B=len
A=range
def p(g):
 for i in A(B(g)-2):
  for j in A(B(g[0])-2):
   u=[g[i+k][j:j+3]for k in A(3)]
   if B({*sum(u,[])})>3:
    d=max(g[0],key=g[0].count);c,={*u[1]}-{d}
    for _ in A(4):
     for s in A(1,4):
      for y in A(B(g)-3*s):
       for x in A(B(g[0])-3*s):
        if all(g[y+k][x+l]==[u[k//s][l//s],d][u[k//s][l//s]==c]for k in A(3*s)for l in A(3*s)):
         for k in A(3*s):
          for l in A(3*s):g[y+k][x+l]=u[k//s][l//s]
     u[:]=zip(*u[::-1])
    return g