# best: 63(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, jailctf merger, intgrah jimboko awu macaque sammyuri, HETHAT, xsot ovs att joking mewheni) / others: 64(duckyluuk), 64(MasukenSamba), 64(kabutack), 64(biz), 64(mukundan)
# ============================= 63 ============================
# p=lambda g,R=range(9):[[(g[i//3][j//3]>1)*g[i%3][j%3]for j in R]for i in R]
# p=lambda g:[sum([[[0,0,0],s][v>1]for v in t],[])for t in g for s in g]
# lambda g:[[x//2*y for x in t for y in s]for t in g for s in g]
p=lambda g:[[y*(x>1)for x in t for y in s]for t in g for s in g]
# {
#   (0,0):0, (0,1):0, (0,2):0,
#   (1,0):0, (1,1):0, (1,2):0,
#   (2,0):0, (2,1):1, (2,2):2
# }[(x,y)]
