# best: 63(jacekw Potatoman nauti natte, 4atj sisyphus luke Seek mukundan, HETHAT, natte, import itertools, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 64(JRKX), 64(jacekw Potatoman nauti), 64(cg-klogw-sekken), 64(kabutack), 64(JRKXK)
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
