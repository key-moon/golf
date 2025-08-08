A=range
p=lambda g,R=A(21):[[[u[i%d,j%d]for j in R]for i in R]for d in A(4,10)if len(u:=dict(m:=[((i%21%d,i//21%d),v)for(i,v)in enumerate(sum(g,[]))if v]))==len({*m})][0]