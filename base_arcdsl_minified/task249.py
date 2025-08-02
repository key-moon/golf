def val_func_hconcat(A,B):return tuple(A+B for(A,B)in zip(A,B))
def p(A):A=tuple(map(tuple,A));B=val_func_hconcat(A,A);return[*map(list,B)]