from collections import*
def p(r):
 n=[n for n in r for n in n];m=Counter(n).most_common(3);m=[m for m in m if m[0]>0][-1][0];r=[n for n in r if m in n];o=[]
 for n in r:
  for i in range(len(n)):
   if n[i]==m:o+=[i]
 return[n[min(o):max(o)+1]for n in r]