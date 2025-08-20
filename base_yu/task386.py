# best: 52(ovs, luke, mukundan, 4atj, att, xsot, sisyphus) / others: 54(Seek64), 56(natte), 56(HashPanda), 56(duckyluuk), 56(cg)
# ======================= 52 =======================
# p=lambda g:[[*eval("3-(s.pop(0)|s[3]and 3),"*3)]for s in g]
# p=lambda g:[[3-3*(s[i]|s[i+4]>0)for i in(0,1,2)]for s in g]
p=lambda g:[[*eval("3-3*(s.pop(0)|s[3]>0),"*3)]for s in g]
