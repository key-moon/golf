def p(A):
	K,L=len(A),len(A[0]);G=[(B,C)for B in range(K)for C in range(L)if A[B][C]==2];T=min(A for(A,B)in G);U=max(A for(A,B)in G);V=min(A for(B,A)in G);W=max(A for(B,A)in G);M=[(B,C)for B in range(K)for C in range(L)if A[B][C]==5];H=set(M);N=[]
	while H:
		B,C=H.pop();J=[(B,C)];D=[(B,C)]
		while J:
			X,Y=J.pop()
			for(E,F)in((1,0),(-1,0),(0,1),(0,-1)):
				I=X+E,Y+F
				if I in H:H.remove(I);J.append(I);D.append(I)
		N.append(D)
	for(B,C)in M:A[B][C]=0
	for D in N:
		O=[A for(A,B)in D];P=[A for(B,A)in D];Z,a=T+1-min(O),U-1-max(O);b,c=V+1-min(P),W-1-max(P);Q=10**9
		for E in range(Z,a+1):
			for F in range(b,c+1):
				R=1
				for(B,C)in D:
					if A[B+E][C+F]!=0:R=0;break
				if R:
					S=abs(E)+abs(F)
					if S<Q:Q=S;d,e=E,F
		for(B,C)in D:A[B+d][C+e]=5
	return A