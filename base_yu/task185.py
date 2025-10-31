# best: 107(Code Golf International) / others: 110(jailctf merger), 120(import itertools), 121(ox jam), 126(HIMAGINE THE FUTURE.), 143(4atj sisyphus luke Seek mukundan)
# ================================================== 107 ==================================================

# def p(g):
#  c=max(g)[0]
#  k=g[0].index(c)+1
# #  g=[s[k-1::k] for s in g[k-1::k]]
#  for _ in range(100):
# #   g=[*zip(*g[({*g[-1]}!={c})-2::-1])]
#   g=[*zip(*g[-({*g[-k]}=={c})*k-1::-1])]
# #  g=[[sum({g[i][j]}&{g[i+k][j]}&{g[i][j+k]}&{g[i+k][j+k]}-{c}) for j in range(2,14,3)]for i in range(2,14,3)]
# #  g=[[sum({s[j]}&{s[j+1]}&{t[j]}&{t[j+1]}-{c})for j in range(3)]for s,t in zip(g,g[1:])]
# #  g=[[sum({s[j]}&{s[j+k]}&{t[j]}&{t[j+k]}-{c})for j in range(k-1,k*3,k)]for s,t in zip(g[k-1::k],g[k+k-1::k])]
#  g=[[s[j]*(s[j]==s[j+k]==t[j]==t[j+k]!=c)for j in range(k-1,k*3,k)]for s,t in zip(g[k-1::k],g[k+k-1::k])]
#  return g

# def p(g):
#  c=max(g)[0]
#  k=g[0].index(c)+1
#  R=range(k-1,len(g)-k,k)
# #  g=[[sum({g[i][j]}&{g[i+k][j]}&{g[i][j+k]}&{g[i+k][j+k]}-{c})for j in R]for i in R]
#  g=[[g[i][j]*(g[i][j]==g[i+k][j]==g[i][j+k]==g[i+k][j+k]!=c)for j in R]for i in R]
#  for _ in range(100):
#   g=[*zip(*g[any(g[-1])-2::-1])]
#  return g

# def p(g):
#  c=max(g)[0]
#  g=[[v for*t,v in zip(*g,s)if all(t)]for s in g if all(s)]
#  for _ in range(100):
#   g=[*zip(*g[({*g[-1]}!={c})-2::-1])]
#  g=[[sum({s[j]}&{s[j+1]}&{t[j]}&{t[j+1]}-{c})for j in range(3)]for s,t in zip(g,g[1:])]
#  return g

# def p(g):
#  c=max(g)[0]
#  g=[*zip(*[(l:=c)and[(v==l!=c)*(l:=v)for*t,v in zip(*g,s)if {*t}-{0,c}]for s in g])][1:]
#  g=[*zip(*[(l:=c)and[(v==l!=c)*(l:=v)for*t,v in zip(*g,s)if {*t}-{0,c}]for s in g])][1:]
# #  c=max(g)[0]
# #  g=[*zip(*[(l:=c)and[(v==l!=c)*(l:=v)for*t,v in zip(*g,s)if {*t}-{0,c}]for s in g])]
#  return g

# def p(g):
#  g=[(l:=(d:=max(g[0])))and[(v==l!=d*0)*(l:=v)for t,v in zip(g,s)if{*t}-{0,d}][1:]for s in zip(*g)]
#  g=[(l:=(d:=max(g[0])))and[(v==l!=d*1)*(l:=v)for t,v in zip(g,s)if{*t}-{0,d}][1:]for s in zip(*g)]
#  return g

# p=lambda g,d=0,c=-1:c*[s[1:]for s in g[1:]]or p([*zip(*[(l:=(d:=d or max(g)[0]))and[(v==l!=d)*(l:=v)for*t,v in zip(*g,s)if {*t}-{0,d}]for s in g])],d,c+1)
# p=lambda g,c=-1:c*g or p([*zip(*[(l:=(d:=max(g)[0]or-1))and[(v==l!=d)*(l:=v)for*t,v in zip(*g,s)if{*t}-{0,d}]for s in g])][1:],c+1)
# p=lambda g,c=-1:c*g or p([(l:=(d:=max(g[0])or-1))and[(v==l!=d)*(l:=v)for t,v in zip(g,s)if{*t}-{0,d}][1:]for s in zip(*g)],c+1)
# p=lambda g:g*(len(g)<4)or p([(l:=(d:=max(g[0])or-1))and[(v==l!=d)*(l:=v)for t,v in zip(g,s)if{*t}-{0,d}][1:]for s in zip(*g)])
p=lambda g,c=-1:c*g or p([(l:=(d:=max(g[0])+~c))and[(v==l!=d)*(l:=v)for t,v in zip(g,s)if{*t}-{0,d}][1:]for s in zip(*g)],c+1)

