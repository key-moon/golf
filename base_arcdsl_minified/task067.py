def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_hsplit(A,B):D,C=len(A),len(A[0])//B;E=len(A[0])%B!=0;return tuple(val_func_crop(A,(0,C*B+B*E),(D,C))for B in range(B))
def val_func_first(A):return next(iter(A))
def p(A):A=tuple(map(tuple,A));B=val_func_hsplit(A,3);C=val_func_first(B);return[*map(list,C)]