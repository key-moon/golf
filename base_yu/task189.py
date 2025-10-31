# best: 95(Code Golf International) / others: 111(LogicLynx), 111(FuunAgent), 111(jailctf merger), 111(ox jam), 112(lv1.dev)
# ============================================= 95 ============================================

p=lambda g,R=range(6):[[g[i+(y:=g[2][0]>7)*3][j+(x:=g[0][2]>7)*3]and g[i//3+7-y*7][j//3+7-x*7]for j in R]for i in R]

# def p(g,R=range(6)):
#  x=g[0][2]>7
#  y=g[2][0]>7
#  return[[g[i+y*3][j+x*3]and g[i//3+7-y*7][j//3+7-x*7]for j in R]for i in R]
