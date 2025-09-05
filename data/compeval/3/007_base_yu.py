# best: 65(luke, luke/sisyphus/Seek) / others: 67(biz), 68(ovs), 68(mukundan), 68(4atj), 68(att)
# ============================== 65 =============================
# p=lambda g:(G:=sum(g,[]))and[[max(G[(i+j)%3::3])for j in range(7)]for i in range(7)]
p=lambda g,R=range(7):[[max(sum(g,[])[(i+j)%3::3])for j in R]for i in R]
# p=lambda g:(u:=[max(sum(g,[])[i::3])for i in(0,1,2)]*99)and[u[i*7:i*7+7] for i in range(7)]
