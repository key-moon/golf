# best: 50(ovs, luke, mukundan, 4atj, att, xsot, sisyphus) / others: 54(duckyluuk), 56(Seek64), 56(joking), 56(kg583), 56(kabutack)
# ====================== 50 ======================
# p=lambda g:[[s[i]|s[i+3]and 6for i in range(3)]for s in g]
# p=lambda g:[[x|y and 6for x,y in zip(s,s[3:])]for s in g]
p=lambda g:[[(x|y>0)*6for x,y in zip(s,s[3:])]for s in g]


