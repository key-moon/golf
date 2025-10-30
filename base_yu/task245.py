# best: 100(jailctf merger) / others: 101(ox jam), 106(Code Golf International), 106(4atj sisyphus luke Seek mukundan), 109(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 117(HIMAGINE THE FUTURE.)
# ============================================== 100 ===============================================
# p=lambda g,c=-7:c*g or p([*zip(*2in max(g,key=set)and[[y%3-9%~x for x,y in zip(*c)]for c in zip(g,[[0]*len(g[0])]+g)]or g)],c+1)
p=lambda g,c=-7:c*g or p([*zip(*[[y%3-9%~x for x,y in zip(*c)]for c in zip(g,[[0]*99]*(2in max(g,key=set))+g)])],c+1)

# def p(g):
#  for _ in range(8):
#   if 2in max(g,key=set):
# #    g=[[(x==3)*3+(y==2)*2 for x,y in zip(*c)] for c in zip(g,[[0]*len(g[0])]+g)]
#    g=[[y%3-9%~x for x,y in zip(*c)]for c in zip(g,[[0]*len(g[0])]+g)]
#   g=[*zip(*g)]
#  return g
