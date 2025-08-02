def p(g,case):
 if case!=0:
  return g
 if r:=len(g)<len(g[0]):*g,=map(list,zip(*g))
 h,w=len(g)//2,len(g[0])
 s=g[h:]
 a={i:[]for i in range(10)}
 for i in range(h):
  for j in range(w):
   a[s[i][j]].append((i,j))
 for i in range(h):
  for j in range(w):
   for c in range(10):
    if g[i][j] in (1,c):
     for y in range(h):
      for x in range(w):
       if len(a[c])>9 or len(a[c]) == 0:
        continue
       if all(u-y+i in range(h) and v-x+j in range(w) and g[u-y+i][v-x+j]==c for u,v in a[c]):
        print(c, y,x, i,j)
        for u in range(h):
         for v in range(w):
          if j+v==w or g[i+u][j+v] not in(1,c):
           break
          if y+u in range(h) and x+v in range(w):
           s[y+u][x+v]=g[i+u][j+v]
         if i+u==h or j+v==w or g[i+u][j+v] not in(1,c):
          break
        a[c].append((999, 999))
 
 if r:*g,=map(list,zip(*g))
 return s