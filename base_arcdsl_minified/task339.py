def val_func_remove(value,container):A=container;return type(A)(A for A in A if A!=value)
def val_func_first(container):return next(iter(container))
def val_func_canvas(value,dimensions):A=dimensions;return tuple(tuple(value for A in range(A[1]))for B in range(A[0]))
def val_func_palette(element):
	A=element
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_astuple(a,b):return a,b
def val_func_other(container,value):return val_func_first(val_func_remove(value,container))
def val_func_size(container):return len(container)
def p(I):I=tuple(map(tuple,I));B=val_func_palette(I);A=val_func_other(B,0);C=val_func_ofcolor(I,A);D=val_func_size(C);E=val_func_astuple(1,D);F=val_func_canvas(A,E);return[*map(list,F)]