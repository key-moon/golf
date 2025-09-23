# best: 269(ox jam, jailctf merger) / others: 322(4atj sisyphus luke Seek mukundan), 325(natte), 325(jacekw Potatoman nauti), 325(Rafael Pooja), 325(kdmitrie)
def p(g):
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   u=[g[i+k][j:j+3]for k in range(3)]
   if len({*sum(u,[])})>3:
    d=max(g[0],key=g[0].count)
    c,={*u[1]}-{d}
    for _ in range(4):
     for s in range(1,4):
      for y in range(len(g)-3*s):
       for x in range(len(g[0])-3*s):
        if all(g[y+k][x+l]==[u[k//s][l//s],d][u[k//s][l//s]==c]for k in range(3*s)for l in range(3*s)):
         for k in range(3*s):
          for l in range(3*s):
           g[y+k][x+l]=u[k//s][l//s]
     u[:]=zip(*u[::-1])
    return g
