A=range
def p(g):
 c=[*filter(int,sum(g,[]))][0]
 for p in A(32):
  x=[[{s[j],(s+g[0])[p-j]}&{0,c}for j in A(16)]for s in g]
  if{0,c}>max(max(x)):return[[*map(sum,s)]for s in x]