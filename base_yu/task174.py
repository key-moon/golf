# best: 89(jailctf merger) / others: 97(Code Golf International), 97(4atj sisyphus luke Seek mukundan), 97(ox jam), 105(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 105(import itertools)
# ========================================== 89 =========================================
# p=lambda g:max((m:=[[v for*t,v in zip(*g,s)if c in t]for s in g if c in s],all(s==s[::-1] for s in m))[::-1]for c in sum(g,[]))[1]
# p=lambda g:max((m:=[[v for*t,v in zip(*g,s)if c in t]for s in g if c in s],(w:=[*zip(*m)])==w[::-1])[::-1]for c in sum(g,[]))[1]
# p=lambda g,c=1,o=1:[(u:=[v for*t,v in zip(*g,s)if c in t])*(o:=o*(u==u[::-1]))for s in g if c in s]*o or p(g,c+1)
# p=lambda g,c=1:[*zip(*(a:=[[v for t,v in zip(g,s)if c in t]for s in zip(*g)if c in s])*(a==a[::-1]))]or p(g,c+1)

# p=lambda g,c=1:g*(c>19)or[*zip(*(u:=[s for s in p(g,c+10)if c%10in s]))]*(c>9or u==u[::-1])or p(g,c+1)
# p=lambda g,c=1:c//20*g or[*zip(*(u:=[s for s in p(g,c+10)if c%10in s]))]*(c>9or u==u[::-1])or p(g,c+1)
# p=lambda g,c=1:[*zip(*(u:=[s for s in g*(c>9)or p(g,c+10)if c%10in s]))]*(c>9or u==u[::-1])or p(g,c+1)
p=lambda g,c=1:[*zip(*(u:=[s for s in g*(c>9)or p(g,c+10)if c%10in s]))]*(u==u[::1|-(c<9)])or p(g,c+1)

# def p(g,c=1):
#  if c>19:
#   return g
#  u=[s for s in p(g,c+10)if c%10 in s]
#  return [*zip(*u)]*(c>9 or u==u[::-1]) or p(g,c+1)

# def p(g,c=1):
#  if c<=9:
#   u=[s for s in p(g,c+10) if c%10 in s]
#   return [*zip(*u)]*(u==u[::-1]) or p(g,c+1)
#  else:
#   u=[s for s in g if c%10 in s]
#   return [*zip(*u)]


# def p(g):
#  for c in sum(g,[]):
#   if CASE==4:
#    print(c,[*zip(*[(t:=[v for*t,v in zip(*g,s)if c in t],t==t[::-1])[::-1]for s in g if c in s])])

# def p(g):
#  for c in {*sum(g,[])}:
#   m=[[v for*t,v in zip(*g,s)if c in t]for s in g if c in s]
#   if all(s==s[::-1] for s in m):
#    return m
