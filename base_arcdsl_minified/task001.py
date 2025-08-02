def val_func_cellwise(A,B,C):
	I,J=len(A),len(A[0]);D=tuple()
	for F in range(I):
		E=tuple()
		for G in range(J):H=A[F][G];K=H if H==B[F][G]else C;E=E+(K,)
		D=D+(E,)
	return D
def val_func_vconcat(A,B):return A+B
def val_func_hconcat(A,B):return tuple(A+B for(A,B)in zip(A,B))
def val_func_vupscale(A,B):
	C=tuple()
	for D in A:C=C+tuple(D for A in range(B))
	return C
def val_func_hupscale(A,B):
	C=tuple()
	for E in A:
		D=tuple()
		for F in E:D=D+tuple(F for A in range(B))
		C=C+(D,)
	return C
def p(A):A=tuple(map(tuple,A));C=val_func_hupscale(A,3);D=val_func_vupscale(C,3);E=val_func_hconcat(A,A);B=val_func_hconcat(E,A);F=val_func_vconcat(B,B);G=val_func_vconcat(F,B);H=val_func_cellwise(D,G,0);return[*map(list,H)]