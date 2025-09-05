def	p(g):
	d={}
	for(i,r)in	enumerate(g):
		for(j,v)in	enumerate(r):
			if	v:d.setdefault(v,[]).append((i,j))
	for(s,D)in	d.items():
		A={i	for(i,_)in	D};B={j	for(_,j)in	D}
		if	len(A)>1and	len(B)>1:E,F,G,H=min(A),max(A)+1,min(B),max(B)+1;break
	C=[]
	for(v,D)in	d.items():
		if	v==s:continue
		A={i	for(i,_)in	D};B={j	for(_,j)in	D}
		if(len(A)==1)^(len(B)==1):C.append((v,A,B))
	I=F-E;J=H-G;M,K,N=C[0]
	if	len(K)==1:C.sort(key=lambda	t:next(iter(t[1])));return[[v]*J	for(v,_,_)in	C]
	C.sort(key=lambda	t:next(iter(t[2])));L=[v	for(v,_,_)in	C];return[L]*I