import re
A=re.sub
def p(g):
	d=A('[[ ,]','',str(g));n=[8]
	while'8'in d:
		d=A('8','1',d,1)
		for x in d:d=A('8(?=('+'.'*len(g[0])+')?1)','1',d)[::-1]
		n+=[0]
	return[(n:=[0,*n[:-1]])[1:]for x in n[:-1]]