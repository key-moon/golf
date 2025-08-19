A=range(10)
def p(g):
 for _ in[0]*4:
  for i in A:
   if{*g[i]}=={0,2}and{*g[i+1]}>{0}:g=[[v or 3for v in(j<=i)*(i*2+1-j<10)and g[i*2+1-j]or g[j]]for j in A]
  *g,=map(list,zip(*g[::-1]))
 return g