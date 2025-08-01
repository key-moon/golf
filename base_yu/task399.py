# 1の2x2の数を数えて配置しなおす x,yは[0,0,1,2,2],[0,2,1,0,2]
def p(g):
 *r,=eval("[0]*3,"*3)
 for i in range(sum(sum(g,[]))//8):
  r[int(.7*i)][i*2%3]=1
 return r