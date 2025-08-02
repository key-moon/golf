def val_func_cellwise(a,b,fallback):
	F,G=len(a),len(a[0]);A=tuple()
	for C in range(F):
		B=tuple()
		for D in range(G):E=a[C][D];H=E if E==b[C][D]else fallback;B=B+(H,)
		A=A+(B,)
	return A
def val_func_vconcat(a,b):return a+b
def val_func_hconcat(a,b):return tuple(A+B for(A,B)in zip(a,b))
def val_func_vupscale(grid,factor):
	A=tuple()
	for B in grid:A=A+tuple(B for A in range(factor))
	return A
def val_func_hupscale(grid,factor):
	A=tuple()
	for C in grid:
		B=tuple()
		for D in C:B=B+tuple(D for A in range(factor))
		A=A+(B,)
	return A
def p(I):I=tuple(map(tuple,I));B=val_func_hupscale(I,3);C=val_func_vupscale(B,3);D=val_func_hconcat(I,I);A=val_func_hconcat(D,I);E=val_func_vconcat(A,A);F=val_func_vconcat(E,A);G=val_func_cellwise(C,F,0);return[*map(list,G)]