# best: 93(jailctf merger) / others: 96(4atj sisyphus luke Seek mukundan), 96(Code Golf International), 98(ox jam), 114(jacekw Potatoman nauti natte), 114(intgrah jimboko awu macaque sammyuri)
# ============================================ 93 ===========================================
# p=lambda g,c=-3:c*g or p([[s[i]or any(s[:i])*any(s[i:])*8for i in range(len(s))]for s in zip(*g)],c+1)
# p=lambda g,c=-3:c*g or p((l:=[0]*len(g[0]))and[(l:=[s[i]or(any(s[:i])*any(s[i:])or(l.count(8),v)==(1,8))*8for i,v in enumerate(l)])for s in zip(*g[::-1])],c+1)

# p=lambda g,c=-3:c*g or p([[s[i]or([*s,5].index(5)<i<[*s,5].index(5,4))*8for i in range(10)]for s in zip(*g[::-1])],c+1)
p=lambda g,c=-3:c*g or[[s[i]or((f:=[*s,5].index)(5)<i<f(5,4))*8for i in range(10)]for s in zip(*p(g,c+1)[::-1])]


# def p(g):
#  for _ in range(4):
#   *g,=map(list,zip(*g[::-1]))
#   for s in g:
#    l=[*s,5].index(5)
#    r=[*s,5].index(5,4)
#    for i in range(l+1,r):
#     s[i]=s[i] or 8
#  return g
