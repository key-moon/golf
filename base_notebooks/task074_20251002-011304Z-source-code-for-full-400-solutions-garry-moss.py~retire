def p(e,d=enumerate,f=range):
 n=min(len(e),len(e[0]))if e and e[0]else 0
 def p(e):
  if n<=2:return tuple(tuple(0if n==9else n for n in n)for n in e)
  l=[[0if n==9else n for n in n]for n in e];u=list(map(list,zip(*l)));e=[[max(l[e][n],u[e][n])for n in f(n)]for e in f(n)];l=[l[2:n][::-1]for l in e[1:n]];p=[n[:]for n in e]
  for(i,l)in d(l,1):
   for(t,u)in d(l,2):
    if u:p[i][t]=u
  return tuple(map(tuple,p))
 l=tuple(tuple(n)for n in e)
 for u in f(256):
  e=p(l)
  if e==l:break
  l=e
 return[list(n)for n in l]