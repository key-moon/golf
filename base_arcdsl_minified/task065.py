def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_palette(element):
	A=element
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_vsplit(grid,n):A=grid;B,D=len(A)//n,len(A[0]);E=len(A)%n!=0;return tuple(val_func_crop(A,(B*C+C*E,0),(B,D))for C in range(n))
def val_func_hsplit(grid,n):A=grid;D,B=len(A),len(A[0])//n;E=len(A[0])%n!=0;return tuple(val_func_crop(A,(0,B*C+C*E),(D,B))for C in range(n))
def val_func_numcolors(element):return len(val_func_palette(element))
def mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_rbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def val_func_argmax(container,compfunc):return max(container,key=compfunc)
def p(I):I=tuple(map(tuple,I));A=val_func_vsplit(I,2);B=val_func_rbind(val_func_hsplit,2);C=mval_func_apply(B,A);D=val_func_argmax(C,val_func_numcolors);return[*map(list,D)]