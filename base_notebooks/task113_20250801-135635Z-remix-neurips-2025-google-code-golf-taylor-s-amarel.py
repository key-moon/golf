def p(g):
 H,W=len(g),len(g[0]);m=H//2
 top=g[:m]
 return top + top[::-1]