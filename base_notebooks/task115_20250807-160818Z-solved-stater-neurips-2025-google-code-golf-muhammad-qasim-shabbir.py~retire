def p(g):
 def u(a):
  r=[]
  for v in a:
   if v not in r:r.append(v)
  return r
 s=[u(r)for r in g]
 if all(s[0]==r for r in s):return[s[0]]
 return[[v]for v in u([v for r in g for v in r])]
