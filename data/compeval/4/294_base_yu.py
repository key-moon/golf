# best: 76(luke, mukundan, Seek64, joking, xsot, kg583) / others: 98(kabutack), 101(natte), 107(Bulmenisaurus), 136(nauti), 140(MeWhenI)
# =================================== 76 ===================================
# p=lambda g:[[(0<i<9>j>0and g[i-1][j]==g[i][j-1]==g[i+1][j]==g[i][j+1]>0)*2 or g[i][j] for j in range(10)]for i in range(10)]
# p=lambda g,R=range(10):[[(0<i<9>j>0and g[i-1][j]==g[i][j-1]==g[i+1][j]==g[i][j+1]>0)*2or g[i][j]for j in R]for i in R]
p=lambda g,R=range(10):[[(0<i<9>j>0and{g[i-1][j],g[i+1][j],*g[i][j-1:j+2]}=={5})*2or g[i][j]for j in R]for i in R]
