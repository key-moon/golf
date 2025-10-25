# 類題:257
# best: 79(Code Golf International, 4atj sisyphus luke Seek mukundan, jailctf merger) / others: 81(ox jam), 81(biz), 83(Tony Li & Darren Amadeus Martin), 84(jacekwl Potatoman nauti), 84(jacekw Potatoman nauti natte)
# ===================================== 79 ====================================
# p=lambda g:[[s[j+4]or t[j]or t[j+4]or s[j] for j in(0,1,2,3)]for s,t in zip(g,g[4:])]
p=lambda g:[[s[j]or t[j-4]or t[j]or s[j-4]for j in b""]for s,t in zip(g,g[4:])]

# 値
# 4 5
# 6 7
# 順序
# 4 1
# 2 3
