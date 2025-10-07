# best: 171(ox jam) / others: 177(jailctf merger), 178(4atj sisyphus luke Seek mukundan), 193(jacekw Potatoman nauti natte), 204(intgrah jimboko awu macaque sammyuri), 210(JRKKX)
# ================================================================================== 171 ==================================================================================
# lambda g,c=7:-c*g or c<4and p([*zip(*[[max(max(g))]*99]+g[1:])][::-1],c-1)or g[:(t:=g.index(max(g,key=any))+1)]+[*zip(*p([*zip(*g[t:][::-1])],c-1))][::-1]
# lambda g,c=7:-c*g or c<4and p([*zip(*g[:0:-1],[max(max(g))]*99)],c-1)or g[:(t:=g.index(max(g,key=any))+1)]+[*zip(*p([*zip(*g[t:][::-1])],c-1))][::-1]
# lambda g,c=7:-c*g or c<4and[*zip(*p(g,c-1)[:0:-1],[max(max(g))]*99)]or g[:(t:=g.index(max(g,key=any))+1)]+[*zip(*p([*zip(*g[t:][::-1])],c-1))][::-1]
# lambda g,c=7:-c*g or[[*zip(*p(g,c-1)[:0:-1],[max(max(g))]*99)],g[:(t:=g.index(max(g,key=any))+1)]+[*zip(*p([*zip(*g[t:][::-1])],c-1))][::-1]][c>3]
p=lambda g,c=7:-c*g or[[*zip(*p(g,c-1)[:0:-1],[max(max(g))]*99)],g[:(t:=g.index(max(g,key=any)))+1]+[*zip(*p([*zip(*g[:t:-1])],c-1))][::-1]][c>3]

# def p(g,c=-3):
#  if c==5:
#   return g
#  if c>0:
#   return p([*zip(*[[max(max(g))]*len(g[0])]+g[1:])][::-1],c+1)
#  return g[:(t:=g.index(max(g,key=any))+1)]+[*zip(*p([*zip(*g[t:][::-1])],c+1))][::-1]

# def p(e):
#  b,i=zip(*[(a,n)for(a,o)in enumerate(e)for(n,j)in enumerate(o)if j==5])
#  g,={*sum(e,[])}-{0,5}
#  f,m=min(b)+1,max(b)-1
#  r,d=min(i)+1,max(i)-1
#  for n in range(r,d+1):e[f][n]=e[m][n]=g
#  for a in range(f,m+1):e[a][r]=e[a][d]=g
#  return e
