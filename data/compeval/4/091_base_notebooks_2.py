def p(g):
 l=len
 q=range
 c=[]
 for j in q(l(g[0])):
  if any(g[i][j]==5for i in q(l(g))):
   c.append(j)
 o=[]
 for i in q(l(g)):
  if g[i][c[0]]==5:
   o.append(i)
 s,t=min(o)-1,max(o)+1
 d,e=c[0],c[1]
 return[[g[i][j]for j in q(d,e+1)]for i in q(s,t+1)]