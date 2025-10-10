# best: 75(jacekw Potatoman nauti natte, 4atj sisyphus luke Seek mukundan, HETHAT, jacekw Potatoman nauti, cg-klogw-sekken, natte, import itertools, jailctf merger, Yuchen20, ox jam, intgrah jimboko awu macaque sammyuri) / others: 76(cg-klogw), 76(2F), 76(biz), 77(Tony Li), 80(JRKX)
# =================================== 75 ==================================
# R=range(10)
# p=lambda g:[[g[0][max(i,j)%(4+(g[0][4]>0))]for j in R]for i in R]


# lambda g,R=range(10):[[(a:=g[0])[max(i,j)%(5-0**a[4])]for j in R]for i in R]
p=lambda g,R=range(10):[[g[0][max(i,j)%(4+any(g[4]))]for j in R]for i in R]

# def p(g):
#  return[[g[0][max(i,j)%(4+(g[0][4]>0))] for j in range(10)]for i in range(10)]
