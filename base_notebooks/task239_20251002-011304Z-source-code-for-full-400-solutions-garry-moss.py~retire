from collections import*
def p(s,b=range):
 m=Counter([r for r in s for r in r]).most_common(9);q,o=m[0][1],len(m);s=[[0for r in b(o)]for r in b(q)]
 for d in b(o):
  for r in b(m[d][1]):s[r][d]=m[d][0]
 return s