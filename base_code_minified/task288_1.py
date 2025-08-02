def p(g):
	A=g[-1];E=min({*A}-{0},key=A.count);F=[A for(A,B)in enumerate(A)if B==E];G,H=F[0],F[-1];I=len(g)-2;J=len(g[0])
	for B in range(1,len(g)):
		C=I-B
		if C<0:break
		for D in(G-B,H+B):
			if 0<=D<J and g[C][D]==0:g[C][D]=E
	return g