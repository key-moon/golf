def p(u):
	l=range;r=len(u);n=[[0]*r for k in l(r)]
	def k(t,e):
		if 0<=t<r and 0<=e<r and not n[t][e]and u[t][e]==0:n[t][e]=1;[k(t+r,e+l)for(r,l)in[(1,0),(-1,0),(0,1),(0,-1)]]
	[k(l,0)or k(l,r-1)or k(0,l)or k(r-1,l)for l in l(r)];u=[[3 if u[k][r]==0 and not n[k][r]else u[k][r]for r in l(r)]for k in l(r)];return[[3 if r==3 else 0 for r in r]for r in u]