def val_func_rot270(grid):return tuple(tuple(A[::-1])for A in zip(*grid[::-1]))[::-1]
def val_func_rot90(grid):return tuple(A for A in zip(*grid[::-1]))
def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_rbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def val_func_order(container,compfunc):return tuple(sorted(container,key=compfunc))
def val_func_identity(x):return x
def p(I):I=tuple(map(tuple,I));A=val_func_rot270(I);B=val_func_rbind(val_func_order,val_func_identity);C=val_func_apply(B,A);D=val_func_rot90(C);return[*map(list,D)]