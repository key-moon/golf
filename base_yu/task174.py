# best: 97(4atj sisyphus luke Seek mukundan, xsot ovs att joking mewheni) / others: 103(jailctf merger), 120(HETHAT), 121(jonas ryno kg583), 129(natte), 129(jacekwl)
# ============================================== 97 =============================================
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











