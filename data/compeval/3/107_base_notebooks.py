def	p(j,p=range):
	B=len(j);c=len(j[0]);A=len({*sum(j,[])}-{0});j=[[j[B//A][l//A]for	l	in	p(c*A)]for	B	in	p(B*A)];B*=A;c*=A
	for	k	in	p(min(B,c),0,-1):
		for	C	in	p(B-k+1):
			for	l	in	p(c-k+1):
				E=j[C][l]
				if	E	and	all(r[l:l+k]==[E]*k	for	r	in	j[C:C+k]):
					for(a,F)in(-1,-1),(-1,k),(k,-1),(k,k):
						e=C+a;D=l+F
						while-1<e<B	and-1<D<c	and	not	j[e][D]:j[e][D]=2;e+=a>0	or-1;D+=F>0	or-1
					return	j