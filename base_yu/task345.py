# best: 89(ox jam) / others: 90(jailctf merger), 93(jacekw Potatoman nauti natte), 93(import itertools), 93(intgrah jimboko awu macaque sammyuri), 95(natte)
# ========================================== 89 =========================================
# def p(g):
#  u=[*zip(*g)]
# #  R=range(10)
# #  return [[u[j][i]|max(u[j][i:])%5|(5in(0,*u[j-1])[i:])*u[j-1][9]for j in R]for i in R]
#  return[[s[i]|max(s[i:])%5|(5in(0,*t)[i:])*t[9]for s,t in zip(u,u[:1]+u)]for i in range(10)]

# def p(g):
# #  u=[*zip(*g)]
# #  R=range(10)
# #  return [[u[j][i]|max(u[j][i:])%5|(5in(0,*u[j-1])[i:])*u[j-1][9]for j in R]for i in R]
#  t=[0]*10
#  return[*zip(*[t:=[s[i]|max(s[i:])%5|(5in(0,*t)[i:])*t[9]for i in range(10)]for s in zip(*g)])]


p=lambda g,t=[0]*10:[*zip(*[t:=[s[i]|max(s[i:])%5|(5in(0,*t)[i:])*t[9]for i in range(10)]for s in zip(*g)])]
