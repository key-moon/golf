def p(A):
	F=[[0]*3 for A in[0]*3];J=[(0,0),(0,2),(1,1),(2,0),(2,2)];E=len(A);G=0
	for H in range(E):
		for I in range(E):
			if A[H][I]==2:
				K,L=J[G];F[K][L]=1;G+=1;D=[(H,I)]
				while D:
					B,C=D.pop()
					if A[B][C]!=2:continue
					A[B][C]=0
					if B:D+=[(B-1,C)]
					if B+1<E:D+=[(B+1,C)]
					if C:D+=[(B,C-1)]
					if C+1<E:D+=[(B,C+1)]
	A=F;return A