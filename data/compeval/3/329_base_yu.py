# best: 54(ovs, luke, mukundan, 4atj, Seek64, nauti, MasukenSamba, att, xsot, kabutack) / others: 56(duckyluuk), 64(dbdr), 64(natte), 64(kg583), 66(joking)
# p=lambda g:[[v*(i==len(s)//2)for i,v in enumerate(s)]for s in g]
# lambda g:[(a:=[0]*(b:=len(s)//2))+[s[b],*a]for s in g]
# ======================== 54 ========================
p=lambda g:[[0]*(b:=len(s)//2)+[s[b]]+b*[0]for s in g]
