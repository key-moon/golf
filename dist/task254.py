A=zip
def p(g):a,*_,b=sorted({*A(*g)}-{(0,)*9},key=sum);return[*A(*[[v and(s==a)*2+(s==b)for v in s]for s in A(*g)])]