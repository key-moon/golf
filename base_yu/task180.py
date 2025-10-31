# 類題:257
# best: 74(ox jam) / others: 79(Code Golf International), 79(4atj sisyphus luke Seek mukundan), 79(jailctf merger), 81(biz), 82(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# ================================== 74 ==================================
# p=lambda g:[[s[j+4]or t[j]or t[j+4]or s[j] for j in(0,1,2,3)]for s,t in zip(g,g[4:])]
p=lambda g:[[s[j]or t[j-4]or t[j]or s[j-4]for j in b""]for s,t in zip(g,g[4:])]

# 値
# 4 5
# 6 7
# 順序
# 4 1
# 2 3
