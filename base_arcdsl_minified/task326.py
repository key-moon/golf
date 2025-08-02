def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def p(A):A=tuple(map(tuple,A));B=val_func_crop(A,(0,0),(2,2));return[*map(list,B)]