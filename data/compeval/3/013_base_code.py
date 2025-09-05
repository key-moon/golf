def	p(g):
	B,C=len(g),len(g[0]);K=[(y,x,g[y][x])for	y	in	range(B)for	x	in	range(C)if	g[y][x]];(L,M,F),(N,O,G)=K;A=C>B;H=sorted([(M,F),(O,G)])if	A	else	sorted([(L,F),(N,G)]);E,P=H[0];Q,R=H[1];I=Q-E;D=0
	while	E+D*I<(C	if	A	else	B):
		J=E+D*I;S=P	if	D%2<1else	R
		for	_	in	range(B*A+C*(1-A)):g[A*_+(1-A)*J][A*J+(1-A)*_]=S
		D+=1
	return	g