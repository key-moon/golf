def p(g):
 f=sum(g,[])
 C=max([f.count(c) for c in set(f) if c>0])
 M=sum(map(list,zip(*g[::-1])),[])
 M=[c for i,c in enumerate(M) if M.index(c)==i]
 g=[[c for c in M if f.count(c)==C]]*C
 return g
