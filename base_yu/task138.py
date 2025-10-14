# best: 104(4atj sisyphus luke Seek mukundan, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 116(cubbus), 117(jacekw Potatoman nauti natte), 117(import itertools), 123(MasukenSamba), 133(THUNDER THUNDER)
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
