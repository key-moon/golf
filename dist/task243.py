import re
A=re.sub
def p(g):
	d=A('[[ ,]','',str(g))
	for x in d+d:d=A('0(?=('+'.'*len(g)+')?1)','1',d)[::-1]
	return[[*map(int,r)]for r in d.split(']')[:-2]]