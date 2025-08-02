def p(A):
	B=len(A);F=len(A[0]);D=max(range(B),key=lambda E:sum(map(bool,A[E])));E=[A for A in A[D]if A];I=A[D].index(E[0]);C=max(range(F),key=lambda J:sum(A[B][J]!=0 for B in range(B)));G=[A[B][C]for B in range(B)if A[B][C]];J=next(B for B in range(B)if A[B][C]);A[D]=[E[(A-I)%len(E)]for A in range(F)]
	for H in range(B):A[H][C]=G[(H-J)%len(G)]
	return A