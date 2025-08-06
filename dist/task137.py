R=range
def p(g):
 h,w=len(g),len(g[0]);s=sum([[i,j]for i in R(h)for j in R(w)if g[i][j]],[]);return[[[g[i][j],g[s[0]][s[1]]][max(abs(i-s[2]),abs(j-s[3]))%(s[3]-s[1])==0]for j in R(w)]for i in R(h)]