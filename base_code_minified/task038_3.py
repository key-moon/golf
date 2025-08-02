def p(A):
	J=len(A);D=set();H=0
	for(E,K)in enumerate(A):
		for(F,L)in enumerate(K):
			if L==1 and(E,F)not in D:
				G=[(E,F)];D.add((E,F));I=0
				while G:
					M,N=G.pop();I+=1
					for(O,P)in((1,0),(-1,0),(0,1),(0,-1)):
						B,C=M+O,N+P
						if 0<=B<J and 0<=C<len(A[0])and A[B][C]==1 and(B,C)not in D:D.add((B,C));G.append((B,C))
				if I>1:H+=1
	return([1]*H+[0]*5)[:5]