# best: 74(Code Golf International, 4atj sisyphus luke Seek mukundan) / others: 75(ox jam), 76(intgrah jimboko awu macaque sammyuri), 77(jailctf merger), 78(import itertools), 79(jacekw Potatoman nauti natte)
# ================================== 74 ==================================
# p=lambda g,c=2:c and p([*zip(*[{*s[1:len(g)-1]}&{2,8}and s or[s[0],*([3]*(len(g)-2)),s[-1]]for s in g])],c-1)or g
# p=lambda g,c=-1:g*c or p([*zip(*[{*s[1:len(g)-1]}&{2,8}and s or[s[0],*([3]*(len(g)-2)),s[-1]]for s in g])],c+1)
# p=lambda g,c=-1:g*c or p([[s[0]]+[[3,v][bool({*s[1:-1]}-{0,3})] for v in s[1:-1]]+[s[-1]]for s in zip(*g)],c+1)
# p=lambda g,c=-1:g*c or p([{*s[1:-1]}-{0,3}and s or[s[0]]+[3 for v in s[1:-1]]+[s[-1]]for s in zip(*g)],c+1)
# p=lambda g,c=-1:g*c or p([{*s[1:-1]}-{0,3}and s or[s[0]]+[3]*(len(s)-2)+[s[-1]]for s in zip(*g)],c+1)
# p=lambda g,c=-1:g*c or p([{*s[1:-1]}-{0,3}and s or[s[0],*[3]*(len(s)-2),s[-1]]for s in zip(*g)],c+1)
# p=lambda g,c=-1:g*c or p([{*s[1:-1]}-{0,3}and s or[v or 3 for v in s]for s in zip(*g)],c+1)
# p=lambda g,c=-1:g*c or p([[(not {*s[1:-1]}-{0,3}and not v)*3+v for v in s]for s in zip(*g)],c+1)
# p=lambda g,c=-1:g*c or p([[v|3*(not{*s[1:-1],v}-{0,3})for v in s]for s in zip(*g)],c+1)
# p=lambda g:[[v|3*((not min({*s[1:-1],v},{*t[1:-1],v})-{0}))for*t,v in zip(*g,s)]for s in g]
# p=lambda g:[[v+3*({*min(s[1:-1],t[1:-1]),v}=={0})for*t,v in zip(*g,s)]for s in g]
p=lambda g:[[v or 3-3*any(min(s[1:-1],t[1:-1]))for*t,v in zip(*g,s)]for s in g]

# true  2,8 2,8
# true  0,3 3,3
# false 2,8 2,8
# false 0,3 0,3

# def p(g):
#  n=len(g)
#  for _ in[0]*2:*g,=zip(*[{*s[1:n-1]}&{2,8}and s or[s[0],*([3]*(n-2)),s[-1]]for s in g])
#  return g

# def p(g):
#  n=len(g)
#  for _ in[0]*2:
#   g=[{*s[1:n-1]}&{2,8}and s or[s[0],*([3]*(n-2)),s[-1]]for s in g]
#   *g,=map(list,zip(*g))
#  return g
