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
def p(g):
  val_prev=[0]
  for val_line in g[::-1]:
    if val_sum:=sum(val_prev):
      val_line.insert(0,val_line.pop([-1,val_prev.index(val_cell:=max(val_prev))][val_sum//val_cell!=2]))
      # val_line[:[val_prev.index(val_cell:=max(val_prev)),]]
      # val_line.insert(0,val_line.pop([-1,val_prev.index(val_cell:=max(val_prev))][val_sum//val_cell!=2]))
    val_prev=val_line
  return g
