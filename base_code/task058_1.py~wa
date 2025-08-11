def p(g):val_r,val_c=len(g),len(g[0]);val_d=[(0,1),(1,0),(0,-1),(-1,0)];val_i=val_j=val_t=0; 
 while 1:g[val_i][val_j]=3;val_di,val_dj=val_d[val_t];val_ni,val_nj=val_i+val_di,val_j+val_dj; 
 if 0<=val_ni<val_r and 0<=val_nj<val_c and g[val_ni][val_nj]==0:val_i,val_j=val_ni,val_nj;continue 
 val_t=(val_t+1)&3;val_di,val_dj=val_d[val_t];val_ni,val_nj=val_i+val_di,val_j+val_dj 
 if 0<=val_ni<val_r and 0<=val_nj<val_c and g[val_ni][val_nj]==0:val_i,val_j=val_ni,val_nj;continue 
 break 
 return g
