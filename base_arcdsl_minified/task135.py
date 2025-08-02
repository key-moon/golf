def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_tojvec(A):return 0,A
def p(A):A=tuple(map(tuple,A));B=val_func_tojvec(6);C=val_func_crop(A,B,(3,3));return[*map(list,C)]