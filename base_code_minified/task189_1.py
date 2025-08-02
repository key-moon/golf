def p(A):
	for(B,E)in enumerate(A):
		if E.count(8)==len(E):break
	for(C,F)in enumerate(zip(*A)):
		if F.count(8)==len(F):break
	G=[[A[:C]for A in A[:B]],[A[C+1:]for A in A[:B]],[A[:C]for A in A[B+1:]],[A[C+1:]for A in A[B+1:]]];J=next(A for A in G if len(A)==2 and len(A[0])==2);D=next(A for A in G if len(A)>2 and len(A[0])>2);H,I=len(D),len(D[0]);K,L=H//2,I//2;return[[D[A][B]//3*J[A//K][B//L]for B in range(I)]for A in range(H)]