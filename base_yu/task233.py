# best: 297(jailctf merger) / others: 299(xsot ovs att joking mewheni), 370(garrymoss), 387(MasukenSamba), 391(kdmitrie), 408(jonas ryno kg583)
def p(g):
 for u in range(len(g)):
  for l in range(len(g[0])):
   r=[*g[u],0].index(0,l)
   d=[*(g[k][l]for k in range(len(g))),0].index(0,u)
   if g[u][l]==2 and r-l>5<d-u:
    t=[s[l:r]for s in g[u:d]]
    for _ in range(8):
     for i in range(len(g)-2):
      for j in range(len(g[0])-2):
       for y in range(len(t)-2):
        for x in range(len(t[0])-2):
         if all(g[i+k][j+m]==2 if t[y+k][x+m]==0 else g[i+k][j+m]|2!=2 for k in range(3)for m in range(3))*(y<1 or 0!=t[y-1][x+1])*(y+4>len(t) or 0!=t[y+3][x+1]):
          for k in range(3):
           for m in range(3):
            t[y+k][x+m]=g[i+k][j+m]
            g[i+k][j+m]=0
     *t,=map(list,zip(*t[::-1]))
    return t

