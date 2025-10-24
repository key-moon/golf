def p(e,u=enumerate):
 j=[]
 for(f,n)in u(e):
  for(p,n)in u(n):
   if n not in[0,8]:j+=[[f,p,n]];e[f][p]=0
 t=j[0][:];j=[[j[0]-t[0],j[1]-t[1],j[2]]for j in j]
 for(f,n)in u(e):
  for(p,n)in u(n):
   if n==8:
    e[f][p]=t[2]
    for t in j:e[f+t[0]][p+t[1]]=t[2]
 return e