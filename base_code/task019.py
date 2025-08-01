def p(g):
 h,w=len(g),len(g[0])
 return[[g[i%h][j%w]or(8 if (i//h+j//w+i+j)&1 else 0)
          for j in range(w*2)]
         for i in range(h*2)]
