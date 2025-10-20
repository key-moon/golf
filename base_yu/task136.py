# best: 105(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger) / others: 107(jacekw Potatoman nauti natte), 107(import itertools), 107(ox jam), 113(THUNDER THUNDER), 116(biz)
# 131
# def p(g,R=range):
#  for _ in R(10):
#   for i in R(1,9):
#    for j in R(1,9):
#     b=g[i][j]
#     a=-~b%3-1
#     g[i-a][j-a]|=b&g[i+a][j+a]
#  return g
# 125
# def p(g,R=range):
#  for _ in R(10):
#   for x in R(64):
#    i,j=x//8+1,x%8+1;b=g[i][j]
#    a=b**b+~b
#    g[i+a][j+a]|=b&g[i-a][j-a]
#  return g
# ================================================= 105 =================================================
# lambda g:exec("for x in range(64):\n i,j=x//8+1,x%8+1;a=-~g[i][j]%3-1;g[i-a][j-a]|=g[i][j]&g[i+a][j+a]\n"*9)or g
# lambda g:exec("x=%d;i,j=x//8+1,-~x&7;a=-~g[i][j]%%3-1;g[i-a][j-a]|=g[i][j]&g[i+a][j+a];"*64%(*range(64),)*9)or g
# lambda g,R=range(1,9):exec("for i in R:\n for j in R:a=-~g[i][j]%3-1;g[i-a][j-a]|=g[i][j]&g[i+a][j+a]\n"*9)or g
p=lambda g,R=range(1,9):exec("for j in R:i=%s;b=g[i][j];a=b**b+~b;g[i+a][j+a]|=b&g[i-a][j-a]\n"*8%(*R,)*9)or g
