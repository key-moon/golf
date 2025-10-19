# best: 171(ox jam) / others: 177(jailctf merger), 178(4atj sisyphus luke Seek mukundan), 178(Code Golf International), 193(jacekw Potatoman nauti natte), 193(import itertools)
# ================================================================================== 171 ==================================================================================
# tmp
def	p(e):
	b,i=zip(*[(a,n)for(a,o)in	enumerate(e)for(n,j)in	enumerate(o)if	j==5]);g,={*sum(e,[])}-{0,5};f,m=min(b)+1,max(b)-1;r,d=min(i)+1,max(i)-1
	for	n	in	range(r,d+1):e[f][n]=e[m][n]=g
	for	a	in	range(f,m+1):e[a][r]=e[a][d]=g
	return	e
