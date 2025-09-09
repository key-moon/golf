# best: 54(4atj sisyphus luke Seek mukundan, jailctf merger, xsot ovs att joking mewheni) / others: 60(HETHAT), 62(intgrah jimboko awu macaque sammyuri), 63(duckyluuk), 63(jonas ryno kg583), 63(JRK)
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

