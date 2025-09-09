# best: 61(jailctf merger) / others: 62(duckyluuk), 62(4atj sisyphus luke Seek mukundan), 62(xsot ovs att joking mewheni), 69(Bulmenisaurus), 70(intgrah jimboko awu macaque sammyuri)
# ============================ 61 ===========================

#p=lambda g:[[c for c in range(1,10)if len({s.count(c)for s in g})>2]]

# 二個以上の数字連続を消して、残りの一文字を返す
#import re;p=lambda g:[[re.sub('(\d)(, \\1)+','',str(g))]]

#p=lambda g:[[c+1 for c in range(9)if len({s.count(c+1)for s in g})>2]]

#p=lambda g,c=1:[[c]]*(len({s.count(c)for s in g})>2)or p(g,c+1)
p=lambda g,c=1:len({s.count(c)for s in g})//3*[[c]]or p(g,c+1)





