import re
def p(g):
 d=re.sub('2','1',re.sub('[[ ,]','',str(g)),1)
 for x in d:d=re.sub('(8|2)(?=('+'.'*len(g[0])+')?1)','1',d)[::-1]
 return[[[8,0]['2'in d]]]