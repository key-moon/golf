def p(j,A=range):
	c,E=len(j),len(j[0]);j=[[2 if k>0 else 0 for k in k]for k in j]
	for k in A(E):
		W=[j[c][k]for c in A(c)][::-1];l=sum(W)//2//2
		for J in A(l):j[-(J+1)][k]=8
	return j