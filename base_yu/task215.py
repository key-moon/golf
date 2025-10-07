# best: 42(jailctf merger) / others: 44(intgrah jimboko awu macaque sammyuri), 45(ox jam), 46(4atj sisyphus luke Seek mukundan), 48(jacekw Potatoman nauti natte), 48(MasukenSamba)
# ================== 42 ==================
# p=lambda g:[[*map(max,zip(g[i%3+3],g[i%3+6]))]for i in range(len(g))]
# p=lambda g:[[g[i%3+6],g[i%3+3]][any(g[i%3+3])]for i in range(len(g))]
p=lambda g:[g[i%3+6-3*any(g[i%3+3])]for i in range(len(g))]
# p=lambda g:([g[i+6-3*any(g[i+3])]for i in range(3)]*9)[:len(g)]
# p=lambda g:[any(g[i%3+3])and g[i%3+3]or g[i%3+6]for i in range(len(g))]
# p=lambda g:[(u:=[*filter(any,g)])[(i-g.index(u[0]))%len(u)]for i in range(len(g))]
