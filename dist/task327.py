def p(g):
  h=len(g);n=h*2;return[[sum((g[r-k][c-k]if 0<=r-k<h and 0<=c-k<h else 0)for k in range(n))for c in range(n)]for r in range(n)]