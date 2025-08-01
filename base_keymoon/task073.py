# Input:
# 0 0 0 0 0
# 0 0 0 0 0
# 0 1 0 1 0
# 0 5 0 5 0
# 5 5 5 5 5
# Output:
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 5 0 5 0
# 5 1 5 1 5
# def p(g):
#  for val_r in g[:-1]:
#   for val_x,val_v in enumerate(val_r):
#    if val_v==1:val_r[val_x]=0;g[-1][val_x]=1
#  return g
# 改善の余地ありそう（1を消し飛ばすところが雑
# p=lambda g:eval(str(g[:-1]).replace("1","0"))+[[next(filter(None,z))for z in zip(*g)]]
# p=lambda g:eval(f"{g[:-1]}".replace("1","0"))+[[next(filter(None,z))for z in zip(*g)]]
p=lambda g:[*eval(f"{g[:-1]}".replace("1","0")),[next(filter(None,z))for z in zip(*g)]]
