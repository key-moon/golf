# best: 95(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, jailctf merger) / others: 96(xsot ovs att joking mewheni), 101(jonas ryno kg583), 112(kg583), 112(kabutack), 112(JRK)
# ============================================= 95 ============================================
# p=lambda g:(G:=sum(g,[]),u:=sorted((G.count(c),G.index(c)%10,c)for c in{*G}-{0}))and[[c for k,_,c in u if k==u[-1][0]]]*u[-1][0]
# p=lambda g:(G:=sum(zip(*g),()),u:=[[c]*G.count(c)for c in G if c>0])and[*zip(*[s for s in u if len(s)==max(map(len,u))])]

def p(g):
 G=sum(g,[])
 u=sorted((G.count(c),G.index(c)%10,c)for c in{*G}-{0})
 return[[c for k,_,c in u if k==u[-1][0]]]*u[-1][0]
