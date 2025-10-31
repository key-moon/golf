# best: 81(LogicLynx) / others: 84(Code Golf International), 85(lv1.dev), 85(ALE-Agent), 85(FuunAgent), 86(import itertools)
# ====================================== 81 =====================================
p=lambda g:(((v:=[u:=[1]+[8]*~-len(g[0])]+[u:=[8]+u[:-1]for _ in u[1:]])+v[-2:0:-1])*9)[9::-1]

# p=lambda g:[[8-7*(i==5-abs(j-4))for i in range(len(g[0]))]for j in range(10)] これはダメだけどこんな感じで短くできるかも
