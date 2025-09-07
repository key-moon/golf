# best: 75(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, jailctf merger, natte) / others: 76(mukundan), 76(biz), 76(xsot ovs att joking mewheni), 77(intgrah jimboko awu macaque sammyuri), 80(dbdr)
# =================================== 75 ==================================
# R=range(10)
# p=lambda g:[[g[0][max(i,j)%(4+(g[0][4]>0))]for j in R]for i in R]


# lambda g,R=range(10):[[(a:=g[0])[max(i,j)%(5-0**a[4])]for j in R]for i in R]
p=lambda g,R=range(10):[[g[0][max(i,j)%(4+any(g[4]))]for j in R]for i in R]

# def p(g):
#  return[[g[0][max(i,j)%(4+(g[0][4]>0))] for j in range(10)]for i in range(10)]
