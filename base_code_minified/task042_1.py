def p(A):
	I,J=len(A),len(A[0]);T=[(B,C)for B in range(I)for C in range(J)if A[B][C]==3];G=set();N=[]
	for(K,L)in T:
		if(K,L)in G:continue
		M=[(K,L)];B=[];G.add((K,L))
		while M:
			C,D=M.pop();B.append((C,D))
			for(U,V)in[(1,0),(-1,0),(0,1),(0,-1)]:
				E,F=C+U,D+V
				if 0<=E<I and 0<=F<J and(E,F)not in G and A[E][F]==3:G.add((E,F));M.append((E,F))
		N.append(B)
	H=[];O=[]
	for B in N:W=[A for(A,B)in B];X=[A for(B,A)in B];P,Q=min(W),min(X);H.append((P,Q));O.append([(A-P,B-Q)for(A,B)in B])
	Y=sorted({A for(A,B)in H});Z=sorted({A for(B,A)in H})
	for R in Y:
		for S in Z:
			if(R,S)in H:continue
			for a in O:
				for(b,c)in a:
					C,D=R+b,S+c
					if 0<=C<I and 0<=D<J and A[C][D]==0:A[C][D]=8
	return A