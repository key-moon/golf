# best: 71(jacekw Potatoman nauti natte, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, import itertools, jailctf merger, HIMAGINE THE FUTURE., ox jam, biz) / others: 72(jacekw Potatoman nauti), 74(JRKX), 74(JRKXK), 74(JRKKX), 75(HETHAT)
# ================================= 71 ================================
# p=lambda g:(a:=[*filter(int,map(sum,zip(*g)))],c:=[8]*(a[0]//5-(a[1]+3)//8)+[0]*9)and[c[:3],c[5:2:-1],c[6:9]]
# p=lambda g:(a:=[*({s.count(0)for s in zip(*g)}-{len(g)})],c:=[8]*abs(a[0]-a[1])+[0]*9)and[c[:3],c[5:2:-1],c[6:9]]
# p=lambda g:(c:=[8]*(len([*filter(lambda s:5 in s and 8 not in s,g)])-1)+[0]*9)and[c[:3],c[5:2:-1],c[6:9]]
# p=lambda g:(c:=[8]*~-len([*filter(lambda s:{*s}&{5,8}=={5},g)])+[0]*9)and[c[:3],c[5:2:-1],c[6:9]]
# p=lambda g:(c:=[8]*~-sum({*s}&{5,8}=={5}for s in g)+[0]*9)and[c[:3],c[5:2:-1],c[6:9]]
# lambda g:[(c:=[8]*~-sum({*s}-{0}=={5}for s in g)+[0]*9)[:3],c[5:2:-1],c[6:9]]
p=lambda g:[(c:=[8]*g.count(max(g,key=any))+[0]*9)[:3],c[5:2:-1],[0]*3]
