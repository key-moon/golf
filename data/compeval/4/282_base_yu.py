# best: 89(att) / others: 115(joking+MWI), 115(joking), 117(dbdr), 121(Seek64), 122(ovs)
# ========================================== 89 =========================================
# p=lambda g,c=-3:c*g or p([[(c<0 or y!=5 or x!=1)and(y or [0,5,1][min(x,2)])for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
# p=lambda g,c=-3:c*g or p([[(c<0,y,x)!=(0,5,1)and(y or-x%6)for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
# p=lambda g,c=-3:c*g or p([[(not(0>c)<x<y)*((-x%6)|y)for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
# p=lambda g,c=-3:c*g or p([(x:=0)or[(not(0>c)<x<y)*((-x%6)|(x:=y))for y in s]for s in zip(*g[::-1])],c+1)
p=lambda g,c=-3,x=0:c*g or p([[(not(0>c)<x<y)*(-x%6|(x:=y))for y in s]for s in zip(*g[::-1])],c+1)
