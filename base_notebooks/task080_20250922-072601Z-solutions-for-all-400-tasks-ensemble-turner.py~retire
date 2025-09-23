def p(o):
 o=[list(i)for i in o];s=[]
 for i in[o,[*zip(*o)]]:e=len(i);k=[-1]+[k for k in range(e)if len({*i[k]})<2]+[e];s.append([(a+1,m)for a,m in zip(k,k[1:])if m>a+1])
 m,m=s;g=len(m);t=range(g);d=[[o[i[0]][k[0]]for k in m]for i in m];i=sum(d,[]);l=max(i,key=i.count);e=p=0;f=[-1,0,1]
 for i in range(1,g-1):
  for k in range(1,g-1):
   if(s:=d[i][k])!=l:
    if d[i][k-1]==d[i+1][k]==d[i-1][k]!=l:e=[[d[i+n][k+y]for y in f]for n in f];p=s;break
  if e:break
 for i in t:
  for k in t:
   if d[i][k]==p:
    for n in f:
     if 0<=(l:=i+n)<g:
      for y in f:
       if 0<=(s:=k+y)<g:d[l][s]=e[n+1][y+1]
 for k,(y,t)in zip(d,m):
  for s,(i,n)in zip(k,m):
   for k in range(y,t):o[k][i:n]=[s]*(n-i)
 return o