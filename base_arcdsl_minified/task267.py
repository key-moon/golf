def val_func_replace(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def val_func_leastcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def p(A):A=tuple(map(tuple,A));B=val_func_leastcolor(A);C=val_func_replace(A,B,0);D=val_func_leastcolor(C);E=val_func_replace(C,D,B);return[*map(list,E)]