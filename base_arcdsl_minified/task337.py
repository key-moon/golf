def val_func_switch(grid,a,b):return tuple(tuple(A if A!=a and A!=b else{a:b,b:a}[A]for A in A)for A in grid)
def p(I):I=tuple(map(tuple,I));A=val_func_switch(I,5,8);return[*map(list,A)]