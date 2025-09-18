def p(g):
    # find separator rows and cols
    val_sepR=[i for i,r in enumerate(g) if len(set(r))==1]
    val_sepC=[j for j in range(len(g[0])) if len({g[i][j] for i in range(len(g))})==1]
    val_rs=[0]+val_sepR+[len(g)]
    val_cs=[0]+val_sepC+[len(g[0])]
    # extract blocks
    val_B=[[ [row[val_cs[c]:val_cs[c+1]] 
               for row in g[val_rs[r]:val_rs[r+1]]] 
             for c in range(len(val_cs)-1)]
           for r in range(len(val_rs)-1)]
    # transpose block‐matrix
    val_BT=list(map(list,zip(*val_B)))
    # reassemble
    val_out=[]
    for rb in val_bt:
        for i in range(len(rb[0])):
            row=[]
            for cell in rb:
                row+=cell[i]
            val_out.append(row)
        # add separator row if any
        if val_rs[val_bt.index(rb)+1]<len(g):
            val_out.append(g[val_rs[val_bt.index(rb)+1]])
    return val_out
