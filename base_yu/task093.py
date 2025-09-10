# best: 99(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 100(xsot ovs att joking mewheni), 125(intgrah jimboko awu macaque sammyuri), 129(jacekwl Potatoman nauti), 138(natte), 157(MasukenSamba)
# =============================================== 99 ==============================================
# p=lambda g:(i:=[*g[0],5].index(5))<9and[([0]*s[:i].count(0)+[5]*(14-s.count(0))+[0]*9)[:14]for s in g]or[*map(list,zip(*p([*zip(*g)])))]
# p=lambda g:(i:=[*g[0],5].index(5))<9and[([0]*s[:i].count(0)+[5]*(14-s.count(0))+[0]*9)[:14]for s in g]or[*zip(*p([*zip(*g)]))]
p=lambda g:5in g[0]and[([0]*s[:s.index(5)].count(0)+[5]*(14-s.count(0))+[0]*9)[:14]for s in g]or[*zip(*p([*zip(*g)]))]


# def p(g):
#  if(i:=[*g[0],5].index(5))<9:
#   return[([0]*s[:i].count(0)+[5]*(14-s.count(0))+[0]*9)[:14]for s in g]
#  return[*map(list,zip(*p([*zip(*g)])))]


# def p(g):
#  for _ in 0,1:
#   if 1-any(all(s)for s in g):
#    for s in g:
#     i=s.index(5)
#     l=s[:i].count(0)
#     r=s[i:].count(0)
#     s[:14]=[0]*l+[5]*(14-l-r)+[0]*r
#   *g,=map(list,zip(*g))
#  return g










