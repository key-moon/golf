def p(g):
 h,w=len(g),len(g[0]);K={c for r in g for c in r}-{0}
 if len(K)<2:return g
 f=next(c for r in g for c in r if c);i=(K-{f}).pop();rs,cs,re,ce=max(((a,b,c,d)for a in range(h)for b in range(w)if g[a][b]==i for c in range(a,h)for d in range(b,w)if all(g[y][x]==i for y in range(a,c+1)for x in range(b,d+1))),key=lambda t:(t[2]-t[0]+1)*(t[3]-t[1]+1),default=(-1,-1,-1,-1))
 if rs<0:return g
 P=[(r,c)for r in range(h)for c in range(w)if g[r][c]==i and not(rs<=r<=re and cs<=c<=ce)];R={r for r,c in P if rs<=r<=re};C={c for r,c in P if cs<=c<=ce};M={i:f,0:i}
 return[[M.get(g[r][c],g[r][c])if r in R or c in C else g[r][c]for c in range(w)]for r in range(h)]