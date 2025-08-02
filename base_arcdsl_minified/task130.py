def val_func_replace(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def val_func_downscale(A,B):
	E,I=len(A),len(A[0]);C=tuple()
	for D in range(E):
		F=tuple()
		for H in range(I):
			if H%B==0:F=F+(A[D][H],)
		C=C+(F,)
	E=len(C);G=tuple()
	for D in range(E):
		if D%B==0:G=G+(C[D],)
	return G
def p(A):A=tuple(map(tuple,A));B=val_func_replace(A,5,0);C=val_func_downscale(B,3);return[*map(list,C)]