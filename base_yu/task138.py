# best: 104(4atj sisyphus luke Seek mukundan, xsot ovs att joking mewheni) / others: 107(jailctf merger), 149(natte), 154(MasukenSamba), 174(jonas ryno kg583), 175(JRK)
# ================================================ 104 =================================================

# p=lambda g,c=-79:c*g or p([*zip(*g[1-all(g[0]):][::-1])],c+1)
# p=lambda g,c=-79:c*g or p([[(s[0]in s[i:]and c>-4)*s[0]|v for i,v in enumerate(s)]for s in zip(*g[1-all(g[0]):][::-1])],c+1)
# p=lambda g,c=79:-c*g or p([[(s[0]in s[i:]and c<4)*s[0]|v for i,v in enumerate(s)]for s in zip(*g[1-all(g[0]):][::-1])],c-1)
# p=lambda g,c=79:-c*g or p([[(s[0]in s[i:])*(c<4)*s[0]|v for i,v in enumerate(s)]for s in zip(*g[1-all(g[0]):][::-1])],c-1)
p=lambda g,c=79:-c*g or p([[(s[0]in s[i:])*(c<4)*s[0]|v for i,v in enumerate(s)]for s in zip(*g[all(g[-1])-2::-1])],c-1)

# def p(g):
#  for _ in range(4):
#   while 1-all(g[0]):
#    g=g[1:]
#   *g,=map(list,zip(*g[::-1]))
#  return[[(s[0]in s[i:])*s[0]|v for i,v in enumerate(s)] for s in g]
#  for _ in range(4):
#   for s in g:
#    for j in range(len(s)):
#     if s[j]==s[0]:
#      s[:j]=[s[0]]*j
#   *g,=map(list,zip(*g[::-1]))
#  return g









