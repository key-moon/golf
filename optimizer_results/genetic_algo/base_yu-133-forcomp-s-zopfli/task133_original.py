def p(g):
 for c in range(10):
  for d in range(10):
   u=[(i,j)for i in range(len(g))for j in range(len(g[0]))if c==g[i][j]];v=[(i,j)for i in range(len(g))for j in range(len(g[0]))if d==g[i][j]];a=[(i,j)for i in range(len(g))for j in range(len(g[0]))if c!=g[i][j]>0if any((i+k,j+l)in u for k in range(-1,2)for l in range(-1,2))];b=[(i,j)for i in range(len(g))for j in range(len(g[0]))if d!=g[i][j]>0if any((i+k,j+l)in v for k in range(-1,2)for l in range(-1,2))];b=[(i,j)for i in range(len(g))for j in range(len(g[0]))if d!=g[i][j]>0if any((i+k,j+l)in b+v for k in range(-1,2)for l in range(-1,2))];b=[(i,j)for i in range(len(g))for j in range(len(g[0]))if d!=g[i][j]>0if any((i+k,j+l)in b+v for k in range(-1,2)for l in range(-1,2))];b=[(i,j)for i in range(len(g))for j in range(len(g[0]))if d!=g[i][j]>0if any((i+k,j+l)in b+v for k in range(-1,2)for l in range(-1,2))];s=(len(b)^6)%6
   for(i,j)in u*(len(a)==1<len(u)and len(v)==len(b)):
    for k in range(s):
     for l in range(s):g[(i-a[0][0])*s+b[0][0]+k][(j-a[0][1])*s+b[0][1]+l]=d
 return g