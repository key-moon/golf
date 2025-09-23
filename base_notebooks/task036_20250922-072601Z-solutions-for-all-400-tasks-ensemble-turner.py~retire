def p(d,i=len,r=range):
	l='r';m='r';e,l,x=i(d),i(d[0]),{}
	for a in r(e):
		for z in r(l):
			e=d[a][z]
			if e in x:x[e][l]+=[a];x[e][m]+=[z]
			else:x[e]={l:[a],m:[z]}
	r=sorted([[i(x[e][l])*(max(x[e][m])-min(x[e][m])),e]for e in x if e>0])[0][1];d=[[r if x==r else 0 for x in x]for x in d];x=x[r];d=[l[min(x[m]):max(x[m])+1]for l in d];d=d[min(x[l]):max(x[l])+1];return d