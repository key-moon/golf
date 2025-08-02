def p(g):
	B,C=len(g),len(g[0]);L=[(A,B,g[A][B])for A in range(B)for B in range(C)if g[A][B]];(M,N,F),(O,P,G)=L;A=C>B;H=sorted([(N,F),(P,G)])if A else sorted([(M,F),(O,G)]);E,Q=H[0];R,S=H[1];I=R-E;D=0
	while E+D*I<(C if A else B):
		J=E+D*I;T=Q if D%2<1 else S
		for K in range(B*A+C*(1-A)):g[A*K+(1-A)*J][A*J+(1-A)*K]=T
		D+=1
	return g