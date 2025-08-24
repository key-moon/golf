# best: 79(luke) / others: 81(4atj), 84(sisyphus), 86(att), 88(duckyluuk), 89(ovs)
# ===================================== 79 ====================================
# p=lambda g,c=80:c and p([*map(list,zip(*(g[:1]+[[y or(x==1)for x,y in zip(s,t)]for s,t in zip(g,g[1:])])[::-1]))],c-1)or g
# p=lambda g,c=80:c and p([*map(list,zip(*[s[:1]+[y or(x==1)for x,y in zip(s,s[1:])]for s in g][::-1]))],c-1)or g
# p=lambda g,c=80:c and p([[s[0]]+[y or(x==1)for x,y in zip(s,s[1:])]for s in zip(*g[::-1])],c-1)or g
# p=lambda g,c=80:c and p([[y or(x==1)for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c-1)or g
p=lambda g,c=-79:c*g or p([[y or(x==1)for x,y in zip((0,)+s,s)]for s in zip(*g[::-1])],c+1)
