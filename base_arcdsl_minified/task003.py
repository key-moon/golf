def val_func_bottomhalf(A):return A[len(A)//2+len(A)%2:]
def val_func_tophalf(A):return A[:len(A)//2]
def val_func_replace(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def val_func_vconcat(A,B):return A+B
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_branch(A,B,C):return B if A else C
def val_func_equality(A,B):return A==B
def p(A):A=tuple(map(tuple,A));C=val_func_tophalf(A);B=val_func_bottomhalf(A);D=val_func_equality(C,B);E=val_func_crop(A,(2,0),(3,3));F=val_func_branch(D,B,E);G=val_func_vconcat(A,F);H=val_func_replace(G,1,2);return[*map(list,H)]