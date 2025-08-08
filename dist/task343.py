B=len
A=range
def p(g):
 for r in g:
  n=B(r)
  for i in A(n-1,-1,-1):
   if r[i]:break
  s=r[:i+1]
  for k in A(1,B(s)+1):
   if all(s[j]==s[j%k]for j in A(B(s))):break
  r[:]=[s[j%k]for j in A(n)]
 return g