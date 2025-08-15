B=zip
A=lambda x:[[*i]for i in B(*x[::-1])]
p=lambda g:[a+b for(a,b)in B(g,A(g))]+[a+b for(a,b)in B(A(A(A(g))),A(A(g)))]