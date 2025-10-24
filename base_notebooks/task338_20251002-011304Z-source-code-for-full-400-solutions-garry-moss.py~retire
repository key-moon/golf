def p(r):
 f=range;n=len(r);i=[[0]*n for p in f(n)]
 def p(t,s):
  if 0<=t<n and 0<=s<n and not i[t][s]and r[t][s]==0:i[t][s]=1;[p(t+n,s+f)for(n,f)in[(1,0),(-1,0),(0,1),(0,-1)]]
 [p(f,0)or p(f,n-1)or p(0,f)or p(n-1,f)for f in f(n)];r=[[3if r[p][n]==0and not i[p][n]else r[p][n]for n in f(n)]for p in f(n)];return[[3if n==3else 0for n in n]for n in r]