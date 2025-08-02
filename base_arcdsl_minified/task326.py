def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def p(I):I=tuple(map(tuple,I));A=val_func_crop(I,(0,0),(2,2));return[*map(list,A)]