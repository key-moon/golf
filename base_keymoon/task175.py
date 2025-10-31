# best: 74(Code Golf International) / others: 75(Team JYCDT), 75(lv1.dev), 75(LogicLynx), 75(FuunAgent), 75(import itertools)
# ================================== 74 ==================================
# lambda g,R=range(2,23):[[1+(r//c+c//r+g[0][0]-3)%~-len({*sum(g,[])})for c in R] for r in R]
# lambda g,R=range(2,23):[[1+(r//c+c//r+g[0][0]-3)%~-len({0,*g[0]})for c in R] for r in R] <- 隠れてる場合に死
# lambda g,R=range(2,23):[[1+(r//c+c//r+g[0][0]-3)%(len({*str(g)})-5)for c in R] for r in R]
# lambda g,R=range(2,23):[[1+(r//c+c//r+g[0][0]-3)%max(g[0]+g[1])for c in R] for r in R]
p=lambda g,R=range(2,23):[[1+(r//c+c//r+g[0][0]-3)%max(sum(g,[]))for c in R] for r in R]
