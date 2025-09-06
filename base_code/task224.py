# best: 171(xsot ovs att joking mewheni) / others: 178(4atj sisyphus luke Seek mukundan), 178(mukundan), 202(jailctf merger), 204(intgrah jimboko awu macaque sammyuri), 215(Jonas)
# ================================================================================== 171 ==================================================================================
def p(g):
 d,e=zip(*[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==5])
 k,={*sum(g,[])}-{0,5}
 a,b=min(d)+1,max(d)-1
 c,f=min(e)+1,max(e)-1
 for j in range(c,f+1):g[a][j]=g[b][j]=k
 for i in range(a,b+1):g[i][c]=g[i][f]=k
 return g
