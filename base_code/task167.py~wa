def p(g):
 if len(set(sum(g,[])))<2:return[[5]*3]+[[0]*3]*2
 r=len({g[0][2],g[1][1],g[2][0]})>len({g[0][0],g[1][1],g[2][2]})
 return[[5 if j==(i,2-i)[r]else 0 for j in range(3)]for i in range(3)]
