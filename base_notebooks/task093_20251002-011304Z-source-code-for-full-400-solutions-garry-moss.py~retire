def p(n):
 a=0
 if n[0].count(5)==0:n=list(map(list,zip(*n[::-1])));a=3
 p=n[0].count(5);r=[e[:]for e in n];n=[[5if e==5else 0for e in e]for e in n];d=n[0].index(5)
 for e in range(len(n)):t=sum([1for e in r[e][:d]if e>0]);i=sum([1for e in r[e][d+p:]if e>0]);n[e]=n[e][:d-t]+[5]*(p+t+i)+n[e][d+p+i:]
 for r in range(a):n=list(map(list,zip(*n[::-1])))
 return n