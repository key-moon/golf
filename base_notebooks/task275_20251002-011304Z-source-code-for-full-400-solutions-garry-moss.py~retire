def p(a):
 n=min(len(a),len(a[0]));r,a=[r[:n]for r in a[:n]],[r[-n:]for r in a[-n:]]
 if any(max(n)==8for n in r):r,a=a,r
 return[[r[l//n][b//n]*a[l%n][b%n]//8for b in range(n*n)]for l in range(n*n)]