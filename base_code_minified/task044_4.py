def p(A):
	M,K=len(A),len(A[0]);L=[[0]*K for A in A];S=[];T=[]
	for E in range(M):
		for F in range(K):
			if A[E][F]and not L[E][F]:
				N=A[E][F];O=[(E,F)];L[E][F]=1;P=[]
				while O:
					B,C=O.pop();P.append((B,C))
					for(G,H)in((B+1,C),(B-1,C),(B,C+1),(B,C-1)):
						if 0<=G<M and 0<=H<K and not L[G][H]and A[G][H]==N:L[G][H]=1;O.append((G,H))
				U,V=zip(*P);I,J,Q,R=min(U),max(U),min(V),max(V);D=(I+J<M)+(Q+R<K)*2
				if N==5:S.append((D,I,J,Q,R))
				else:T.append((D,I,J,Q,R,N,P))
	for(D,I,J,W,X)in S:
		for(Y,f,g,h,i,Z,a)in T:
			if D==Y:
				for(B,C)in a:A[B][C]=0
				b=I+1 if D<2 else J-2;c=W+1 if D%2==0 else X-2
				for d in(0,1):
					for e in(0,1):A[b+d][c+e]=Z
	return A