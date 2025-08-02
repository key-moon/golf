def p(val_g):
	C=val_g;F,G=len(C),len(C[0]);O=[]
	for P in range(F):
		for Q in range(G):
			if C[P][Q]==2:
				D,E=P,Q;H=[(D,E)]
				for R in H:
					for(L,M)in((1,0),(-1,0),(0,1),(0,-1)):
						A,B=R[0]+L,R[1]+M
						if 0<=A<F and 0<=B<G and C[A][B]==3 and(A,B)not in H:H.append((A,B))
				I=[(A-D,B-E)for(A,B)in H];O.append((D,E,I))
	for(D,E,I)in O:
		for(L,M)in((0,1),(0,-1),(1,0),(-1,0)):
			N=1
			while 1:
				A,B=D+N*L,E+N*M
				if not(0<=A<F and 0<=B<G):break
				for(J,K)in I:
					S,T=A+J,B+K
					if not(0<=S<F and 0<=T<G)or C[S][T]!=0:break
				else:
					for(J,K)in I:C[A+J][B+K]=2 if(J,K)==(0,0)else 3
					N+=1;continue
				break
	return C