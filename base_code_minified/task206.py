def p(g):
	B=sum(g,[]);C=[A for A in set(B)if B.count(A)==1][0];A=[(B,E,A)for(B,D)in enumerate(g)for(E,A)in enumerate(D)if A and A!=C];D=(min(A for(A,B,C)in A)+max(A for(A,B,C)in A))//2;E=(min(A for(B,A,C)in A)+max(A for(B,A,C)in A))//2;F,G=next((A,D)for(A,B)in enumerate(g)for(D,E)in enumerate(B)if E==C);H,I=F-D,G-E
	for(J,K,L)in A:g[J+H][K+I]=L
	return g