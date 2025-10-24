def p(n,q=enumerate,t=range(11)):
 c=0;r=[[0if(r+1)%4>0and(n+1)%4>0else 5for r in t]for n in t];t={n+r:0for n in'012'for r in'012'}
 for e,n in q(n):
  for f,n in q(n):
   if n>0and n!=5:c=int(n);t[str(e//4)+str(f//4)]+=1
 u=max(t.values())
 for e,n in q(r):
  for f,n in q(n):
   if n==0and t[str(e//4)+str(f//4)]==u:r[e][f]=c
 return r