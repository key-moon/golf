# best: 75(natte, ox jam, 4atj sisyphus luke Seek mukundan, jailctf merger, intgrah jimboko awu macaque sammyuri, Yuchen20, HETHAT, xsot ovs att joking mewheni) / others: 76(2F), 76(biz), 76(cg-klogw), 77(jacekw Potatoman nauti), 80(JRKX)
# =================================== 75 ==================================
# R=range(10)
# p=lambda g:[[g[0][max(i,j)%(4+(g[0][4]>0))]for j in R]for i in R]


# lambda g,R=range(10):[[(a:=g[0])[max(i,j)%(5-0**a[4])]for j in R]for i in R]
p=lambda g,R=range(10):[[g[0][max(i,j)%(4+any(g[4]))]for j in R]for i in R]

# def p(g):
#  return[[g[0][max(i,j)%(4+(g[0][4]>0))] for j in range(10)]for i in range(10)]
