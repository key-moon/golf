A=enumerate
def p(j):
 B,C=[sum(k)//2for k in zip(*((i,k)for(i,r)in A(j)for(k,v)in A(r)if v))]
 for i in-1,0,1:j[B+i][C]=j[B][C+i]=3
 return j