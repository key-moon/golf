# best: 67(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, biz, jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 68(xsot ovs att joking mewheni), 70(nauti), 80(kabutack), 81(mukundan), 82(duckyluuk)
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
