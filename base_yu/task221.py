# best: 87(jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 89(4atj sisyphus luke Seek mukundan), 100(HashPanda Pooja), 100(HashPanda), 100(Rafael Pooja), 101(jacekw Potatoman nauti natte)
# ========================================= 87 ========================================
# p=lambda g:(c:=sum(g,[]).count(0))and[[((i//3)*c+(j//3)<9-c)*g[i%3][j%3]for j in range(3*c)]for i in range(3*c)]
# p=lambda g:(R:=range(c:=sum(g,[]).count(0)))and[[(i*c+j<9-c)*v for j in R for v in s]for i in R for s in g]
# p=lambda g:(c:=sum(g,[]).count(0),R:=range(3*c))and[[(i//3*c+j//3<9-c)*g[i%3][j%3]for j in R]for i in R]
# p=lambda g:(R:=range(c:=sum(g,[]).count(0)*3))and[[(i//3*c+j<27-c)*g[i%3][j%3]for j in R]for i in R]
def p(g):
 R=range(c:=str(g).count('0')*3)
 return[[(i//3*c+j<27-c)*g[i%3][j%3]for j in R]for i in R]
