def p(g):
 h,w=len(g),len(g[0]);a=[]
 for r in g:
  j=0
  while j<w:
   v=r[j]
   if v:
    k=j+1
    while k<w and r[k]==v:k+=1
    a+=[(k-j,v)];j=k
   else:j+=1
 a.sort(reverse=1)
 o=[[0]*w for _ in g]
 for i,(l,v)in enumerate(a):
  for j in range(w-l,w):o[h-1-i][j]=v
 return o