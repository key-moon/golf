def p(g):
 a=sum(g,[]);w=len(g[0]);s=[i for i,x in enumerate(a)if x]
 f,F=s[0]//w,s[-1]//w;h=min(i%w for i in s);H=max(i%w for i in s)
 m,d=sorted({*a}-{0,8},key=a.count);q=[d]+[m]*(H-h-1)+[d]
 for i in range(f,F+1):g[i][h:H+1]=(q,[d]*len(q))[i in(f,F)]
 return g