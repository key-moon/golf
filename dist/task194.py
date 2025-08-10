B=zip
A=lambda A:[[*i]for i in B(*A[::-1])]
p=lambda c:[a+b for(a,b)in B(c,A(c))]+[a+b for(a,b)in B(A(A(A(c))),A(A(c)))]