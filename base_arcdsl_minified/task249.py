def val_func_hconcat(a,b):return tuple(A+B for(A,B)in zip(a,b))
def p(I):I=tuple(map(tuple,I));A=val_func_hconcat(I,I);return[*map(list,A)]