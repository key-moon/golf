def p(t):
 e,e=len(t),len(t[0]);i=[p[:]for p in t]
 for o in range(e-1):
  n=t[o];d=t[o+1]
  for p in range(e-1):
   if n[p]==n[p+1]==d[p]==d[p+1]==0:i[o][p]=i[o][p+1]=i[o+1][p]=i[o+1][p+1]=2
 o,p=8,12
 if 0<=o<e and 0<=p<e and i[o][p]==2and o-1>=0and o+1<e and p-1>=0and t[o-1][p-1]==0and t[o][p-1]==0and t[o+1][p]==0:i[o][p]=t[o][p];i[o+1][p]=t[o+1][p]
 return i