def p(A):
	L=len(A);H=len(A[0]);I=[];M=0
	for B in range(L):
		for C in range(H):
			if A[B][C]:
				N=A[B][C];J=[(B,C)];A[B][C]=0;K=[]
				while J:
					D,E=J.pop();K.append((D,E))
					for(P,Q)in((1,0),(-1,0),(0,1),(0,-1)):
						F=D+P;G=E+Q
						if 0<=F<L and 0<=G<H and A[F][G]==N:A[F][G]=0;J.append((F,G))
				if len(K)>len(I):I=K;M=N
	O=[[0]*H for A in A]
	for(D,E)in I:O[D][E]=M
	return O