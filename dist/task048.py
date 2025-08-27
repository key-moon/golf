import re
A=re.sub
def p(g):
 d=A(*'21',A('[[ ,]','',str(g)),1)
 for x in d:d=A('[82](?=('+'.'*len(g[0])+')?1)','1',d)[::-1]
 return[[8-8*('2'in d)]]