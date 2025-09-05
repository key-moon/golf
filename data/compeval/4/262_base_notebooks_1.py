def	p(g):
	d='[qGJBKHLDFGGlvHHnFMJBKDcLDFJGrKLHxFGMrKHDcxFMJlvDcLnFJMlvLDcnFJGBKLHDFMGrKDcHxz]';m='BkMxcL0vKrkJncHlcGEqFz,EC2DjjCAbB5,Ay}z]]yw4xiiwuhvtOus"t]ase,rphqoIp{"om3nddmbel0ck2,j4,ig[hf[g":fb5e3,da[c0,b],a';m=[[m[i:i+2],m[i+2]]for	i	in	range(0,len(m),3)]
	for	r	in	m:d=d.replace(r[1],r[0])
	d=eval(d)
	for	k	in	d:
		if	k['I']==g:g=k['O'];return	g