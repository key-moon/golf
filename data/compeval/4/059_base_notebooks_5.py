def	p(j,A=enumerate,c=range(11)):
	E=0;k=[[0if(i+1)%4>0and(j+1)%4>0else	5for	i	in	c]for	j	in	c];C={'00':0,'01':0,'02':0,'10':0,'11':0,'12':0,'20':0,'21':0,'22':0}
	for(l,D)in	A(j):
		for(a,B)in	A(D):
			if	B>0and	B!=5:E=int(B);C[str(l//4)+str(a//4)]+=1
	e=max(C.values())
	for(l,D)in	A(k):
		for(a,B)in	A(D):
			if	B==0and	C[str(l//4)+str(a//4)]==e:k[l][a]=E
	return	k