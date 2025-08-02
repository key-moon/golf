def val_func_remove(A,B):return type(B)(B for B in B if B!=A)
def val_func_first(A):return next(iter(A))
def val_func_canvas(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_astuple(A,B):return A,B
def val_func_other(A,B):return val_func_first(val_func_remove(B,A))
def val_func_size(A):return len(A)
def p(A):A=tuple(map(tuple,A));C=val_func_palette(A);B=val_func_other(C,0);D=val_func_ofcolor(A,B);E=val_func_size(D);F=val_func_astuple(1,E);G=val_func_canvas(B,F);return[*map(list,G)]