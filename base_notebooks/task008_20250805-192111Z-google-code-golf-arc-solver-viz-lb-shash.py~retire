def p(g,R=enumerate):
 a,b=[(i,j)for i,r in R(g)for j,v in R(r)if v==2],[(i,j)for i,r in R(g)for j,v in R(r)if v==8]
 if not a or not b:return g
 f=lambda s:(min(i for i,_ in s),max(i for i,_ in s),min(j for _,j in s),max(j for _,j in s))
 L,E,D,C=f(a);A,I,V,x=f(b);U=G=0
 if C<V:G=V-C-1
 elif x<D:G=x-D+1
 elif E<A:U=A-E-1
 elif I<L:U=I-L+1
 u,B={*a},{*b}
 return[[8 if(i,j)in B else 2 if(i-U,j-G)in u else 0 for j,_ in R(g[0])]for i,_ in R(g)]