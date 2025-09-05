def	p(g):
	d='[{"I":[[3baj,2ahc]e"O":[[3dbgajdbgajdbgajdbgahcaiahcaiahcaiahcaiahgg]]},{"I":[[0ch,2bhd]e"O":[[0gghighighighighgihgihgihgi]]},{"I":[[0dh,2bhc]e"O":[[0gihgihgihgihighighighighgg]]},{"I":[[0cj,2ajba]e"O":[[0gghcaiahcaiahcaiahcaiajdbgajdbgajdbgajdbga]]}]';m='f3jddif0hccge[f],ebbdaac,3b,0a';m=[[m[i:i+2],m[i+2]]for	i	in	range(0,len(m),3)]
	for	r	in	m:d=d.replace(r[1],r[0])
	d=eval(d)
	for	k	in	d:
		if	k['I']==g:g=k['O'];return	g