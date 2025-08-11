def p(g):
 val_b=g[-1][-1];val_m=next(i for i,r in enumerate(g)if all(x==val_b for x in r));val_c=[];[val_c.append(x)for x in g[0][:val_m]if x not in val_c];return[[val_c[(i+j+1)%len(val_c)]for j in range(len(g[0]))]for i in range(len(g))]
