# best: 79(luke, sisyphus) / others: 87(nauti), 93(kabutack), 96(joking+MWI), 96(MeWhenI), 99(MasukenSamba)
# ===================================== 79 ====================================
# p=lambda g:(u:=[[0]*i+[1]+[0]*(len(g[0])-i-1)for i in range(len(g[0]))])and((u+u[-2:0:-1])*9)[:len(g)][::-1]
# p=lambda g:(((u:=[[0]*i+[1]+[0]*(len(g[0])-i-1)for i in range(len(g[0]))])+u[-2:0:-1])*9)[:len(g)][::-1]
# p=lambda g:(((u:=[[0]*i+[1]+[0]*(len(g[0])-i-1)for i in range(len(g[0]))])+u[-2:0:-1])*9)[len(g)-1::-1]
p=lambda g:(((v:=[u:=[1]+[0]*~-len(g[0])]+[u:=[0]+u[:-1]for _ in u[1:]])+v[-2:0:-1])*9)[len(g)-1::-1]
