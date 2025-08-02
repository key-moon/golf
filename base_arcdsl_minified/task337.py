def val_func_switch(A,B,C):return tuple(tuple(A if A!=B and A!=C else{B:C,C:B}[A]for A in A)for A in A)
def p(A):A=tuple(map(tuple,A));B=val_func_switch(A,5,8);return[*map(list,B)]