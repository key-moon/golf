def p(a,i=len,r=range):
 f='r';m='r';e,f,x=i(a),i(a[0]),{}
 for s in r(e):
  for n in r(f):
   e=a[s][n]
   if e in x:x[e][f]+=[s];x[e][m]+=[n]
   else:x[e]={f:[s],m:[n]}
 r=sorted([[i(x[e][f])*(max(x[e][m])-min(x[e][m])),e]for e in x if e>0])[0][1];a=[[r if x==r else 0for x in x]for x in a];x=x[r];a=[f[min(x[m]):max(x[m])+1]for f in a];a=a[min(x[f]):max(x[f])+1];return a