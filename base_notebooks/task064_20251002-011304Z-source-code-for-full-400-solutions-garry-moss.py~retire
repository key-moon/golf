a=len
i=range
q=[[0,1],[0,-1],[1,0],[-1,0]]
def p(n):
 k,m=a(n),a(n[0]);d=sum(n,[]);x=sorted([[d.count(t),t]for t in set(d)])
 for t in i(k):
  for s in i(m):
   if n[t][s]==x[1][1]:
    for(d,b)in q:
     if 0<=t+d<k and 0<=s+b<m and n[t+d][s+b]==x[2][1]:
      for f in i(20):
       if 0<=t+d*f<k and 0<=s+b*f<m:
        j=n[t+d*f][s+b*f]
        if j==x[0][1]:n[t][s]=0
 for t in range(4):
  n=list(map(list,zip(*n[::-1])));k,m=a(n),a(n[0])
  for t in i(k):
   if n[t].count(0)>0:
    j=0
    for s in i(m):
     if n[t][s]==x[0][1]and n[t].count(0)>0and n[t].index(0)>s:j=1
     if j:
      if n[t][s]==x[2][1]:n[t][s]=x[0][1]
      elif n[t][s]==0:j=0
 n=[[x[1][1]if t==0else t for t in t]for t in n];return n