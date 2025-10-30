# best: 86(import itertools, jailctf merger, Yuchen20) / others: 88(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 90(ox jam), 92(Code Golf International), 92(4atj sisyphus luke Seek mukundan), 93(intgrah jimboko awu macaque sammyuri)
# ======================================== 86 ========================================
p=lambda g:(((v:=[u:=[1]+[8]*~-len(g[0])]+[u:=[8]+u[:-1]for _ in u[1:]])+v[-2:0:-1])*9)[9::-1]

# p=lambda g:[[8-7*(i==5-abs(j-4))for i in range(len(g[0]))]for j in range(10)] これはダメだけどこんな感じで短くできるかも
