def p(g):
 m=len(g[0]);L=2*m-2;a=-9%L
 for i in range(10):r=(i+a)%L;g[i]=[(r<m and r or 2*m-2-r)==j for j in range(m)]
 return g
