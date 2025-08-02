def p(A):
	F,G=len(A),len(A[0]);O=[]
	for P in range(F):
		for Q in range(G):
			if A[P][Q]==2:
				D,E=P,Q;H=[(D,E)]
				for R in H:
					for(L,M)in((1,0),(-1,0),(0,1),(0,-1)):
						B,C=R[0]+L,R[1]+M
						if 0<=B<F and 0<=C<G and A[B][C]==3 and(B,C)not in H:H.append((B,C))
				I=[(A-D,B-E)for(A,B)in H];O.append((D,E,I))
	for(D,E,I)in O:
		for(L,M)in((0,1),(0,-1),(1,0),(-1,0)):
			N=1
			while 1:
				B,C=D+N*L,E+N*M
				if not(0<=B<F and 0<=C<G):break
				for(J,K)in I:
					S,T=B+J,C+K
					if not(0<=S<F and 0<=T<G)or A[S][T]!=0:break
				else:
					for(J,K)in I:A[B+J][C+K]=2 if(J,K)==(0,0)else 3
					N+=1;continue
				break
	return A