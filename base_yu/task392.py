# best: 149(2F, biz) / others: 155(jailctf merger), 156(4atj sisyphus luke Seek mukundan), 157(intgrah jimboko awu macaque sammyuri), 161(MasukenSamba), 161(kabutack)
# ======================================================================= 149 =======================================================================
# def p(g):
#  d=lambda i,j,k:max(abs(j*2+1-i//21),abs(k*2+1-i%21))
#  b,v=0,9
#  for i in range(441):
#   m={(d(i,j//10,j%10),g[j%10][j//10])for j in range(100)}
#   if len(m)==len(m:=dict(m)) and v>(k:=sum(map(bool,m.values()))):
#    v,b,u=k,i,m
#  x,y,*_=sorted(k for k,v in u.items()if v)
#  return[[u[d(b,j,i)%(y-x)]or 5for j in range(10)]for i in range(10)]

# def p(g):
#  d=lambda i,j:max(abs(j//10*2+1-i//21),abs(j%10*2+1-i%21))
#  b,v=0,9
#  for i in range(441):
#   m={(d(i,j),g[j%10][j//10])for j in range(100)}
#   if v>(k:=sum(v>0for _,v in m))and len(m)==len(m:=dict(m)):
#    v,b,u=k,i,m
#  x,y,*_=sorted(k for k,v in u.items()if v)
# #  return[[u[d(b,j*10+i)%(y-x)]or 5for j in range(10)]for i in range(10)]
#  for i in range(100):
#   g[i%10][i//10]=u[d(b,i)%(y-x)]or 5
#  return g


# p=lambda g:([u
#              for x in range(21)
#              for c in (4,6)
#              for d in range(c)
#              for y in range(d)
#              if (o:=1,u:=[[(v:=(max(abs(i*2+1-y),abs(j*2+1-x))%c==d)*max(max(g)),o:=o*(v>=g[i][j]))[0] or 5 for j in range(10)]for i in range(10)])and o]
#                or [[*zip(*p([*zip(*g[::-1])]))][::-1]])[0]

p=lambda g:min((o:=0,[[(v:=(max(abs(i*2+1-I//18%21),abs(j*2+1-I//378%21))%(I%3+4)==I//3%6)*max(max(g)),o:=o+(v<g[i][j])*999+v)[0]or 5for j in range(10)]for i in range(10)],o)[::-1]for I in range(7938))[1]

# p=lambda g:min((o:=0,[[(v:=(max(abs(i*2+1-y),abs(j*2+1-x))%c==d)*max(max(g)),o:=o+(v<g[i][j])*999+v)[0] or 5 for j in range(10)]for i in range(10)],o)[::-1]
#              for x in range(21)
#              for y in range(21)
#              for c in (4,6)
#              for d in range(c))[1]

# p=lambda g:min((o:=0,[[(v:=(max(abs(i*2+1-y),abs(j*2+1-x))%c==d)*max(max(g)),o:=o+(v<g[i][j])*999+v)[0] or 5 for j in range(10)]for i in range(10)],o)[::-1]
#              for x in range(21)
#              for c in (4,6)
#              for d in range(c)
#              for y in range(21))[1]



# p=lambda g:([u
#              for x in range(21)
#              for c in (4,6)
#              for d in range(c)
#              for y in range(d)
#              if (u:=[[(max(abs(i*2+1-y),abs(j*2+1-x))%c==d) * max(max(g)) or 5 for j in range(10)]for i in range(10)])
#              and all((u[i][j]%5>=g[i][j]%5) for j in range(10)for i in range(10))]+[g])[0]

# p=lambda g:max(([-len(u:={max(abs(i*2+1-y),abs(j*2+1-x))%c for i in range(10)for j in range(10)if g[i][j]}),*u],
#             [[(max(abs(i*2+1-y),abs(j*2+1-x))%c in u) * max(max(g)) or 5 for j in range(10)]for i in range(10)])
#              for y in range(21)
#              for x in range(21)
#              for c in (4,6))[1]

# p=lambda g:min((sum((u[i][j]%5<g[i][j]%5)*99+u[i][j]%5 for j in range(10)for i in range(10)),u)
#              for y in range(21)
#              for x in range(21)
#              for c in (4,6)
#              for d in range(c)
#              if (u:=[[(max(abs(i*2+1-y),abs(j*2+1-x))%c==d) * max(max(g)) or 5 for j in range(10)]for i in range(10)]))[1]

# def p(g):
#  u,g=max(([*u],[[(max(abs(i*2+1-y),abs(j*2+1-x))%c in u) * max(max(g)) or 5 for j in range(10)]for i in range(10)])
#              for y in range(21)
#              for x in range(21)
#              for c in (4,6)
#              if len(u:={max(abs(i*2+1-y),abs(j*2+1-x))%c for i in range(10)for j in range(10)if g[i][j]})==1)
#  return g

# def p(g):
#  u,y,x,c=max(([*u],y,x,c)for y in range(21)for x in range(21)for c in (4,6)if len(u:={max(abs(i*2+1-y),abs(j*2+1-x))%c for i in range(10)for j in range(10)if g[i][j]})==1)
#  return [[(max(abs(i*2+1-y),abs(j*2+1-x))%c in u) * max(max(g)) or 5 for j in range(10)]for i in range(10)]


# def p(g):
#  for y in range(21):
#   for x in range(21):
#    for c in range(4,8):
#     u={max(abs(i*2+1-y),abs(j*2+1-x))%c for i in range(10)for j in range(10)if g[i][j]}
#     if len(u)==1:
#      return [[(max(abs(i*2+1-y),abs(j*2+1-x))%c in u) * max(max(g)) or 5 for j in range(10)]for i in range(10)]

# R=range
# def p(g):
#  d=lambda i,j:max(abs(j//10*2+1-i//21),abs(j%10*2+1-i%21))
#  _,b,u=min((sum(v for _,v in m),i,m)for i in R(441)if len(m:={(d(i,j),g[j%10][j//10])for j in R(100)})==len(dict(m)))
#  x,y,*_=sorted(k for k,v in u if v)
# #  for i in R(100):g[i%10][i//10]=dict(u)[d(b,i)%(y-x)]or 5
# #  return g
#  return[[dict(u)[d(b,j*10+i)%(y-x)]or 5 for j in R(10)]for i in R(10)]

# R=range
# def p(g):
#  d=lambda i,j:max(abs(j//10*2+1-i//21),abs(j%10*2+1-i%21))
#  b,v=0,9
#  for i in R(441):
#   m={(d(i,j),g[j%10][j//10])for j in R(100)}
#   if v>(k:=sum(v>0for _,v in m))and len(dict(m))==len(u:=m):v,b=k,i
#  x,y,*_=sorted(k for k,v in u if v)
# #  return[[u[d(b,j*10+i)%(y-x)]or 5for j in range(10)]for i in range(10)]
#  for i in R(100):g[i%10][i//10]=dict(u)[d(b,i)%(y-x)]or 5
#  return g

# def p(g):
#  d=lambda i,j:max(abs(j//10*2+1-i//21),abs(j%10*2+1-i%21))
#  b,v=0,9
#  for i in range(441):
#   m={(d(i,j),g[j%10][j//10])for j in range(100)}
#   if len(m)==len(m:=dict(m))and v>(k:=sum(map(bool,m.values()))):
#    v,b,u=k,i,m
#  x,y,*_=sorted(k for k,v in u.items()if v)
# #  return[[u[d(b,j*10+i)%(y-x)]or 5for j in range(10)]for i in range(10)]
#  for i in range(100):
#   g[i%10][i//10]=u[d(b,i)%(y-x)]or 5
#  return g









