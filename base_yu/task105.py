# best: 126(import itertools, jailctf merger) / others: 148(Code Golf International), 148(4atj sisyphus luke Seek mukundan), 153(ox jam), 172(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 181(MasukenSamba)
# =========================================================== 126 ============================================================
# p=lambda g,c=33:g*-c or c<2and p([*zip(*[[v or(s[1:-1].count(1)>1or i%~-len(g)<1)*2for v in s]for i,s in enumerate(g)])],c-1)or[*zip(*p([*zip(*g[any(g[-1])-2::-1])],c-1))][::-1]+g[-1:]
# p=lambda g,c=35:g*-c or c<4and p([*zip(*[[v or(s[1:-1].count(1)>(i>0))*2for v in s]for i,s in enumerate(g)][::-1])],c-1)or[*zip(*p([*zip(*g[any(g[-1])-2::-1])],c-1))][::-1]+g[-1:]
# p=lambda g,c=35:g*-c or c<4and p([*zip(*[[v or(i<s[1:-1].count(1)**3)*2for v in s]for i,s in enumerate(g)][::-1])],c-1)or[*zip(*p([*zip(*g[any(g[-1])-2::-1])],c-1))][::-1]+g[-1:]
# p=lambda g,c=35,f=0:g*-c or c<4and p([*zip(*[f:=[v or(s[1:-1].count(1)>1 or f==0)*2for v in s]for s in g][::-1])],c-1)or[*zip(*p([*zip(*g[any(g[-1])-2::-1])],c-1))][::-1]+g[-1:]
# p=lambda g,c=35,f=0:g*-c or c<4and p([*zip(*[[v or(f<s[1:-1].count(1)**3)*2for v in s]*(f:=1)for s in g][::-1])],c-1)or[*zip(*p([*zip(*g[any(g[-1])-2::-1])],c-1))][::-1]+g[-1:]
p=lambda g,c=35,f=0:g*-c or c<4and[*zip(*[[v or(f<s[1:-1].count(1)**3)*2for v in s]*(f:=1)for s in p(g,c-1)][::-1])]or[*zip(*p([*zip(*g[any(g[-1])-2::-1])],c-1))][::-1]+g[-1:]

# def p(g,c=-31):
#  if c==3:
#   return g
#  if c==1 or c==2:
#   return p([*zip(*[[v or (s[1:-1].count(1)>1 or i%(len(g)-1)<1)*2 for v in s]for i,s in enumerate(g)])],c+1)
#  return [*zip(*p([*zip(*g[any(g[-1])-2::-1])],c+1))][::-1]+g[-1:]

# def p(g,c=-31):
#  if c>0:
#   return [[s[j] or (sum(s[1:-1])>1 or sum(t[1:-1])>1 or i%(len(g)-1)==0 or j%(len(s)-1)==0)*2 for j,t in enumerate(zip(*g))]for i,s in enumerate(g)]
#  return [*zip(*p([*zip(*g[any(g[-1])-2::-1])],c+1))][::-1]+g[-1:]
