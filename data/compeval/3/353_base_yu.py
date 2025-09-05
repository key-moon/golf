# best: 104(att, xsot ovs att) / others: 126(dbdr), 126(xsot ovs), 126(joking), 126(xsot), 126(joking MeWhenI)
# ================================================ 104 =================================================
# p=lambda g,c=-3:c*g or p([*zip(*([*filter(int,t:=[*map(max,g)])]<[4]and[g[k:=t.index(3)+1]]+g[:k]+g[k+1:]or g)[::-1])],c+1)
# p=lambda g,c=-3:c*g or p([*zip(*([g[k:=[*filter(int,t:=[*map(max,g)])]<[4]and-~t.index(3)]]+g[:k]+g[k+1:])[::-1])],c+1)
p=lambda g,c=-3:c*g or p([*zip(*[g.pop([*filter(int,t:=[*map(max,g)])]<[4]and-~t.index(3)),*g][::-1])],c+1)
# p=lambda g,c=-3:c*g or p([*zip(*((k:=((t:=[*map(max,g)])+[3]).index(3)+1)<t.index(4)and[g[k]]+g[:k]+g[k+1:]or g)[::-1])],c+1)
