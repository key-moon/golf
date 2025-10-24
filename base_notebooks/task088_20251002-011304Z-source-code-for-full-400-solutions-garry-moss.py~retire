from collections import*
q=len
g=range
def p(s):
 m=[g for g in s for g in g];n=Counter(m).most_common();n=[e for e in n if e[1]==4][0][0];o,p=q(s),q(s[0]);t=[]
 for m in g(o):
  for e in g(p):
   if s[m][e]==n:t.append([m,e])
 r=min([g[1]for g in t]);o=max([g[1]for g in t]);m=min([g[0]for g in t]);d=max([g[0]for g in t]);s=s[m+1:d];s=[g[r+1:o]for g in s];o,p=q(s),q(s[0])
 for m in g(o):
  for e in g(p):
   if s[m][e]>0:s[m][e]=n
 return s