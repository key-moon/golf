def val_func_switch(A,B,C):return tuple(tuple(A if A!=B and A!=C else{B:C,C:B}[A]for A in A)for A in A)
def val_func_replace(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_last(A):return max(enumerate(A))[1]
def val_func_first(A):return next(iter(A))
def p(A):A=tuple(map(tuple,A));B=val_func_palette(A);C=val_func_first(B);D=val_func_last(B);E=val_func_switch(A,C,D);F=val_func_replace(E,5,0);return[*map(list,F)]