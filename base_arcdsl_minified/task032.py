def val_func_rot270(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def val_func_rot90(A):return tuple(A for A in zip(*A[::-1]))
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_order(A,B):return tuple(sorted(A,key=B))
def val_func_identity(A):return A
def p(A):A=tuple(map(tuple,A));B=val_func_rot270(A);C=val_func_rbind(val_func_order,val_func_identity);D=val_func_apply(C,B);E=val_func_rot90(D);return[*map(list,E)]