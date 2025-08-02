def p(A):
	J,K=len(A),len(A[0]);G=set();B=set();L=0
	for C in range(J):
		for D in range(K):
			if A[C][D]and(C,D)not in G:
				M=A[C][D];H=[(C,D)];G.add((C,D));I={(C,D)}
				while H:
					N,O=H.pop()
					for(P,Q)in((1,0),(-1,0),(0,1),(0,-1)):
						E,F=N+P,O+Q
						if 0<=E<J and 0<=F<K and A[E][F]==M and(E,F)not in G:G.add((E,F));H.append((E,F));I.add((E,F))
				if len(I)>len(B):B=I;L=M
	R,S=min(A for(A,B)in B),max(A for(A,B)in B);T,U=min(A for(B,A)in B),max(A for(B,A)in B);return[[L if(A,C)in B else 0 for C in range(T,U+1)]for A in range(R,S+1)]