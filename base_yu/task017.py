p=lambda g,R=range(21):[[[u[(i%d,j%d)]for j in R]for i in R]for d in range(4,10)if len(u:=dict(m:=[((i%21%d,i//21%d),v)for i,v in enumerate(sum(g,[]))if v]))==len({*m})][0]

# def p(g):
#  for d in range(4,10):
#   if len(u:=dict(m:=[((i%21%d,i//21%d),v) for i,v in enumerate(sum(g,[]))if v]))==len({*m}):
#    return [[u[(i%d,j%d)]for j in range(21)]for i in range(21)]
