def p(g,a=3):
 l=len(g)//2
 for i in range(2-0**g[-2][l-1],l+1):g[-a][l-i]=g[-a][l+i]=g[-1][l];a+=1
 return g