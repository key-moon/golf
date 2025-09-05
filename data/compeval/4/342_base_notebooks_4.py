def	p(g,E=enumerate):
	A=lambda	a,b:sum([[i,j]for(i,r)in	E(g)for(j,v)in	E(r)if	v	in	a	and	v	not	in	b],[]);a,b,c,d,e,f,h,m=A(range(10),[0,8]);x,y=A([8],[])[:2];g[x][y:y+2]=[g[a][b],g[c][d]][::(1,-1)[b>d]];g[x+1][y:y+2]=[g[e][f],g[h][m]][::(1,-1)[f>m]]
	for(i,j)in(a,b),(c,d),(e,f),(h,m):g[i][j]=0
	return	g