j=lambda A,c:sum(sum(A==c for A in A)for A in A)
def p(A):C=max(j([A],8)for A in A);B=(j(A,5)-C-2)/2-j(A,8)/C;return[[8*(B>0),8*(B>1),8*(B>2)],[0,0,8*(B>3)],[0,0,0]]