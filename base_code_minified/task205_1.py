def p(g):
	A={}
	for(S,T)in enumerate(g):
		for(U,B)in enumerate(T):A.setdefault(B,[]).append((S,U))
	E=F=G=H=I=J=0
	for(B,C)in A.items():
		K=[A for(A,B)in C];L=[A for(B,A)in C];M,N=min(K),max(K);O,P=min(L),max(L);D=(N-M+1)*(P-O+1)
		if D==len(C)and D>E:E=D;F=B;G,X=M;H=N;I,Y=O;J=P
	V=sorted([(len(B),A)for(A,B)in A.items()],reverse=1);W=V[1][1];Q=H-G+1;R=J-I+1;return[[F if min(A,B,Q-1-A,R-1-B)%2==0 else W for B in range(R)]for A in range(Q)]