# best: 196(jailctf merger) / others: 202(jacekw Potatoman nauti), 202(jacekwl Potatoman nauti), 211(4atj sisyphus luke Seek mukundan), 213(ox jam), 213(xsot ovs att joking mewheni)
# ============================================================================================== 196 ===============================================================================================
def p(g):
 y,x,c=zip(*[(i,j,v)for i,s in enumerate(g)for j,v in enumerate(s)if v])
 d=3+1%len({*c[:-9]})
 R=range(d)
 k=-d*d
 l=(y[k-1]-y[0]+1)//d
 return[[g[i*l+y[0]][j*l+min(x[:k])]and g[y[k]+i][x[k]+j]for j in R]for i in R]
