def p(val_g):
	C=val_g;F=len(C);G=len(C[0]);K=[[0]*G for A in range(F)];H=set()
	for D in range(F):
		for E in range(G):
			if C[D][E]and(D,E)not in H:
				L=C[D][E];I=[(D,E)];M=[]
				while I:
					A,B=I.pop()
					if 0<=A<F and 0<=B<G and(A,B)not in H and C[A][B]==L:H.add((A,B));M.append((A,B));I+=(A+1,B),(A-1,B),(A,B+1),(A,B-1)
				J={}
				for(A,B)in M:J.setdefault(A,set()).add(B)
				N=set.intersection(*J.values())
				for A in J:
					for B in N:K[A][B]=L
	return K