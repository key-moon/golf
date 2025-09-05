def	p(j,A=range):
	c=len(j);C=len(j[0]);k=len({*sum(j,[])}-{0});j=[[j[l//k][A//k]for	A	in	A(C*k)]for	l	in	A(c*k)];c*=k;C*=k
	for	B	in	A(min(c,C),0,-1):
		for	l	in	A(c-B+1):
			for	D	in	A(C-B+1):
				a=j[l][D]
				if	a	and	all(r[D:D+B]==[a]*B	for	r	in	j[l:l+B]):
					for(F,e)in(-1,-1),(-1,B),(B,-1),(B,B):
						E=l+F;w=D+e
						while-1<E<c	and-1<w<C	and	not	j[E][w]:j[E][w]=2;E+=F>0	or-1;w+=e>0	or-1
					return	j