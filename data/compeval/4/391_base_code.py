def	p(g):
	d={}
	for	v	in	sum(g,[]):
		if	v:d[v]=d.get(v,0)+1
	d.pop(max(d,key=d.get));return[[k]for	k	in	sorted(d,key=d.get,reverse=True)]