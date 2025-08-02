def val_func_switch(grid,a,b):return tuple(tuple(A if A!=a and A!=b else{a:b,b:a}[A]for A in A)for A in grid)
def val_func_replace(grid,val_func_replacee,val_func_replacer):return tuple(tuple(val_func_replacer if A==val_func_replacee else A for A in A)for A in grid)
def val_func_palette(element):
	A=element
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_last(container):return max(enumerate(container))[1]
def val_func_first(container):return next(iter(container))
def p(I):I=tuple(map(tuple,I));A=val_func_palette(I);B=val_func_first(A);C=val_func_last(A);D=val_func_switch(I,B,C);E=val_func_replace(D,5,0);return[*map(list,E)]