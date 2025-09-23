def p(j):
	I,F=len(j),len(j[0]);U=[(A,B)for A in(-4,0,4)for B in(-4,0,4)if A|B];D=range;K=[F]*10;L=[I]*10;M=[-1]*10;N=[-1]*10
	for B in D(I):
		for C in D(F):
			A=j[B][C]
			if C<K[A]:K[A]=C
			if B<L[A]:L[A]=B
			if C>M[A]:M[A]=C
			if B>N[A]:N[A]=B
	for A in D(1,10):
		if M[A]-K[A]==2 and N[A]-L[A]==2:E,J=K[A],L[A];break
	O=[[0]*F for A in j]
	for R in D(3):O[J+R][E:E+3]=j[J+R][E:E+3]
	V=[(B,A)for A in D(3)for B in D(3)if j[J+A][E+B]]
	for(S,T)in U:
		C=E+S;B=J+T;A=0
		for P in D(3):
			for Q in D(3):
				G,H=C+Q,B+P
				if 0<=G<F and 0<=H<I and j[H][G]:A=j[H][G];break
			if A:break
		if not A:continue
		C=E;B=J
		while 1:
			C+=S;B+=T
			if not(-3<C<F and-3<B<I):break
			for(Q,P)in V:
				G,H=C+Q,B+P
				if 0<=G<F and 0<=H<I:O[H][G]=A
	return O