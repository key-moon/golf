# best: 89(mukundan) / others: 116(joking+MWI), 119(joking), 120(ovs), 120(biz), 159(nauti)
# ========================================== 89 =========================================
# p=lambda g:[([0]*g[9].index(c:=max(g[9]))+[c,0,c,5,c,0][(i<1)*2:][:4-2*(0<i<9)]*9)[:10]for i in range(10)]
# p=lambda g:[([0]*g[9].index(c:=max(g[9]))+[c,5,c,0,c,0,c,5][((i>0)+(i>8))*2:][:4]*9)[:10]for i in range(10)]
# p=lambda g,R=range(10):[([0]*g[9].index(c:=max(g[9]))+[[c,((i<j%4<2)+(i==j%4*3>8))*5][j%2] for j in R])[:10]for i in R]

# p=lambda g:[([0]*g[9].index(c:=max(g[9]))+[c,(i<1)*5,c,(i>8)*5]*9)[:10]for i in range(10)]
p=lambda g:[([0]*g[9].index(c:=max(g[9]))+[c,0**i*5,c,(i>8)*5]*9)[:10]for i in range(10)]


# i==0 2:6
# 0<i<9 0:2
# i==9 0:4
