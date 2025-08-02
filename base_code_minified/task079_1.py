def p(A):
	L=len(A);J=len(A[0]);G=[[0]*J for A in A];H={}
	for B in range(L):
		for C in range(J):
			if A[B][C]and not G[B][C]:
				D=A[B][C];K=[(B,C)];G[B][C]=1;I=[]
				while K:
					M,N=K.pop();I.append((M,N))
					for(P,Q)in((1,0),(0,1),(-1,0),(0,-1)):
						E,F=M+P,N+Q
						if 0<=E<L and 0<=F<J and not G[E][F]and A[E][F]==D:G[E][F]=1;K.append((E,F))
				R=min(A for(A,B)in I);S=min(A for(B,A)in I);T=tuple(D if(R+A,S+B)in I else 0 for A in range(3)for B in range(3));H.setdefault(D,[]).append(T)
	D=max(H,key=lambda W:len(H[W]));O=H[D];U=max(set(O),key=O.count);return[list(U[A*3:(A+1)*3])for A in range(3)]