B=filter
A=zip
def p(g):*g,=map(list,A(*g));k=sum(g,[]).index(4);l=g[k//13][k%13+1:].index(4)+2;a=g[k//13][k%13:k%13+l];g[k//13][k%13:k%13+l]=[0]*l;k=sum(g,[]).index(4);l=g[k//13][k%13+1:].index(4)+2;b=g[k//13][k%13:k%13+l];g[k//13][k%13:k%13+l]=[0]*l;*g,=B(any,A(*g));*g,=B(any,A(*g));return[*A(a,*[[0,*s,0]for s in g][::1|-(max(g[0])!=a[1])],b)]