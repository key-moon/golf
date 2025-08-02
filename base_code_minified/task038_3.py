def p(g):
	I=len(g);C=set();G=0
	for(D,J)in enumerate(g):
		for(E,K)in enumerate(J):
			if K==1 and(D,E)not in C:
				F=[(D,E)];C.add((D,E));H=0
				while F:
					L,M=F.pop();H+=1
					for(N,O)in((1,0),(-1,0),(0,1),(0,-1)):
						A,B=L+N,M+O
						if 0<=A<I and 0<=B<len(g[0])and g[A][B]==1 and(A,B)not in C:C.add((A,B));F.append((A,B))
				if H>1:G+=1
	return([1]*G+[0]*5)[:5]