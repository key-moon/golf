def p(g):
 AC=len(g[0]);AF=g[-1].index(1);AA=1;AB=[[0]*AC for _ in g]
 for AD in AB[::-1]:
  AD[AF]=1;AE=AF+AA
  (AE<0 or AE>=AC)and(AA:=-AA)
  AF+=AA
 return AB