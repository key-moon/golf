# best: 93(ox jam) / others: 96(Code Golf International), 98(jailctf merger), 108(lv1.dev), 108(LogicLynx), 108(ALE-Agent)
# ============================================ 93 ===========================================
# lambda g,E=enumerate:[[v*(1<str([(),*zip(*[[0]*99,*g][i:i+3])][j:j+3]).count(str(v)))for j,v in E(r)]for i,r in E(g)]
p=lambda g,E=enumerate:[[v*(v<sum(sum([(),*zip(*[[0]*99,*g][i:i+3])][j:j+3],())))for j,v in E(r)]for i,r in E(g)]
