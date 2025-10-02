# best: 194(jailctf merger) / others: 207(4atj sisyphus luke Seek mukundan), 240(ox jam), 292(intgrah jimboko awu macaque sammyuri), 324(jacekw Potatoman nauti natte), 327(MasukenSamba)
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
#  *C,B=sorted({*sum(g,[])},key=sum(g,[]).count)
#  for c in C:
#   for d in C:
#    u=[(i,j)for i in range(len(g))for j in range(len(g[i]))if g[i][j]==c]
#    v=[(i,j)for i in range(len(g))for j in range(len(g[i]))if g[i][j]==d]
#    for y,x in u:
#     for a,b in v:
#      w=[((i-y)*2+a+k,(j-x)*2+b+l) for i,j in u for k in (0,1)for l in (0,1) if len(g)>(i-y)*2+a+k>-1<(j-x)*2+b+l<len(g[0])]
#      if v==sorted(w):
#       return [[[B,v][v==c] for*t,v in zip(*g,s)if c in t]for s in g if c in s]

def p(g):
 *C,b=sorted({*sum(g,[])},key=sum(g,[]).count)
 for c in C:
  for y in range(-32,14):
   for x in range(-32,14):
    d=[g[i*2+y+k][j*2+x+l]for i in range(len(g))for j in range(len(g[i]))for k in range(2)for l in range(2)if g[i][j]==c if len(g)>i*2+y+k>-1<j*2+x+l<len(g[i])]
    if []<d==[d[0]]*sum(g,[]).count(d[0]):
     return [[[b,v][v==c] for*t,v in zip(*g,s)if c in t]for s in g if c in s]


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
