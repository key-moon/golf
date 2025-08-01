# 「輪」のいちばん下のcomponent以外を動かす
# 輪の下には0,0,0...があることを利用して下端を判別（下端のときは動かさず、さらに一個上のを動かす）
def p(g):
  p=[0]
  for l in g[::-1]:
    # 最後のindexをとってくるほうほう
    # max(range(len(g)),key=lambda x:l[x])
    if s:=sum(p):
      a=max(p);i=p.index(a)+s//a
      l[:i]=[0]+l[:i-1]
    p=l
  return g
