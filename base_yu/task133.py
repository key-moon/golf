# best: 298(jailctf merger, ox jam) / others: 321(open source), 321(blob2822), 321(garrymoss), 321(Rafael Pooja), 321(sekken)
def p(g):
 for c in range(10):
  for d in range(10):
   u=[(i,j)for i in range(len(g))for j in range(len(g[0]))if c==g[i][j]]
   v=[(i,j)for i in range(len(g))for j in range(len(g[0]))if d==g[i][j]]
   a=[(i,j)for i in range(len(g))for j in range(len(g[0]))if c!=g[i][j]>0 if any((i+k,j+l)in u for k in range(-1,2)for l in range(-1,2))]
   b=[(i,j)for i in range(len(g))for j in range(len(g[0]))if d!=g[i][j]>0 if any((i+k,j+l)in v for k in range(-1,2)for l in range(-1,2))]
   b=[(i,j)for i in range(len(g))for j in range(len(g[0]))if d!=g[i][j]>0 if any((i+k,j+l)in b+v for k in range(-1,2)for l in range(-1,2))]
   b=[(i,j)for i in range(len(g))for j in range(len(g[0]))if d!=g[i][j]>0 if any((i+k,j+l)in b+v for k in range(-1,2)for l in range(-1,2))]
   b=[(i,j)for i in range(len(g))for j in range(len(g[0]))if d!=g[i][j]>0 if any((i+k,j+l)in b+v for k in range(-1,2)for l in range(-1,2))]
   s=(len(b)^6)%6
   for i,j in u*(len(a)==1<len(u) and len(v)==len(b)):
    for k in range(s):
     for l in range(s):
      g[(i-a[0][0])*s+b[0][0]+k][(j-a[0][1])*s+b[0][1]+l]=d
 return g

# def p(g):
#  for c in range(1,10):
#   for d in range(1,10):
#    u=[(i,j)for i in range(len(g))for j in range(len(g[0]))if g[i][j] if any(len(g)>i+k>-1<j+l<len(g[0]) and g[i+k][j+l]==c for k in range(-1,2)for l in range(-1,2))]
#    v=[(i,j)for i in range(len(g))for j in range(len(g[0]))if g[i][j] if any(len(g)>i+k>-1<j+l<len(g[0]) and g[i+k][j+l]==d for k in range(-1,2)for l in range(-1,2))]
#    v=[(i,j)for i in range(len(g))for j in range(len(g[0]))if g[i][j] if any(len(g)>i+k>-1<j+l<len(g[0]) and g[i+k][j+l]==d or (i+k,j+l) in v for k in range(-1,2)for l in range(-1,2))]
#    v=[(i,j)for i in range(len(g))for j in range(len(g[0]))if g[i][j] if any(len(g)>i+k>-1<j+l<len(g[0]) and g[i+k][j+l]==d or (i+k,j+l) in v for k in range(-1,2)for l in range(-1,2))]
#    v=[(i,j)for i in range(len(g))for j in range(len(g[0]))if g[i][j] if any(len(g)>i+k>-1<j+l<len(g[0]) and g[i+k][j+l]==d or (i+k,j+l) in v for k in range(-1,2)for l in range(-1,2))]
#    a=[(i,j) for i,j in u if g[i][j]!=c]
#    b=[(i,j) for i,j in v if g[i][j]!=d]
#    if len(a)==1 and len(u)>2 and d!=g[a[0][0]][a[0][1]]:
#     s=(len(b)^6)%6
#     for i,j in u:
#      if g[i][j]==c:
#       for k in range(s):
#        for l in range(s):
#         g[(i-a[0][0])*s+b[0][0]+k][(j-a[0][1])*s+b[0][1]+l]=d
#  return g
