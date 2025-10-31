# best: 194(jailctf merger) / others: 203(Code Golf International), 207(4atj sisyphus luke Seek mukundan), 211(lv1.dev), 235(ox jam), 257(HIMAGINE THE FUTURE.)
# ============================================================================================= 194 ==============================================================================================
# def p(g):
#  *C,b=sorted({*sum(g,[])},key=sum(g,[]).count)
#  for c in C:
#   for y in range(-32,14):
#    for x in range(-32,14):
#     u=[len(g)>(Y:=(i+y)//2)>-1<(X:=(j+x)//2)<len(g[i]) and g[Y][X] for i,s in enumerate(g)for j,v in enumerate(s)if v==c]
#     if len({*u})==1 and u[0] not in (0,c,b):
#      print(CASE,u)
#      return[[v for*t,v in zip(*g,s)if u[0]in t]for s in g if u[0]in s]
#  return g

# def p(g):
# #  B=max({*sum(g,[])},key=sum(g,[]).count)
#  for c in range(10):
#   for d in range(10):
#    u={(i,j)for i in range(len(g))for j in range(len(g[i]))if g[i][j]==c}
#    v={(i,j)for i in range(len(g))for j in range(len(g[i]))if g[i][j]==d}
#    w={(i,j)for i in range(len(g))for j in range(len(g[i]))}
#    if len(u)<30 and len(v)<60 and any(w&{((i-y)*2+a+k,(j-x)*2+b+l) for i,j in u for k in (0,1)for l in (0,1)}==v for y,x in u for a,b in v):
#     return [[[max({*t},key=(s+t).count),v][v==c] for*t,v in zip(*g,s)if c in t]for s in g if c in s]
# #     return [[[B,v][v==c] for*t,v in zip(*g,s)if c in t]for s in g if c in s]
# #     return [[v for*t,v in zip(*g,s)if c in t]for s in g if c in s]

# def p(g):
#  *C,B=sorted({*sum(g,[])},key=sum(g,[]).count)
#  for c in C:
#   for d in C:
#    u={(i,j)for i in range(len(g))for j in range(len(g[i]))if g[i][j]==c}
#    v={(i,j)for i in range(len(g))for j in range(len(g[i]))if g[i][j]==d}
#    w={(i,j)for i in range(len(g))for j in range(len(g[i]))}
#    if any(w&{(i*2-y*2+a+k,j*2-x*2+b+l) for i,j in u for k in (0,1)for l in (0,1)}==v for y,x in u for a,b in v):
#     return [[[B,v][v==c] for*t,v in zip(*g,s)if c in t]for s in g if c in s]


def p(g):
 *C,b=sorted({*sum(g,[])},key=sum(g,[]).count)
 for c in C:
  for y in range(-32,14):
   for x in range(-32,14):
    d=[g[i*2+y+k][j*2+x+l]for i in range(len(g))for j in range(len(g[i]))for k in range(2)for l in range(2)if g[i][j]==c if i*2+y+k in range(len(g))if j*2+x+l in range(len(g[i]))]
    if []<d==[d[0]]*sum(g,[]).count(d[0]):
     g=[[[b,v][v==c]for v in s] for s in zip(*g) if c in s]
     return[[[b,v][v==c]for v in s] for s in zip(*g) if c in s]

# def p(g):
#  b=max(sum(g,[]),key=sum(g,[]).count)
#  a=[v for v in sum(g,[])if f"{b}, {v}, {b}"not in str(g+[*zip(*g)])][0]
#  for i in range(len(g)):
#   for j in range(len(g[i])):
#    c,*u={g[i+y//2-len(g)][j+x//2-len(g[i])] for y in range(0,len(g),2)for x in range(0,len(g[i]),2) if g[y][x]==a}
#    v={g[i+y//2-len(g)][j+x//2-len(g[i])] for y in range(0,len(g),2)for x in range(0,len(g[i]),2) if g[y][x]!=a}
#    if not u and c not in v:
#     g=[[[b,v][v==c]for v in s] for s in zip(*g) if c in s]
#     return[[[b,v][v==c]for v in s] for s in zip(*g) if c in s]

# def p(g):
#     b=max(sum(g,[]),key=sum(g,[]).count)
#     a=[v for v in sum(g,[])if f"{b}, {v}, {b}"not in str(g+[*zip(*g)])][0]
#     o=[[[b,a][v==a]for v in r[::2]]for r in g[::2]]
#     m=[r*2for r in g*2]
#     for i,r in enumerate(m):
#         for j,v in enumerate(r):
#             for k in{*sum(g,[])}:
#                 if[[[b,a][v==k]for v in r[j:j+len(o[0])]]for r in m[i:i+len(o)]]==o:
#                     s=g
#                     s=[[[b,k][v==k]for v in i]for i in zip(*s)if k in i]
#                     s=[[[b,k][v==k]for v in i]for i in zip(*s)if k in i]
#                     return s
# def p(g):
#  *C,b=sorted({*sum(g,[])},key=sum(g,[]).count)
#  for c in C:
#   for y in range(-32,14):
#    for x in range(-32,14):
#     U=[]
#     L=[]
#     d=[]
#     for i in range(len(g)):
#      for j in range(len(g[i])):
#       if g[i][j]==c:
#        U+=[i]
#        L+=[j]
#        for k in range(2):
#         for l in range(2):
#          Y=i*2+y+k
#          X=j*2+x+l
#          if len(g)>Y>-1<X<len(g[i]):
#           d+=[g[Y][X]]
#     L,*_,R=sorted(L)
#     U,*_,D=sorted(U)
#     if any({*d}=={C[k]}and len(d)==sum(g,[]).count(C[k])for k in range(3)):
#      return[[[b,c][v==c]for v in s[L:R+1]]for s in g[U:D+1]]
