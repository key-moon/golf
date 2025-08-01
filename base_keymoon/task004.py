# 「輪」のいちばん下のcomponent以外を動かす
# 輪の下には0,0,0...があることを利用して下端を判別（下端のときは動かさず、さらに一個上のを動かす）
def p(g):
  p=[0]
  for val_line in g[::-1]:
    # 最後のindexをとってくるほうほう
    # max(range(len(g)),key=lambda x:l[x])
    if s:=sum(p):
      a=max(p);i=p.index(a)+s//a
      val_line[:i]=[0]+val_line[:i-1]
    p=val_line
  return g
