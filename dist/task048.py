import re
def p(g):
 w=len(g[0])
 for x in range(99):
  if g[i:=x//w][j:=x%w]&2:g[i][j]=1;break
 for x in range(99):g=[re.sub('81|21','11',''.join(map(str,r)))for r in zip(*g[::-1])]
 return[[8-('2'in str(g))*8]]