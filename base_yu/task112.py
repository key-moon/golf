# best: 103(HIMAGINE THE FUTURE.) / others: 106(jacekw Potatoman nauti natte), 106(import itertools), 106(intgrah jimboko awu macaque sammyuri), 109(jailctf merger), 110(Code Golf International)
# ================================================ 103 ================================================

# p=lambda g,c=-1:c*g or p([*zip(*(g[:(i:=[i for i,s in enumerate(g)if 3in s][0])+1]+g[i::-1]+[g[-1]]*99)[:len(g)])],c+1)
# p=lambda g,c=-1:c*g or p([*zip(*(g[:(i:=g.index(max(g,key=max)))+1]+g[i::-1]+[g[-1]]*99)[:len(g)])],c+1)
p=lambda g,c=-1:c*g or p([*zip(*((a:=g[:g.index(max(g,key=max))+1])+a[::-1]+[g[-1]]*99)[:len(g)])],c+1)


# def p(g):
#  i=[i for i,s in enumerate(g)if 3in s][0]
#  print(g.index(max(g,key=max)))
#  print(i)
#  g=[*zip(*(g[:i+1]+g[i::-1]+[g[-1]]*99)[:len(g)])]
#  i=[i for i,s in enumerate(g)if 3in s][0]
#  g=[*zip(*(g[:i+1]+g[i::-1]+[g[-1]]*99)[:len(g)])]
#  return g
