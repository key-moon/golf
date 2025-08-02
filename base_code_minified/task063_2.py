def p(g):
	import numpy as F;D=F.array(g);G=D==0;A=F.pad(G,1);E=list({(0,A)for A in range(A.shape[1])}|{(A.shape[0]-1,B)for B in range(A.shape[1])}|{(A,0)for A in range(A.shape[0])}|{(B,A.shape[1]-1)for B in range(A.shape[0])})
	while E:
		B,C=E.pop()
		if A[B,C]:A[B,C]=0;E+=(B+1,C),(B-1,C),(B,C+1),(B,C-1)
	D[A[1:-1]&G]=3;return D.tolist()