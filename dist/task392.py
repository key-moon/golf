C=range
B=max
p=lambda g:min((o:=0,[[(v:=(B(abs(i*2+1-A//18%21),abs(j*2+1-A//378%21))%(A%3+4)==A//3%6)*B(B(g)),o:=o+(v<g[i][j])*999+v)[0]or 5for j in C(10)]for i in C(10)],o)[::-1]for A in C(7938))[1]