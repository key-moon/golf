def p(j,A=enumerate):
	D=[]
	for(E,G)in A(j):
		for(F,I)in A(G):
			if j[E][F]==1:D+=[[E,F]]
	for H in D:
		B,C=H
		if B>0:j[B-1][C]=2
		if B<9:j[B+1][C]=8
		if C>0:j[B][C-1]=7
		if C<9:j[B][C+1]=6
	return j