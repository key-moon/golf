# best: 138(import itertools, jailctf merger) / others: 145(HIMAGINE THE FUTURE.), 171(ox jam), 178(Code Golf International), 178(4atj sisyphus luke Seek mukundan), 189(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# ================================================================= 138 ==================================================================
# tmp
def	p(e):
	b,i=zip(*[(a,n)for(a,o)in	enumerate(e)for(n,j)in	enumerate(o)if	j==5]);g,={*sum(e,[])}-{0,5};f,m=min(b)+1,max(b)-1;r,d=min(i)+1,max(i)-1
	for	n	in	range(r,d+1):e[f][n]=e[m][n]=g
	for	a	in	range(f,m+1):e[a][r]=e[a][d]=g
	return	e
