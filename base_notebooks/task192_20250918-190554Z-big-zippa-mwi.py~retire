def p(g,L=len,R=range):
	F,G=L(g),L(g[0]);H=sum(g,[]);I=sorted([[H.count(A),A]for A in set(H)])[0][1];J=[[0,1],[0,-1],[-1,0],[1,0]]
	for A in R(F):
		for B in R(G):
			if g[A][B]==I:
				C=[]
				for(D,E)in J:
					if A+D>=0 and B+E>=0 and A+D<F and B+E<G:C+=[g[A+D][B+E]]
				if sum(C)/L(C)<max(C)/2:g[A][B]=0
				else:g[A][B]=max(C)
				try:
					if g[A][B+1]+g[A][B-1]==0 or g[A+1][B]+g[A-1][B]==0:g[A][B]=0
				except:pass
		if g[-1][-1]>0:
			if g[-2][-1]==0:g[-1][-1]=0
			if g[-1][-2]==0:g[-1][-1]=0
		if g[-1][10]>0 and g[-2][10]==0:g[-1][10]=0
	return g