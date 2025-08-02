def val_func_rot180(A):return tuple(tuple(A[::-1])for A in A[::-1])
def p(A):A=tuple(map(tuple,A));B=val_func_rot180(A);return[*map(list,B)]