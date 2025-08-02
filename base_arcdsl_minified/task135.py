def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_tojvec(j):return 0,j
def p(I):I=tuple(map(tuple,I));A=val_func_tojvec(6);B=val_func_crop(I,A,(3,3));return[*map(list,B)]