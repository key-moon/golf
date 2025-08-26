A=zip
def p(g):_,a,*_,b=sorted({*A(*g)});return[*A(*[[v and(s==a)*2+(s==b)for v in s]for s in A(*g)])]