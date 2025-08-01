def p(g):
 for r in g:
  n = len(r)
  for i in range(n-1, -1, -1):
   if r[i]:
    break
  s = r[:i+1]
  for k in range(1, len(s)+1):
   if all(s[j] == s[j % k] for j in range(len(s))):
    break
  r[:] = [s[j % k] for j in range(n)]
 return g