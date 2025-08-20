# best: 54(luke, att) / others: 56(Seek64), 58(mukundan), 62(sisyphus), 63(kg583), 63(duckyluuk)
# ======================== 54 ========================
# p=lambda g:(n:=len(s:=g[0]))and[s[:1]*i+s[:n-i]for i in range(n//2)]
# p=lambda g:(s:=g[0])and g+[s[:1]*i+s[:-i]for i in range(1,len(s)//2)]
# p=lambda g:g+[g[0][:1]*i+g[0][:-i]for i in range(1,len(g[0])//2)]
# p=lambda g:[s:=g[0]]+[(s:=s[:1]+s[:-1])for i in range(1,len(s)//2)]
# p=lambda g:[s:=g[0]]+[*eval("(s:=s[:1]+s[:-1]),"*(len(s)//2-1))]
p=lambda g:[s:=g[0]]+[(s:=s[:1]+s[:-1])for _ in s[1:len(s)//2]]

# def p(g):
#  for i in range(len(g[0])//2-1):g+=[g[0][:1]+g[-1][:-1]]
#  return g

# def p(g):
#  n=len(g[0])
#  for i in range(n):
#   g+=[(g[0][:1]+g[i])[:n]]
#  return g[:n//2]