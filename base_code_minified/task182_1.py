def p(A):
	P,Q=len(A),len(A[0]);R={A for B in A for A in B if A};F={B:sum(A.count(B)for A in A)for B in R};C,L=max(F,key=F.get),min(F,key=F.get);Y=min(A for(A,B)in enumerate(A)for(E,D)in enumerate(B)if D==C);Z=max(A for(A,B)in enumerate(A)for(E,D)in enumerate(B)if D==C);a=min(B for A in A for(B,D)in enumerate(A)if D==C);b=max(B for A in A for(B,D)in enumerate(A)if D==C);M,S,N,T=Y+1,Z,a+1,b;c=[(B-M,C-N)for B in range(M,S)for C in range(N,T)if A[B][C]==L];d,e=S-M,T-N;U=[A for A in R if A not in(C,L)];V=U[0]if U else None;G=set()
	for H in range(P):
		for I in range(Q):
			if A[H][I]==V and(H,I)not in G:
				O=[(H,I)];B=[];G.add((H,I))
				while O:
					J,K=O.pop();B.append((J,K))
					for(f,g)in((1,0),(-1,0),(0,1),(0,-1)):
						D,E=J+f,K+g
						if 0<=D<P and 0<=E<Q and A[D][E]==V and(D,E)not in G:G.add((D,E));O.append((D,E))
				W,h=min(A for(A,B)in B),max(A for(A,B)in B);X,i=min(A for(B,A)in B),max(A for(B,A)in B)
				if h-W+1==d and i-X+1==e and set((A-W,B-X)for(A,B)in B)==set(c):
					for(J,K)in B:A[J][K]=L
	return A