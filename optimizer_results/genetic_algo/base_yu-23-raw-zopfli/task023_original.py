C=map
A=len
import re
def p(g):
 D='[[ ,]';B='.';g=[g[-1]]+g
 for _ in[0]*8:
  for _ in[0]*7:d=re.sub(D,'',str(g));d=re.sub(f"(?<=[^5]{B*(A(g[0])-2)}.[^5])555(?={B*(A(g[0])-2)}[^5])",'222',d);g=[[*C(int,c)]for c in d.split(']')[:-2]];*g,=C(list,zip(*g[::-1]))
  d=re.sub(D,'',str(g));d=re.sub(f"(?<=[^5]{B*(A(g[0])-2)}.[^5])55({B*(A(g[0])-2)}.)55(?=[^5]{B*(A(g[0])-2)}.[^5])",'88\g<1>88',d);g=[[*C(int,c)]for c in d.split(']')[:-2]]
 return g[1:]