def p(A):
	J,K=len(A),len(A[0]);G=set();N=[]
	for B in range(J):
		for C in range(K):
			if A[B][C]==9 and(B,C)not in G:
				D=[(B,C)];G.add((B,C))
				for(S,T)in D:
					for(U,V)in((1,0),(-1,0),(0,1),(0,-1)):
						E,F=S+U,T+V
						if 0<=E<J and 0<=F<K and A[E][F]==9 and(E,F)not in G:G.add((E,F));D.append((E,F))
				N.append(D)
	D=max(N,key=len);O=[A for(A,B)in D];P=[A for(B,A)in D];L,M=min(O),min(P);H=max(O)-L+1;I=max(P)-M+1
	for B in range(J-H+1):
		for C in range(K-I+1):
			if(B,C)!=(L,M)and any(A[B+D][C+E]for D in range(H)for E in range(I))and all(A[B+D][C+E]!=9 for D in range(H)for E in range(I)):
				for Q in range(H):
					for R in range(I):A[L+Q][M+R]=A[B+Q][C+R]
				return A
	return A