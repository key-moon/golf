# best: 95(Seek64) / others: 96(4atj), 99(ovs), 112(kg583), 114(mukundan), 114(joking+MWI)
# ============================================= 95 ============================================
p=lambda g:(G:=sum(g,[]),u:=sorted((G.count(c),G.index(c)%10,c)for c in{*G}-{0}))and[[c for k,_,c in u if k==u[-1][0]]]*u[-1][0]
# p=lambda g:(G:=sum(zip(*g),()),u:=[[c]*G.count(c)for c in G if c>0])and[*zip(*[s for s in u if len(s)==max(map(len,u))])]
