def	p(j):
	E=len(j);c=len(j[0]);F=[]
	for	k	in	range(E):
		for	D	in	range(c):
			if	j[k][D]==5:
				l=[(k,D)];j[k][D]=0;B=[]
				while	l:
					a,A=l.pop();B+=[(a,A)]
					for(e,C)in(a+1,A),(a-1,A),(a,A+1),(a,A-1):
						if	0<=e<E	and	0<=C<c	and	j[e][C]==5:j[e][C]=0;l+=[(e,C)]
				F+=B,
	for(B,w)in	zip(sorted(F,key=len),(2,4,1)):
		for(a,A)in	B:j[a][A]=w
	return	j