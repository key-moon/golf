def p(g):
 val_d=3
 val_P=[(i//val_d,j//val_d)for i in range(len(g))for j in range(len(g[0]))if g[i][j]==5]
 val_r0=min(x for x,_ in val_P)*val_d;val_c0=min(y for _,y in val_P)*val_d
 val_S=[[sum(g[val_r0+val_d*i+ii][val_c0+val_d*j+jj]==5
             for ii in range(val_d)for jj in range(val_d))>0
         for j in range(3)]for i in range(3)]
 return[[5 if val_S[i//val_d][j//val_d]else 0
         for j in range(val_d*3)]for i in range(val_d*3)]
