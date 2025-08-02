def p(g):
	C,D=len(g),len(g[0]);E=[(A,B)for A in range(C)for B in range(D)if g[A][B]];A=[g[A][B]for(A,B)in E];F=max({*A},key=A.count);G=next(A for A in{*A}if A!=F);H=[(2*A,2*B,C)for((A,B),C)in zip(E,A)];B=[(A,B)for(A,B,C)in H if C==G];I=sum(A for(A,B)in B)//len(B);J=sum(A for(B,A)in B)//len(B);O=max(abs(A-I)+abs(B-J)for(A,B,C)in H);K=[[0]*D for A in range(C)]
	for L in range(C):
		for M in range(D):
			N=abs(2*L-I)+abs(2*M-J)
			if N<=O:K[L][M]=F if N//2%2==0 else G
	return K