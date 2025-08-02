def val_func_rot270(grid):return tuple(tuple(A[::-1])for A in zip(*grid[::-1]))[::-1]
def val_func_rot90(grid):return tuple(A for A in zip(*grid[::-1]))
def val_func_righthalf(grid):return val_func_rot270(val_func_bottomhalf(val_func_rot90(grid)))
def val_func_lefthalf(grid):return val_func_rot270(val_func_tophalf(val_func_rot90(grid)))
def val_func_bottomhalf(grid):A=grid;return A[len(A)//2+len(A)%2:]
def val_func_tophalf(grid):return grid[:len(grid)//2]
def val_func_astuple(a,b):return a,b
def val_func_leastcommon(container):A=container;return min(set(A),key=A.count)
def val_func_combine(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));A=val_func_lefthalf(I);B=val_func_righthalf(I);C=val_func_tophalf(A);D=val_func_tophalf(B);E=val_func_bottomhalf(A);F=val_func_bottomhalf(B);G=val_func_astuple(C,D);H=val_func_astuple(E,F);J=val_func_combine(G,H);K=val_func_leastcommon(J);return[*map(list,K)]