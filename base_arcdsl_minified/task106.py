def val_func_vconcat(a,b):return a+b
def val_func_hconcat(a,b):return tuple(A+B for(A,B)in zip(a,b))
def val_func_rot270(grid):return tuple(tuple(A[::-1])for A in zip(*grid[::-1]))[::-1]
def val_func_rot180(grid):return tuple(tuple(A[::-1])for A in grid[::-1])
def val_func_rot90(grid):return tuple(A for A in zip(*grid[::-1]))
def p(I):I=tuple(map(tuple,I));A=val_func_rot90(I);B=val_func_rot180(I);C=val_func_rot270(I);D=val_func_hconcat(I,A);E=val_func_hconcat(C,B);F=val_func_vconcat(D,E);return[*map(list,F)]