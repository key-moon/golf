def p(g):
	C={};Q,R=len(g),len(g[0])
	for S in range(Q):
		for T in range(R):C.setdefault(g[S][T],set()).add((S,T))
	C.pop(0);U=sorted(C.items(),key=lambda i:len(i[1]));V,f=U[0][0],U[-1][0];W,X=C[f],C[V]
	def Y(s):A=[A for(A,B)in s];B=[A for(B,A)in s];return min(A),min(B),max(A),max(B)
	F,K,h,Z=Y(W);G,m,L,n=h-F+1,Z-K+1,0,0;a,b,i,j=Y(X);H=i-a+1;I=j-b+1;k=[[1 if(F+A,K+B)in W else 0 for B in range(L)]for A in range(G)];l=[[1 if(a+A,b+B)in X else 0 for B in range(I)]for A in range(H)];D,E=G*H,L*I;J=[[0]*E for A in range(D)]
	for A in range(G):
		for B in range(L):
			if k[A][B]:
				for c in range(H):
					for d in range(I):
						if l[c][d]:J[A*H+c][B*I+d]=V
	for(M,e)in((0,1),(1,0),(0,-1),(-1,0)):
		N=(F if M>=0 else F-D)+(M>0)*G+M-1;O=(Z+1 if e>0 else K-E)+(e<0)*0
		if 0<=N<=Q-D and 0<=O<=R-E:
			P=1
			for A in range(D):
				for B in range(E):
					if J[A][B]and g[N+A][O+B]:P=0;break
				if not P:break
			if P:
				for A in range(D):
					for B in range(E):
						if J[A][B]:g[N+A][O+B]=J[A][B]
				break
	return g