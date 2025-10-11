# best: 75(import itertools, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 77(cg-klogw-sekken), 82(cg-klogw), 84(4atj sisyphus luke Seek mukundan), 87(jacekwl Potatoman nauti), 87(jacekw Potatoman nauti natte)
# =================================== 75 ==================================
# lambda g,R=range(2,23):[[1+(r//c+c//r+g[0][0]-3)%~-len({*sum(g,[])})for c in R] for r in R]
# lambda g,R=range(2,23):[[1+(r//c+c//r+g[0][0]-3)%~-len({0,*g[0]})for c in R] for r in R] <- 隠れてる場合に死
# lambda g,R=range(2,23):[[1+(r//c+c//r+g[0][0]-3)%(len({*str(g)})-5)for c in R] for r in R]
# lambda g,R=range(2,23):[[1+(r//c+c//r+g[0][0]-3)%max(g[0]+g[1])for c in R] for r in R]
p=lambda g,R=range(2,23):[[1+(r//c+c//r+g[0][0]-3)%max(sum(g,[]))for c in R] for r in R]
