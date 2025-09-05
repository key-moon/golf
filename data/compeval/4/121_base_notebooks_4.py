def	p(g):
	for	i	in	range(1,len(g)-1):
		for	j	in	range(1,len(g[0])-1):
			if	g[i][j]==8:
				v=[]
				for	e	in[-1,0,1]:
					for	f	in[-1,0,1]:
						if(e	or	g)and	g[i+e][j+f]:v.append(g[i+e][j+f])
				c=max(set(v),key=v.count);r=[[g[i+e][j+f]for	f	in[-1,0,1]]for	e	in[-1,0,1]];r[1][1]=c;return	r