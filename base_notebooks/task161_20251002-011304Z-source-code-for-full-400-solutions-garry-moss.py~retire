def p(u,p=enumerate,l=range,i=len):
 n,r=i(u),i(u[0]);s={e:{0:[],1:[]}for e in set(sum(u,[]))}
 for(m,y)in p(u):
  for(g,e)in p(y):s[e][0]+=[m];s[e][1]+=[g]
 del s[0];e=sorted([[len(s[e][1])-max(s[e][0])/100,e]for e in s])[0][1];u=[[m if m==e else 0for m in m]for m in u]
 for m in l(n):
  if u[m][0]==e or u[m][-1]==e:
   for g in l(r):u[m][g]=e
 for g in l(r):
  if u[0][g]==e or u[-1][g]==e:
   for m in l(n):u[m][g]=e
 return u