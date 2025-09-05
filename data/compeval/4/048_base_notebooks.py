def	f(j,A,c):
	global	W;l.append((j,A))
	for	B	in	C(j-1,j+2):
		for	k	in	C(A-1,A+2):
			if(B,k)in	l:continue
			l.append((B,k))
			if	B<0	or	B>=J	or	k<0	or	k>=a	or(B,k)in[(K,L),(K+1,L),(K,L+1),(K+1,L+1)]:continue
			if	c[B][k]==2:W=8
			if	c[B][k]==8:f(B,k,c)
def	p(c):
	global	W,l,K,L,J,a,C;W,l,J,a,C,e=0,[],len(c),len(c[0]),range,enumerate
	for(K,w)in	e(c):
		for(L,b)in	e(w):
			if	b==2:
				for	A	in	C(K-1,K+3):
					for	k	in	C(L-1,L+3):
						if	A>=0and	A<J	and	k>=0and	k<a	and	c[A][k]==8:f(A,k,c)
				return[[W]]