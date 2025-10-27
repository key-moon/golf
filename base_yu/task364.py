# best: 149(jailctf merger) / others: 155(ox jam), 156(HIMAGINE THE FUTURE.), 161(Code Golf International), 161(4atj sisyphus luke Seek mukundan), 171(import itertools)
# ======================================================================= 149 =======================================================================
# p=lambda g,c=-63:c*[[(v>>4).bit_count()%-8*5%9 for v in s]for s in g]or p([*zip(*[[v and v|[0,*s][j]|([[0]*99,*g][i][j]>0<[0,*s][j])<<c%4+4 for j,v in enumerate(s)]for i,s in enumerate(g)][::-1])],c+1)
# p=lambda g,c=-63:c*[[v.bit_count()**5*3%7 for v in s]for s in g]or p([[v and v|[0,*s][j]|([0,*g[j]][i]>0<[0,*s][j])<<c%4+2 for j,v in enumerate(s)]for i,s in enumerate(zip(*g))][::-1],c+1)
# p=lambda g,c=-63,E=enumerate:c*g or p([[v and[v.bit_count()%5^2,v|[0,*s][j]|([0,*g[j]][i]>0<[0,*s][j])<<c%4+2][c<0]for j,v in E(s)]for i,s in E(zip(*g))][::-1],c+1)
# p=lambda g,c=-63:c*g or p([(l:=0)or[[v.bit_count()%5^2,l|([0,*t][i]>0<l)<<c%4+2|v,l:=v][-(v<1)|(c<0)]for t,v in zip(g,s)]for i,s in enumerate(zip(*g))][::-1],c+1)
# p=lambda g,c=-63:c*g or p([(l:=0)or[l:=[v.bit_count()**5*3%7,v and l|([0,*t][i]>0<l)<<c%4+2|v][c<0]for t,v in zip(g,s)]for i,s in enumerate(zip(*g))][::-1],c+1)
p=lambda g,c=-63:c*g or p([(l:=0)or[l:=v and[v.bit_count()%5^2,l|v|([0,*t][i]>0<l)<<c%4+2][c<0]for t,v in zip(g,s)]for i,s in enumerate(zip(*g))][::-1],c+1)


# def p(g):
#  for c in range(64):
#   g=[*zip(*[[v and v|[0,*s][j]|([[0]*99,*g][i][j]>0<[0,*s][j])<<c%4+4 for j,v in enumerate(s)]for i,s in enumerate(g)][::-1])]
#  return [[(v>>4).bit_count()%-8*5%9 for v in s] for s in g]
