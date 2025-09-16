A=enumerate
p=lambda g,c=-63:c*[[v.bit_count()**5*3%7for v in s]for s in g]or p([[v and v|[0,*s][j]|([0,*g[j]][i]>0<[0,*s][j])<<c%4+2for(j,v)in A(s)]for(i,s)in A(zip(*g))][::-1],c+1)