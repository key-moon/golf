def p(g,I=range):
 h,w,a,b=len(g),len(g[0]),0,0
 for y in I(h):
  for x in I(w):
   if g[y][x]:a,b=y+2,x
 def s(y,x,c):
  if 0<=x<w:g[y][x]=c
 for i in I(w):
  a,c=a-1,7+i%2
  for y in I(a):s(y,b-i,c);s(y,b+i,c)
 return g
