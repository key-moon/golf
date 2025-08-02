def val_func_canvas(value,dimensions):A=dimensions;return tuple(tuple(value for A in range(A[1]))for B in range(A[0]))
def val_func_mostcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def p(I):I=tuple(map(tuple,I));A=val_func_mostcolor(I);B=val_func_canvas(A,(3,3));return[*map(list,B)]