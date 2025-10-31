# best: 66(ox jam) / others: 67(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 67(Code Golf International), 67(4atj sisyphus luke Seek mukundan), 67(lv1.dev), 67(LogicLynx)
# ============================== 66 ==============================
# 351と同じ問題
#flattenして点対称の位置を集める
# r=range(5)
# p=lambda g:[[(t:=sum(g,[]))[~t.index(1)-i*24-j]for j in r]for i in r]

p=lambda g:[(t:=sum(g,[]))[~t.index(1)-i*24::-1][:5]for i in range(5)]

# def p(g):
#  t=sum(g,[])
#  k=t.index(1)
#  return [t[~k-i*24::-1][:5] for i in range(5)]
#  return [t[~k-i*24-4:][:5][::-1] for i in range(5)]
