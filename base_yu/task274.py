# best: 71(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 75(xsot ovs att joking mewheni), 77(natte), 77(kabutack), 79(MasukenSamba), 79(Yuchen20)
# ================================= 71 ================================
# p=lambda g:(a:=[*filter(int,map(sum,zip(*g)))],c:=[8]*(a[0]//5-(a[1]+3)//8)+[0]*9)and[c[:3],c[5:2:-1],c[6:9]]
# p=lambda g:(a:=[*({s.count(0)for s in zip(*g)}-{len(g)})],c:=[8]*abs(a[0]-a[1])+[0]*9)and[c[:3],c[5:2:-1],c[6:9]]
# p=lambda g:(c:=[8]*(len([*filter(lambda s:5 in s and 8 not in s,g)])-1)+[0]*9)and[c[:3],c[5:2:-1],c[6:9]]
# p=lambda g:(c:=[8]*~-len([*filter(lambda s:{*s}&{5,8}=={5},g)])+[0]*9)and[c[:3],c[5:2:-1],c[6:9]]
# p=lambda g:(c:=[8]*~-sum({*s}&{5,8}=={5}for s in g)+[0]*9)and[c[:3],c[5:2:-1],c[6:9]]
# lambda g:[(c:=[8]*~-sum({*s}-{0}=={5}for s in g)+[0]*9)[:3],c[5:2:-1],c[6:9]]
p=lambda g:[(c:=[8]*g.count(max(g,key=any))+[0]*9)[:3],c[5:2:-1],[0]*3]








