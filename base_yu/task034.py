# best: 125(4atj sisyphus luke Seek mukundan) / others: 156(jailctf merger), 164(ox jam), 164(xsot ovs att joking mewheni), 187(2F), 187(biz)
# =========================================================== 125 ===========================================================

def p(g):
 u=sum(g,[])
 Y,X=divmod(u.index(max(u,key=bool)),9)
 return[[sum({*u}-{2})*(v>0 or g[Y+(r>Y)][X+(c>X)]==2>min(abs(r-c-Y+X),abs(r+c-Y-X-1)))for c,v in enumerate(R)]for r,R in enumerate(g)]
