def val_func_rot270(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def p(A):A=tuple(map(tuple,A));B=val_func_rot270(A);return[*map(list,B)]