# best: 146(4atj sisyphus luke Seek) / others: 148(mukundan), 161(jailctf merger), 178(xsot ovs att joking mewheni), 234(MasukenSamba), 236(duckyluuk)
# ===================================================================== 146 ======================================================================

def p(g):
 u=sum(g,[])
 Y,X=divmod(u.index(max(u,key=bool)),9)
 return[[sum({*u}-{2})*(v>0 or g[Y+(r>Y)][X+(c>X)]==2>min(abs(r-c-Y+X),abs(r+c-Y-X-1)))for c,v in enumerate(R)]for r,R in enumerate(g)]
