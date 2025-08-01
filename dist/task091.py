def p(g):
 F=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==5];G,C=zip(*F);D,E=min(G)-1,max(G)+1;D,max_r0=max(D,0),None;E,min_r1=min(E,len(g)-1),None;A,B=min(C),max(C)
 return[row[A:B+1]for row in g[D:E+1]]