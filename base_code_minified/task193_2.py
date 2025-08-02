def p(A):
	F=len(A);G=len(A[0]);K=[[0]*G for A in range(F)];H=set()
	for D in range(F):
		for E in range(G):
			if A[D][E]and(D,E)not in H:
				L=A[D][E];I=[(D,E)];M=[]
				while I:
					B,C=I.pop()
					if 0<=B<F and 0<=C<G and(B,C)not in H and A[B][C]==L:H.add((B,C));M.append((B,C));I+=(B+1,C),(B-1,C),(B,C+1),(B,C-1)
				J={}
				for(B,C)in M:J.setdefault(B,set()).add(C)
				N=set.intersection(*J.values())
				for B in J:
					for C in N:K[B][C]=L
	return K