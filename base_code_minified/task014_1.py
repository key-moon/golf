def p(g):
	A,B=len(g),len(g[0]);D=[A for(A,C)in enumerate(g)if C.count(0)==B];I,C=D[0],D[-1];E=[B for B in range(B)if all(g[A][B]==0 for A in range(A))];F,J=E[0],E[-1];K={A for B in range(I)for A in g[B]if A};L={A for B in range(C+1,A)for A in g[B]if A};M=(L-K).pop()
	if any(g[A][B]==M for A in range(C+1,A)for B in range(F)):G,H=0,F
	else:G,H=J+1,B
	return[A[G:H]for A in g[C+1:A]]