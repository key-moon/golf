# best: 155(xsot ovs att joking mewheni) / others: 161(4atj sisyphus luke Seek mukundan), 166(jailctf merger), 233(kdmitrie), 286(jacekwl Potatoman nauti), 294(Yuchen20)
# ========================================================================== 155 ==========================================================================
# p=lambda g,c=-63:c*[[(v>>4).bit_count()%-8*5%9 for v in s]for s in g]or p([*zip(*[[v and v|[0,*s][j]|([[0]*99,*g][i][j]>0<[0,*s][j])<<c%4+4 for j,v in enumerate(s)]for i,s in enumerate(g)][::-1])],c+1)
p=lambda g,c=-63:c*[[v.bit_count()**5*3%7 for v in s]for s in g]or p([[v and v|[0,*s][j]|([0,*g[j]][i]>0<[0,*s][j])<<c%4+2 for j,v in enumerate(s)]for i,s in enumerate(zip(*g))][::-1],c+1)


# def p(g):
#  for c in range(64):
#   g=[*zip(*[[v and v|[0,*s][j]|([[0]*99,*g][i][j]>0<[0,*s][j])<<c%4+4 for j,v in enumerate(s)]for i,s in enumerate(g)][::-1])]
#  return [[(v>>4).bit_count()%-8*5%9 for v in s] for s in g]
