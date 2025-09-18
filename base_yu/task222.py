# best: 103(ox jam, xsot ovs att joking mewheni) / others: 107(jailctf merger), 114(4atj sisyphus luke Seek mukundan), 135(intgrah jimboko awu macaque sammyuri), 144(natte), 228(MasukenSamba)
# ================================================ 103 ================================================

# lambda g,c=-5:c*g or[*zip(*[[(s[i]in[0,*s,0][i:i+3:2] and (hash((*g[0],))>>53 not in (-33,617,325) or s[i]%7==2))*s[i] for i in range(16)]for s in p(g,c+1)])]
# lambda g,c=-5:c*g or p([*zip(*[[(s[i]in[0,*s,0][i:i+3:2]and(c<0 or len({*g})==2 or s[i]in(2,9)))*s[i] for i in range(16)]for s in g])],c+1)
# lambda g,c=-5:c*g or p([*zip(*[[(v in[0,*s,0][i:i+3:2]and(c<0 or len({*g})==2 or v in(2,9)))*v for i,v in enumerate(s)]for s in g])],c+1)
# lambda g,c=-7:c*g or p([[(s[i]in[0,*s,0][i:i+3:2]*(5<sum(g,g[0]).count(s[i])))*s[i] for i in range(16)]for s in zip(*g)],c+1)
# lambda g,c=-7:c*g or p([[(5<sum(g,g[0]).count(v:=s[i]))*(v in[0,*s,0][i:i+3:2])*v for i in range(16)]for s in zip(*g)],c+1)
# p=lambda g,c=-7:c*g or p([[(v in[0,*s,0][i:i+3:2]*(5<sum(g,g[0]).count(v)))*v for i,v in enumerate(s)]for s in zip(*g)],c+1)
p=lambda g,c=-7:c*g or p([[v*(85<sum(g,[0,*s][i:i+3]*40).count(v))for i,v in enumerate(s)]for s in zip(*g)],c+1)
# p=lambda g,c=-7:c*g or p([[sum(g,[0,*s][i:i+3]*40).count(s[i])//85*s[i]for i in range(16)]for s in zip(*g)],c+1)


# def p(g):
#  for _ in range(4):
#   g=[[(s[i]in[0,*s,0][i:i+3:2] and (hash((*g[0],))>>53 not in (-33,617,325) or s[i]%7==2))*s[i] for i in range(16)]for s in g]
#   g=[*zip(*g)]
#  return g
