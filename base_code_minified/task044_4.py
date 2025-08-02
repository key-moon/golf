def p(g):
	L,J=len(g),len(g[0]);K=[[0]*J for A in g];R=[];S=[]
	for D in range(L):
		for E in range(J):
			if g[D][E]and not K[D][E]:
				M=g[D][E];N=[(D,E)];K[D][E]=1;O=[]
				while N:
					A,B=N.pop();O.append((A,B))
					for(F,G)in((A+1,B),(A-1,B),(A,B+1),(A,B-1)):
						if 0<=F<L and 0<=G<J and not K[F][G]and g[F][G]==M:K[F][G]=1;N.append((F,G))
				T,U=zip(*O);H,I,P,Q=min(T),max(T),min(U),max(U);C=(H+I<L)+(P+Q<J)*2
				if M==5:R.append((C,H,I,P,Q))
				else:S.append((C,H,I,P,Q,M,O))
	for(C,H,I,V,W)in R:
		for(X,e,f,h,i,Y,Z)in S:
			if C==X:
				for(A,B)in Z:g[A][B]=0
				a=H+1 if C<2 else I-2;b=V+1 if C%2==0 else W-2
				for c in(0,1):
					for d in(0,1):g[a+c][b+d]=Y
	return g