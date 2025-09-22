# best: 54(ox jam, jailctf merger, xsot ovs att joking mewheni) / others: 58(4atj sisyphus luke Seek mukundan), 58(intgrah jimboko awu macaque sammyuri), 58(Yuchen20), 60(2F), 60(biz)
# ======================== 54 ========================
# p=lambda g:[[x|y and 3for x,y in zip(*c)]for c in zip(g,g[5:])]
p=lambda g:[[(x!=y)*3for x,y in zip(*c)]for c in zip(g,g[5:])]

# 00 0
# 01 3
# 20 3
# 21 3
