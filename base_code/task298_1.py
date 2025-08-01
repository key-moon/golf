def p(val_g):val_b=sum(val_g,[]);val_u=sorted({*val_b},key=val_b.count,reverse=1);return[[val_u[(val_u.index(val_x)+2)%3]for val_x in val_r]for val_r in val_g]
