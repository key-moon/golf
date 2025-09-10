# best: 271(jailctf merger) / others: 277(4atj sisyphus luke Seek mukundan), 280(garrymoss), 288(jacekwl Potatoman nauti), 290(MasukenSamba), 290(cg)
# == begin zlib golf ==
def	p(l):
	v={(i,j)for	i	in	range(len(l))for	j	in	range(len(l[0]))if	l[i][j]&2};y=3
	while	1:
		c,k,i,j=max((sum((i+~-abs(q-1)*g,j+~-abs(q-2)*g)in	v	for	q	in	range(4)for	g	in	range(q>0,k)),-k,i,j)for	k	in	range(y,5)for	i	in	range(len(l))for	j	in	range(len(l[0])));y=-k
		if	c<1:return	l
		for	q	in	range(4):
			for	g	in	range(q>0,-k):
				if(i+~-abs(q-1)*g,j+~-abs(q-2)*g)in	v:v-={(i+~-abs(q-1)*g,j+~-abs(q-2)*g)}
				elif	len(l)>i+~-abs(q-1)*g>-1<j+~-abs(q-2)*g<len(l[0]):l[i+~-abs(q-1)*g][j+~-abs(q-2)*g]=8










