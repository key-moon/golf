def p(val_g):
	A=val_g;E=sum(A,[]);F=sorted({*E},key=lambda x:-E.count(x));B=next(A for A in F if A);G=next((A for A in F if A and A!=B),0);C=min(A for(A,C)in enumerate(A)if B in C);H=max(A for(A,C)in enumerate(A)if B in C);D=min(C for(E,A)in enumerate(A)for(C,D)in enumerate(A)if D==B);I=max(C for(E,A)in enumerate(A)for(C,D)in enumerate(A)if D==B);M=(H-C+1)//3;N=(I-D+1)//3;J=[[0]*3 for A in[0]*3]
	for(K,O)in enumerate(A):
		for(L,P)in enumerate(O):
			if P==G and C<=K<=H and D<=L<=I:J[(K-C)//M][(L-D)//N]=G
	return J