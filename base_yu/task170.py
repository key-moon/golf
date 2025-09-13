# best: 196(jailctf merger) / others: 211(4atj sisyphus luke Seek mukundan), 238(xsot ovs att joking mewheni), 312(jacekwl), 312(jacekw), 312(jacekwl Potatoman nauti)
# ============================================================================================== 196 ===============================================================================================
def p(g):
 yy,xx,cc=zip(*[(i,j,v)for i,s in enumerate(g)for j,v in enumerate(s)if v])
 d=3+(len({*cc[:-9]})>1)
 k=-d*d
 l=(yy[k-1]-yy[0]+1)//d
 return[[g[i*l+yy[0]][j*l+min(xx[:k])]and g[yy[k]+i][xx[k]+j] for j in range(d)]for i in range(d)]
