def val_func_canvas(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def val_func_mostcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def p(A):A=tuple(map(tuple,A));B=val_func_mostcolor(A);C=val_func_canvas(B,(3,3));return[*map(list,C)]