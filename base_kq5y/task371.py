# best: 114(jailctf merger, xsot ovs att joking mewheni) / others: 115(4atj sisyphus luke Seek), 141(mukundan), 142(dbdr), 146(Yuchen20), 147(natte)
# ===================================================== 114 ======================================================

# c,B=zip(*((i,j)for i,r in A(j)for j,B in A(r)if B));Y=sum(c)//2;X=sum(B)//2

def p(j):
 Y,X=[sum(k)//2 for k in zip(*((i,k)for i,r in enumerate(j)for k,v in enumerate(r)if v))]
 for i in-1,0,1:j[Y+i][X]=j[Y][X+i]=3
 return j
