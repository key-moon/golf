def val_func_bottomhalf(grid):A=grid;return A[len(A)//2+len(A)%2:]
def val_func_tophalf(grid):return grid[:len(grid)//2]
def val_func_replace(grid,val_func_replacee,val_func_replacer):return tuple(tuple(val_func_replacer if A==val_func_replacee else A for A in A)for A in grid)
def val_func_vconcat(a,b):return a+b
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_branch(condition,a,b):return a if condition else b
def val_func_equality(a,b):return a==b
def p(I):I=tuple(map(tuple,I));B=val_func_tophalf(I);A=val_func_bottomhalf(I);C=val_func_equality(B,A);D=val_func_crop(I,(2,0),(3,3));E=val_func_branch(C,A,D);F=val_func_vconcat(I,E);G=val_func_replace(F,1,2);return[*map(list,G)]