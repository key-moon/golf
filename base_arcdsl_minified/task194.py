def val_func_vconcat(A,B):return A+B
def val_func_hconcat(A,B):return tuple(A+B for(A,B)in zip(A,B))
def val_func_rot270(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def val_func_rot180(A):return tuple(tuple(A[::-1])for A in A[::-1])
def val_func_rot90(A):return tuple(A for A in zip(*A[::-1]))
def p(A):A=tuple(map(tuple,A));B=val_func_rot90(A);C=val_func_rot180(A);D=val_func_rot270(A);E=val_func_hconcat(A,B);F=val_func_hconcat(D,C);G=val_func_vconcat(E,F);return[*map(list,G)]