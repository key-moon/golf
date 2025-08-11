def p(g,A=range(9),B=range(3)):
 c,a=__import__('collections').Counter(g[0]+g[1]+g[2]).most_common(1)[0][0],[[0 for _ in A]for _ in A]
 for y,x in[(y,x)for x in B for y in B if g[y][x]==c]:
  for i in A:a[3*y+i%3][3*x+i//3]=g[i%3][i//3]
 return a