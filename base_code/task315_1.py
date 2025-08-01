def p(val_g):val_m=max(map(max,val_g));return[[val_g[val_i%3][val_j%3]if val_g[val_i//3][val_j//3]==val_m else 0 for val_j in range(9)]for val_i in range(9)]
