# best: 94(xsot ovs att joking mewheni) / others: 105(4atj sisyphus luke Seek mukundan), 107(jailctf merger), 108(natte), 110(intgrah jimboko awu macaque sammyuri), 130(MasukenSamba)
# ============================================ 94 ============================================

# p=lambda g,c=-19,E=enumerate:c*g or p([[v or i+1<len(g) and j>0 and g[i+1][~(j-1)] and 15-g[i+1][~(j-1)] for j,v in E(s[::-1])] for i,s in E(g)],c+1)
# p=lambda g,c=-19,E=enumerate:c*g or p([[v or j>0 and t[~(j-1)] and 15-t[~(j-1)] for j,v in E(s[::-1])] for s,t in zip(g,g[1:]+g[-1:])],c+1)
# p=lambda g,c=-19:c*g or p([[v or w and 15-w for v,w in zip(s,[0]+t)][::-1]for s,t in zip(g,g[1:]+g[-1:])],c+1)
# p=lambda g,c=-19:c*g or p([[v|(15-w)%15for v,w in zip(s,[0]+t)][::-1]for s,t in zip(g,g[1:]+g[-1:])],c+1)
p=lambda g,c=-19:c*g or p([[v|-w%15for v,w in zip(s,[0]+t)][::-1]for s,t in zip(g,g[1:]+g[-1:])],c+1)

# 7:8
# 8:7
# 0:0


# def p(g):
#  for _ in range(20):
#   for i in range(len(g)):
#    for j in range(len(g[i])):
#     g[i][j]=g[i][j] or i+1<len(g) and j>0 and g[i+1][j-1] and 15-g[i+1][j-1]
#   g=[s[::-1]for s in g]
#  return g
