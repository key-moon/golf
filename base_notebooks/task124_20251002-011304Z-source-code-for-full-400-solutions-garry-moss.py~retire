u=range
n=len
def p(s):
 t,d=n(s),n(s[0])
 def f(u,s):
  e=[0]*d
  for(f,t)in enumerate(u):
   T=f+s
   if t and 0<=T<d:e[T]=t
  return e
 for e in u(1,t+1):
  i=s[:e]
  for g in u(-d,d+1):
   r=True
   for T in u(t):
    if f(i[T%e],T//e*g)!=s[T]:r=False;break
   if r:return[f(i[d%e],d//e*g)for d in u(10)]
 return[s[e%t][:]for e in u(10)]