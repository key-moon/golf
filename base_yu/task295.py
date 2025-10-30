# best: 54(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger, ox jam, biz) / others: 59(import itertools), 60(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 60(HETHAT), 60(HIMAGINE THE FUTURE.), 63(jonas ryno kg583 kabutack)
# ======================== 54 ========================
# lambda g:[(s:=g[0])[:]]+[s[:]for s[s.index(0)]in(len(s)//2-1)*s[:1]]
# lambda g:(s:=g[0])and g+[s[:1]*i+s[:-i]for i in range(1,len(s)//2)]
# lambda g:(s:=g[0]+[0])and[s[1:]for s[s.index(0)]in len(s)//2*s[:1]]
# lambda g:(n:=len(s:=g[0]))and[s[:1]*i+s[:n-i]for i in range(n//2)]
# lambda g:[s:=g[0]]+[(s:=s[:1]+s[:-1])for i in range(1,len(s)//2)]
# lambda g:g+[g[0][:1]*i+g[0][:-i]for i in range(1,len(g[0])//2)]
# lambda g:[s:=g[0]]+[*eval("(s:=s[:1]+s[:-1]),"*(len(s)//2-1))]
# lambda g:[s:=g[0]]+[(s:=s[:1]+s[:-1])for _ in s[1:len(s)//2]]
p=lambda g:[s:=g[0]]+[(s:=s[:1]+s[:-1])for _ in s[1:len(s)//2]]

# def p(g):
#  for i in range(len(g[0])//2-1):g+=[g[0][:1]+g[-1][:-1]]
#  return g

# def p(g):
#  n=len(g[0])
#  for i in range(n):
#   g+=[(g[0][:1]+g[i])[:n]]
#  return g[:n//2]
