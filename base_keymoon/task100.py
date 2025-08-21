# best: 54(biz, luke, 4atj, sisyphus) / others: 55(dbdr), 56(duckyluuk), 59(Seek64), 59(joking), 59(xsot)
# min(a,key=a.count) だと誤判定 min(a[:-1],key=a.count)で耐え
# lambda g:[[sorted(a:=sum(g,[])[:-1],key=(k:=a.count))[~k(0)]]*2]*2
# lambda g:[[max(a:=sum(g,[]),key=lambda x:(0<x)*a.count(x))]*2]*2
# lambda g:[[*{*(a:=sum(g,[])[:-1])}-{0,min(a,key=a.count)}]*2]*2
# lambda g:[[sum({*(a:=sum(g,[])[:-1])})-min(a,key=a.count)]*2]*2
# lambda g:[[sorted({*(a:=sum(g,[]))},key=a.count)[1]]*2]*2
# lambda g:[[sorted(set(a:=sum(g,[])),key=a.count)[1]]*2]*2
# lambda g:[sorted(set(a:=sum(g,[])),key=a.count)[1:2]*2]*2
# ======================== 54 ========================
p=lambda g:[sorted(set(a:=sum(g,[])),key=a.count)[1:2]*2]*2
