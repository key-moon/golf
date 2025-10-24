def p(u):
 p=range;r=(len(u)-1)//2
 if r==1:
  e=[u[0][0],u[0][2],u[2][0],u[2][2]]
  for i in e:
   if e.count(i)==1:return[[i]]
 for(t,e)in[(0,0),(0,r+1),(r+1,0),(r+1,r+1)]:
  t=[[u[t+i][e+r]for r in p(r)]for i in p(r)];i=[t[i][e]for i in p(r)for e in p(r)]
  if len(set(i))>1:return t