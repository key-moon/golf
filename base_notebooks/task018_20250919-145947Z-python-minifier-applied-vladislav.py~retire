'\nTask 018 – Optimization reminder (moved from TODO_changed_programs.txt)\n- Direct solver (no DSL) now at ~2.3KB with 100% accuracy.\n- Consider further golfing to increase score:\n  * Inline helpers\n  * Compress D4 transforms\n  * Reduce temporary variables\n'
def dc(G):
	A={}
	for C in G:
		for B in C:
			if B:A[B]=A.get(B,0)+1
	return max(A,key=A.get)if A else 0
def o(G):
	F,H=len(G),len(G[0]);C=[[False]*H for A in range(F)];L=[]
	for D in range(F):
		for E in range(H):
			if G[D][E]and not C[D][E]:
				I=[(D,E)];C[D][E]=True;M=[];N=set()
				while I:
					J,K=I.pop();O=G[J][K];N.add(O);M.append((J,K,O))
					for(P,Q)in((1,0),(-1,0),(0,1),(0,-1)):
						A,B=J+P,K+Q
						if 0<=A<F and 0<=B<H and G[A][B]and not C[A][B]:C[A][B]=True;I.append((A,B))
				L.append({'c':M,'p':N})
	return L
T=lambda i,j:(i,j),lambda i,j:(j,-i),lambda i,j:(-i,-j),lambda i,j:(-j,i),lambda i,j:(-i,j),lambda i,j:(i,-j),lambda i,j:(j,i),lambda i,j:(-j,-i)
def mt(G,cs):
	D,E=len(G),len(G[0]);F=max(A for(A,B,B)in cs)+1;H=max(B for(A,B,A)in cs)+1;A=[]
	for B in range(D-F+1):
		for C in range(E-H+1):
			for(I,J,K)in cs:
				if G[B+I][C+J]!=K:break
			else:A.append((B,C))
	return A
def s(G,si,sj,cs):
	for(A,B,C)in cs:G[si+A][sj+B]=C
def p(g):
	if not g:return g
	B=[A[:]for A in g];F=dc(B);G=[A for A in o(B)if len(A['c'])>3 and len(A['p'])>1]
	for D in G:
		H=D['c'];I=[(B,C,A)for(B,C,A)in H if A!=F]
		if not I:continue
		J=set()
		for E in T:
			C=[(E(A,B)[0],E(A,B)[1],C)for(A,B,C)in H];K=min(A for(A,B,B)in C);L=min(B for(A,B,A)in C);C=[(A-K,B-L,C)for(A,B,C)in C];A=[(E(A,B)[0],E(A,B)[1],C)for(A,B,C)in I];A=[(A-K,B-L,C)for(A,B,C)in A];M=min(A for(A,B,B)in A);N=min(B for(A,B,A)in A);O=[(A-M,B-N,C)for(A,B,C)in A];P=tuple(sorted((A,B,C)for(A,B,C)in O))
			if P in J:continue
			J.add(P)
			for(Q,R)in mt(B,O):s(B,Q-M,R-N,C)
	for D in G:
		if F in D['p']:
			for(A,S,U)in D['c']:B[A][S]=0
	return B