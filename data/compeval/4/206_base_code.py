def	p(g):
	A=[]
	for(y,C)in	enumerate(g):
		for(x,v)in	enumerate(C):
			if	v==5:B=y,x
			elif	v:A.append((y,x,v))
	D,E=min(y	for(y,_,_)in	A),max(y	for(y,_,_)in	A);F,G=min(x	for(_,x,_)in	A),max(x	for(_,x,_)in	A);H,I=(D+E)//2,(F+G)//2;J,K=B[0]-H,B[1]-I;g[B[0]][B[1]]=0
	for(y,x,v)in	A:g[y+J][x+K]=v
	return	g