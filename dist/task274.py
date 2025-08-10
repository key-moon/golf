B=lambda A,c:sum(sum(i==c for i in r)for r in A)
def p(A):C=max(B([r],8)for r in A);k=(B(A,5)-C-2)/2-B(A,8)/C;return[[8*(k>0),8*(k>1),8*(k>2)],[0,0,8*(k>3)],[0,0,0]]