R=range
def	p(g):
	h=len(g);w=h*len(g[0]);s=[i	for	i	in	R(w)if	g[i%h][i//h]==8];y,x=min(i%h	for	i	in	s),min(i//h	for	i	in	s)
	for	k	in	R(w):
		if(i:=k%h)<h-1and	len({g[i+1][j:=k//h],g[i][j],g[i][j+1]})>2:
			m=g[i].index(0,j+1)-j-1;o=[g[i+l][j:j+m+2]for	l	in	R(m+2)]
			for	c	in	R(m*m):
				if	g[y+(u:=c%m)][x+(v:=c//m)]:o[u+1][v+1]=(u+v==m-1or	u-v==0)and	8or[o[t:=u-v>0][1-t],o[-2+t][-1-t]][u+v>=m]
			return	o