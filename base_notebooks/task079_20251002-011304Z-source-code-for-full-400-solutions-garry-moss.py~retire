def p(s):
 p=[];r=len(s)-2
 for o in range(r):
  for q in range(r):
   a=tuple(tuple(s[o+p][q:q+3])for p in(0,1,2))
   for q in{*sum(a,())}-{0}:
    i=tuple(tuple(p*(p==q)for p in p)for p in a)
    if min(map(sum,i))and min(map(sum,zip(*i))):p+=i,
 return[list(p)for p in max(p,key=p.count)]