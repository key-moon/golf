# best: 50(mukundan, luke, 4atj, xsot, ovs, att, sisyphus) / others: 54(duckyluuk), 56(kg583), 56(Seek64), 56(joking), 56(kabutack)
# p=lambda g:[[b"\0\6"[0<a+b]for a,b in zip(r,r[3:])]for r in g]
# p=lambda g:[[b"\0\6"[0<r[i]+r[i+3]]for i in(0,1,2)]for r in g]
# p=lambda g:[[b"06"[0<r[i]+r[i+3]]for i in b"012"]for r in g]
# p=lambda g:[[6*(0<sum(s))for s in zip(r,r[3:])]for r in g]
# p=lambda g:[[6*(0<r[i]+r[i+3])for i in(0,1,2)]for r in g]
# (0,1,2)
#  b"012"
# map(sum,zip(r,r[3:]))
#            r[i::2]
# lambda g:[[               for s in r]for r in g]
# lambda g:[[          for i in(0,1,2)]for r in g]
# lambda g:[[    for s in zip(r,r[3:])]for r in g]
# テスト用だから詰めきってないのは許して
# ====================== 50 ======================
p=lambda g:[[6*(0<r[i]+r[i+3])for i in(0,1,2)]for r in g];p;p;p;p;p;p;p;p
