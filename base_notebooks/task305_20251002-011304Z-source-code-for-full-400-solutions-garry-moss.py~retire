def p(r):
 n=len(r);t=[n for t in r for n in t if n]
 if not t:return r
 d=sorted(set(t));a=len(d);t=[[0]*n for t in[0]*n]
 for r in range(n):
  for g in range(n):t[r][g]=d[(r+g)%a]
 return t