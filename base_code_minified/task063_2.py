def p(A):
	import numpy as G;E=G.array(A);H=E==0;B=G.pad(H,1);F=list({(0,A)for A in range(B.shape[1])}|{(B.shape[0]-1,A)for A in range(B.shape[1])}|{(A,0)for A in range(B.shape[0])}|{(A,B.shape[1]-1)for A in range(B.shape[0])})
	while F:
		C,D=F.pop()
		if B[C,D]:B[C,D]=0;F+=(C+1,D),(C-1,D),(C,D+1),(C,D-1)
	E[B[1:-1]&H]=3;return E.tolist()