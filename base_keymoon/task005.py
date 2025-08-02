def p(g):
  h=19
  for i in range(361):
    if [g[i//h+Y][i%h+X]for Y in(0,1,2)for X in(0,1,2)].count(0)<2:
      g[i//h][i%h:i%h+3]=[1,1,1]
      g[i//h+1][i%h:i%h+3]=[1,1,1]
      g[i//h+2][i%h:i%h+3]=[1,1,1]
      return g
      # # [y*19+x for y, x in [(-4,-4),(-4,0),(-4,4),(0,-4),(0,4),(4,-4),(4,0),(4,4)]]
      # for d in [-80, -76, -72, -4, 4, 72, 76, 80]:
      #   g[i//h][i%h:][:3]
  assert False
