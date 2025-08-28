import re;s=re.sub
def p(g):
 d=s(*"21",s("[[ ,]","",str(g)),1)
 for x in d:d=s("(8|2)(?=(.{%d})?1)"%len(g[0]),"1",d)[::-1]
 return[[8-8*("2"in d)]]