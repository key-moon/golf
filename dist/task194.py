def p(g):
 a=[*map(list,zip(*g[::-1]))]
 b=[*map(list,zip(*g))][::-1]
 c=[i[::-1]for i in g[::-1]]
 return [x+y for x,y in zip(g,a)]+[x+y for x,y in zip(b,c)]