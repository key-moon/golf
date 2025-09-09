# best: 80(4atj sisyphus luke Seek mukundan) / others: 82(jailctf merger), 83(xsot ovs att joking mewheni), 93(biz), 108(jacekwl Potatoman nauti), 139(duckyluuk)
# 「輪」のいちばん下のcomponent以外を動かす
# 輪の下には0,0,0...があることを利用して下端を判別（下端のときは動かさず、さらに一個上のを動かす）
# 最後が
# def p(g):
#   val_prev=[0]
#   for val_line in g[::-1]:
#     if val_sum:=sum(val_prev):
#       val_cell=max(val_prev)
#       if val_sum//val_cell!=2:
#         val_line.pop(val_prev.index(val_cell))
#       else:
#         val_line.pop()
#       val_line.insert(0,0)
#     val_prev=val_line
#   return g
# 125
# def p(g):
#   val_prev=[0]
#   for val_line in g[::-1]:
#     if val_sum:=sum(val_prev):val_line.insert(0,val_line.pop([-1,val_prev.index(val_cell:=max(val_prev))][val_sum//val_cell!=2]))
#     val_prev=val_line
#   return g
# 絶対に今の値は必要→maxは必須
# def p(g):
#   p=[0]
#   for l in g[::-1]:
#     # if s:=sum(p):l.insert(0,l.pop([-1,p.index(c:=max(p))][s//c!=2]))
#     l.insert(0,l.pop([-1,p.index(c:=max(p))][p.count(c)!=2]))
#     p=l
#   return g
# def p(g):p=[0];return [[l.pop([-1,p.index(c:=max(p))][p.count(c)!=2]),p:=[0,*l]][1] for l in g[::-1]][::-1]
# lambda g,p=[0]:[[l.pop([-1,p.index(c:=max(p))][p.count(c)!=2]),p:=[0,*l]][1]for l in g[::-1]][::-1]
# ===================================== 80 =====================================
# lambda g:[[s.pop([-1,t.index(c:=max(t))][t.count(c)!=2]),*s]for s,t in zip(g,(g*2)[1:])]
p=lambda g:[[s.pop(t.index(c:=max(t))|-1*(0<2*c==sum(t)))]+s for s,t in zip(g,(g*2)[1:])]

# t.count(c)!=2
# 0<c==sum(t)/2

# 次:
# [0,2,0,2,0] <- これだけ-1にしたい
# [0,2,2,2,0] <- これは中間
# [0,0,0,0,0] <- 先頭の方がいい

