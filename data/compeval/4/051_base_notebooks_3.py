def	p(j):
	C=range;c=[l[:]for	l	in	j];D,k=len(j),len(j[0]);F={}
	for	l	in	C(D):
		for	A	in	C(k):
			if	j[l][A]:F[j[l][A]]=F.get(j[l][A],0)+1
	l,A,a=next((l,A,j[l][A])for	l	in	C(D)for	A	in	C(k)if	j[l][A]and	F[j[l][A]]==1)
	for(E,e)in[(0,1),(1,0),(0,-1),(-1,0)]:
		G,w=l+E,A+e
		if(G<0)|(G>=D)|(w<0)|(w>=k)|(j[G][w]==0):
			B=1
			while(0<=l-B*E<D)&(0<=A-B*e<k):
				if	j[l-B*E][A-B*e]==0:c[l-B*E][A-B*e]=a
				B+=1
	return	c