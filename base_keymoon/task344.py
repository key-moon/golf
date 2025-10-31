# best: 74(ox jam) / others: 77(Code Golf International), 77(lv1.dev), 77(LogicLynx), 77(jailctf merger), 78(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# ================================== 74 ==================================
# p=lambda g,c=4:c and p([[y or(x==1)for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c-1)or g
# import re;p=lambda g,c=4:c and p([*zip(*eval(re.sub("3, 2","8,0",str(g)))[::-1])],c-1)or g
p=lambda g,c=-3:c*g or[*zip(*eval(str(p(g,c+1)).replace("3, 2","8,0"))[::-1])]
