def	p(j):
	A='[{"Ip3bl,2q]e"Op3swwwxxxxamg]]},{"Izch,2bhd]e"OzggAAyyyy]]},{"Izdh,2bk]e"OzgiyyyAAmg]]},{"Izcj,2lba]e"Ozggktxxxwwwwa]]}]';c='vvAp0zmiyqtxlswugvhiuaitrgsdbrakqo[pn[o":nhgmajlhckf3jddif0hccge[f],ebbdaac,3b,0a';c=[[c[i:i+2],c[i+2]]for	i	in	range(0,len(c),3)]
	for	E	in	c:A=A.replace(E[1],E[0])
	A=eval(A)
	for	k	in	A:
		if	k['I']==j:j=k['O'];return	j