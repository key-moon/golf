# best: 75(xsot ovs att joking mewheni, jailctf merger) / others: 87(jacekw), 87(jacekwl), 92(4atj sisyphus luke Seek), 95(natte), 97(MasukenSamba)
# =================================== 75 ==================================
# lambda g,R=range(2,23):[[1+(r//c+c//r+g[0][0]-3)%~-len({*sum(g,[])})for c in R] for r in R]
# lambda g,R=range(2,23):[[1+(r//c+c//r+g[0][0]-3)%~-len({0,*g[0]})for c in R] for r in R] <- 隠れてる場合に死
# lambda g,R=range(2,23):[[1+(r//c+c//r+g[0][0]-3)%(len({*str(g)})-5)for c in R] for r in R]
# lambda g,R=range(2,23):[[1+(r//c+c//r+g[0][0]-3)%max(sum(g,[]))for c in R] for r in R]
# lambda g,R=range(2,23):[[1+(r//c+c//r+g[0][0]-3)%max(g[0]+g[1])for c in R] for r in R]
p=lambda g,R=range(2,23):[[1+(r//c+c//r+g[0][0]-3)%max(g[0])for c in R] for r in R]
