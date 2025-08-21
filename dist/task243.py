import re;s=re.sub
def p(g):
 d=s("[[,]","",str(g))
 for x in d+d:d=s("0(?=("+"."*len(g)+")?1)","1",d)[::-1]
 return[[*map(int,r)]for r in d.split("]")[:-2]]