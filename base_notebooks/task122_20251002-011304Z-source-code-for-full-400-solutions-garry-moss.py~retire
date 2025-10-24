def p(m,n=len,p=range):
 for i in p(n(m)):
  for a in p(n(m[0])):
   if m[i][a]==2:
    if m[i+1].count(3)>1:
     for n in p(3):
      for u in p(3):
       m[i+n][a+u+2]=m[i+n][a+u]
       if m[i+n][a+u]==2and u<2:m[i+n][a+u]=0
     return m
    else:
     for n in p(3):
      for u in p(3):
       m[i+n+2][a+u]=m[i+n][a+u]
       if m[i+n][a+u]==2and n<2:m[i+n][a+u]=0
     return m