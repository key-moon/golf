# best: 67(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, import itertools, jailctf merger, 2F, biz) / others: 68(jacekwl Potatoman nauti), 68(jacekw Potatoman nauti natte), 68(jacekw Potatoman nauti), 68(natte), 68(ox jam)
# =============================== 67 ==============================
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
