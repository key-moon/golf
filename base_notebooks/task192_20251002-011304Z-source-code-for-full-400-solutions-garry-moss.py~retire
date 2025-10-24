def p(g,m=len,s=range):
 d,e=m(g),m(g[0]);i=sum(g,[]);p=sorted([[i.count(n),n]for n in set(i)])[0][1];u=[[0,1],[0,-1],[-1,0],[1,0]]
 for n in s(d):
  for o in s(e):
   if g[n][o]==p:
    t=[]
    for(i,c)in u:
     if n+i>=0and o+c>=0and n+i<d and o+c<e:t+=[g[n+i][o+c]]
    if sum(t)/m(t)<max(t)/2:g[n][o]=0
    else:g[n][o]=max(t)
    try:
     if g[n][o+1]+g[n][o-1]==0 or g[n+1][o]+g[n-1][o]==0:g[n][o]=0
    except:pass
  if g[-1][-1]>0:
   if g[-2][-1]==0:g[-1][-1]=0
   if g[-1][-2]==0:g[-1][-1]=0
  if g[-1][10]>0and g[-2][10]==0:g[-1][10]=0
 return g