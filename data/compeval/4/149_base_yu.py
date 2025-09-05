# best: 77(luke, luke/sisyphus/Seek) / others: 80(natte), 81(mukundan), 81(sisyphus), 82(joking+MWI), 82(joking/MWI)
# ==================================== 77 ===================================

# p=lambda g,R=range(3):[[sum(sum(g[i*4+k][j*4:j*4+3])for k in R)//12for j in R]for i in R]
# p=lambda g,R=(0,4,8):[[sum(sum(g[i+k][j:j+3])for k in(0,1,2))//12for j in R]for i in R]
# p=lambda g,R=(0,4,8):[[sum(sum(s[j:j+3])for s in g[i:i+3])//12for j in R]for i in R]
# p=lambda g,R=(0,4,8):[[sum(g[i][j:j+3]+g[i+1][j:j+3]+g[i+2][j:j+3])//12for j in R]for i in R]
p=lambda g,R=b"":[[sum(sum(s[j-3:j])for s in g[i-3:i])//12for j in R]for i in R]

# def p(g):
#  u=[*eval("[0]*3,"*3)]
#  for i in range(11):
#   for j in range(11):
#    u[i//4][j//4]+=g[i][j]==6
#  return[[v//2 for v in s]for s in u]
