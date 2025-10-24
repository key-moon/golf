def p(n,f=range):
 l=len(n);u=len(n[0]);e=len({*sum(n,[])}-{0})
 n=[[n[t//e][a//e]for a in f(u*e)]for t in f(l*e)];l*=e;u*=e
 for g in f(min(l,u),0,-1):
  for t in f(l-g+1):
   for a in f(u-g+1):
    i=n[t][a]
    if i and all(e[a:a+g]==[i]*g for e in n[t:t+g]):
     for k,g in(-1,-1),(-1,g),(g,-1),(g,g):
      e=t+k;f=a+g
      while-1<e<l and-1<f<u and not n[e][f]:n[e][f]=2;e+=k>0 or-1;f+=g>0 or-1
     return n