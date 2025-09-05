def	p(g):
	d={}
	for(i,r)in	enumerate(g):
		for(j,v)in	enumerate(r):
			if	v:
				a=d.get(v)
				if	a:a[0]=min(a[0],i);a[1]=max(a[1],i);a[2]=min(a[2],j);a[3]=max(a[3],j)
				else:d[v]=[i,i,j,j]
	k=min(d,key=lambda	x:(d[x][1]-d[x][0]+1)*(d[x][3]-d[x][2]+1));a=d[k];return[[k]*(a[3]-a[2]+1)for	_	in	range(a[1]-a[0]+1)]