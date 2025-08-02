def val_func_rot270(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def val_func_rot90(A):return tuple(A for A in zip(*A[::-1]))
def val_func_righthalf(A):return val_func_rot270(val_func_bottomhalf(val_func_rot90(A)))
def val_func_lefthalf(A):return val_func_rot270(val_func_tophalf(val_func_rot90(A)))
def val_func_bottomhalf(A):return A[len(A)//2+len(A)%2:]
def val_func_tophalf(A):return A[:len(A)//2]
def val_func_astuple(A,B):return A,B
def val_func_leastcommon(A):return min(set(A),key=A.count)
def val_func_combine(A,B):return type(A)((*A,*B))
def p(A):A=tuple(map(tuple,A));B=val_func_lefthalf(A);C=val_func_righthalf(A);D=val_func_tophalf(B);E=val_func_tophalf(C);F=val_func_bottomhalf(B);G=val_func_bottomhalf(C);H=val_func_astuple(D,E);I=val_func_astuple(F,G);J=val_func_combine(H,I);K=val_func_leastcommon(J);return[*map(list,K)]