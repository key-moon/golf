def val_func_replace(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def p(A):A=tuple(map(tuple,A));B=val_func_replace(A,6,2);return[*map(list,B)]