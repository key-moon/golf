# best: 72(ShadowPrompt Labs) / others: 75(jacekw Potatoman nauti natte), 75(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 75(Code Golf International), 75(4atj sisyphus luke Seek mukundan), 75(HETHAT)
# ================================= 72 =================================
# R=range(10)
# p=lambda g:[[g[0][max(i,j)%(4+(g[0][4]>0))]for j in R]for i in R]


# lambda g,R=range(10):[[(a:=g[0])[max(i,j)%(5-0**a[4])]for j in R]for i in R]
p=lambda g,R=range(10):[[g[0][max(i,j)%(4+any(g[4]))]for j in R]for i in R]

# def p(g):
#  return[[g[0][max(i,j)%(4+(g[0][4]>0))] for j in range(10)]for i in range(10)]
