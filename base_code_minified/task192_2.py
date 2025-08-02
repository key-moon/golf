def p(val_g):
	A=val_g;K,L=len(A),len(A[0]);I=max(set(sum(A,[]))-{0},key=lambda v:sum(A.count(v)for A in A));J=set();N=[]
	for E in range(K):
		for F in range(L):
			if A[E][F]==I and(E,F)not in J:
				B=[E,F,E,F];M=[(E,F)];J.add((E,F))
				while M:
					C,D=M.pop();B[0]=min(B[0],C);B[1]=min(B[1],D);B[2]=max(B[2],C);B[3]=max(B[3],D)
					for(O,P)in((1,0),(-1,0),(0,1),(0,-1)):
						G,H=C+O,D+P
						if 0<=G<K and 0<=H<L and A[G][H]==I and(G,H)not in J:J.add((G,H));M.append((G,H))
				N.append(B)
	for(Q,R,S,T)in N:
		for C in range(Q,S+1):
			for D in range(R,T+1):A[C][D]=I
	for C in range(K):
		for D in range(L):
			if A[C][D]!=I:A[C][D]=0
	return A