# best: 105(xsot ovs att) / others: 109(4atj sisyphus luke Seek), 109(sisyphus), 110(mukundan), 112(Seek64), 112(joking)
# ================================================= 105 =================================================
# p=lambda g:max((m:=[[v for*t,v in zip(*g,s)if c in t]for s in g if c in s],all(s==s[::-1] for s in m))[::-1]for c in sum(g,[]))[1]
p=lambda g:max((m:=[[v for*t,v in zip(*g,s)if c in t]for s in g if c in s],(w:=[*zip(*m)])==w[::-1])[::-1]for c in sum(g,[]))[1]

# def p(g):
#  for c in sum(g,[]):
#   if CASE==4:
#    print(c,[*zip(*[(t:=[v for*t,v in zip(*g,s)if c in t],t==t[::-1])[::-1]for s in g if c in s])])

# def p(g):
#  for c in {*sum(g,[])}:
#   m=[[v for*t,v in zip(*g,s)if c in t]for s in g if c in s]
#   if all(s==s[::-1] for s in m):
#    return m
