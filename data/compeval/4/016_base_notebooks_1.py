def p(g):
 m={1:5,2:6,3:4,4:3,5:1,6:2,8:9,9:8}
 return[[m.get(x,x)for x in r]for r in g]