# best: 101(mukundan, 4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, jailctf merger) / others: 104(xsot ovs att joking mewheni), 107(Yuchen20), 109(Bulmenisaurus), 109(duckyluuk), 118(cg)
# =============================================== 101 ===============================================
# def p(g,c=-1):
#  if c*g:
#   return g
#  n=len(g)//2
#  u=[*zip(*[[t,s][len({*s})+c-1]for s,t in zip(g,g[n+1:])])]
#  print(u)
#  return p(u,c+1)
# p=lambda g:(n:=len(g)//2)and[[(u:=[*sorted([*g[i][j::n+1],*g[i+n+1][j::n+1]])])and u[0]^u[1]^u[3] for j in range(n)]for i in range(n)]
# p=lambda g:(n:=len(g),m:=n//2,G:=sum(g,[]),k:=G.index(min(G,key=G.count)))and[s[(k%n>m)*-m:][:m]for s in g[(k>n*m)*-m:][:m]]
# p=lambda g:(n:=len(g)//2+1)and[[(u:=[*sorted([*s[j::n],*t[j::n]])])and sum(u)-u[2]*3for j in range(n-1)]for s,t in zip(g,g[n:])]
def p(g):
 n=len(g)
 m=n//2
 G=sum(g,[])
 k=G.index(min(G,key=G.count))
 return[s[(k%n>m)*-m:][:m]for s in g[(k>n*m)*-m:][:m]]