# [*zip(*)]
# def p(g):
#  c=max(g)[0]
#  for _ in range(2):
#   g=[*zip(*[(l:=c)and[(v==l!=c)*(l:=v)for*t,v in zip(*g,s)if all(t)+_]for s in g if all(s)+_])]
#  for _ in range(40):
#   g=[*zip(*g[any(g[-1])-2::-1])]
#  return g

# def p(g):
#  n=len(g)
#  G=sum(g,[])
#  *C,b,c=sorted({*G},key=G.count)
#  s=G.index(b^c)
# #  u=[[g[i][j]!=b^c and g[i][j]for j in range(s,n,s+1)]for i in range(s,n,s+1)]
#  u=[[v!=b^c and v for v in t[s:n:s+1]]for t in g[s:n:s+1]]
# #  y=min(i for i in range(len(u))for j in range(len(u[0]))if u[i][j]in C)
# #  x=min(j for i in range(len(u))for j in range(len(u[0]))if u[i][j]in C)
# #  y=min(i for i,s in enumerate(u)for j,v in enumerate(s)if v in C)
# #  x=min(j for i,s in enumerate(u)for j,v in enumerate(s)if v in C)
#  y=min(i for i,s in enumerate(u)for v in s if v in C)
#  x=min(j for s in u for j,v in enumerate(s)if v in C)
# #  return[[[0,u[i][j]][u[i][j]==u[i+1][j]==u[i][j+1]==u[i+1][j+1]]for j in range(x,x+3)]for i in range(y,y+3)]
#  return[[[0,A[j]][A[j]==B[j]==A[j+1]==B[j+1]]for j in range(x,x+3)]for A,B in zip(u[y:y+3],u[y+1:y+4])]
# #  return[[[0,u[i][j]][len({u[i+k%2][j+k//2]for k in range(4)})==1] for j in range(x,x+3)]for i in range(y,y+3)]
# #  return[[[0,u[y+i][x+j]][u[y+i][x+j]==u[y+i+1][x+j]==u[y+i][x+j+1]==u[y+i+1][x+j+1]] for j in range(3)]for i in range(3)]
# #  return [[u[y+i][x+j] for j in range(4)]for i in range(4)]

# def p(g):
# #  n=len(g)
#  *C,b,c=sorted({*sum(g,[])},key=sum(g,[]).count)
#  s=sum(g,[]).index(b^c)
#  u=[[g[i][j]!=b^c and g[i][j] for j in range(s,len(g),s+1)]for i in range(s,len(g),s+1)]
# #  u=[[v!=b^c and v for v in t[s:len(g):s+1]]for t in g[s:len(g):s+1]]
#  y=min(i for i in range(len(u))for j in range(len(u[0]))if u[i][j]in C)
#  x=min(j for i in range(len(u))for j in range(len(u[0]))if u[i][j]in C)
# #  y=min(i for i,s in enumerate(u)for j,v in enumerate(s)if v in C)
# #  x=min(j for i,s in enumerate(u)for j,v in enumerate(s)if v in C)
# #  y=min(i for i,s in enumerate(u)for v in s if v in C)
# #  x=min(j for s in u for j,v in enumerate(s)if v in C)
#  return[[[0,u[i][j]][u[i][j]==u[i+1][j]==u[i][j+1]==u[i+1][j+1]]for j in range(x,x+3)]for i in range(y,y+3)]
# #  return[[[0,A[j]][A[j]==B[j]==A[j+1]==B[j+1]]for j in range(x,x+3)]for A,B in zip(u[y:y+3],u[y+1:y+4])]

# #  return[[[0,u[i][j]][len({u[i+k%2][j+k//2]for k in range(4)})==1] for j in range(x,x+3)]for i in range(y,y+3)]
# #  return[[[0,u[y+i][x+j]][u[y+i][x+j]==u[y+i+1][x+j]==u[y+i][x+j+1]==u[y+i+1][x+j+1]] for j in range(3)]for i in range(3)]
# #  return [[u[y+i][x+j] for j in range(4)]for i in range(4)]
