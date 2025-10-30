# best: 92(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger) / others: 104(ox jam), 107(HIMAGINE THE FUTURE.), 111(import itertools), 115(biz), 126(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# =========================================== 92 ===========================================
# p=lambda g,c=-3:c*g or p([*zip(*([*filter(int,t:=[*map(max,g)])]<[4]and[g[k:=t.index(3)+1]]+g[:k]+g[k+1:]or g)[::-1])],c+1)
# p=lambda g,c=-3:c*g or p([*zip(*([g[k:=[*filter(int,t:=[*map(max,g)])]<[4]and-~t.index(3)]]+g[:k]+g[k+1:])[::-1])],c+1)
p=lambda g,c=-3:c*g or p([*zip(*[g.pop([*filter(int,t:=[*map(max,g)])]<[4]and-~t.index(3)),*g][::-1])],c+1)
# p=lambda g,c=-3:c*g or p([*zip(*((k:=((t:=[*map(max,g)])+[3]).index(3)+1)<t.index(4)and[g[k]]+g[:k]+g[k+1:]or g)[::-1])],c+1)
