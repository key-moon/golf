import re
A=re.sub
def p(g):
	d=A('2','1',A('[[ ,]','',str(g)),1)
	for x in d:d=A('(8|2)(?=('+'.'*len(g[0])+')?1)','1',d)[::-1]
	return[[[8,0]['2'in d]]]