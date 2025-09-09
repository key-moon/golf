# best: 43(4atj sisyphus luke Seek mukundan, jailctf merger) / others: 44(xsot ovs att joking mewheni), 46(intgrah jimboko awu macaque sammyuri), 46(HETHAT), 47(cefqrn), 48(rucin93)
# =================== 43 ==================
# これ43らしい あと15byte縮むらしい 意味わからない
# 58
# p=lambda g:[[hash((x*10288502,1))%10for x in r]for r in g]
# 55
# p=lambda g:[[int("0564312798"[x])forx in r]for r in g]
# p=lambda g:[[8972134650//10**x%10forx in r]for r in g]
# p=lambda g:[[0x8972134650>>4*x&15forx in r]for r in g]
# p=lambda g:[[590324385360>>4*x&15forx in r]for r in g]
# p=lambda g:eval(str(g).translate("98,   05643127"*5))

# shortest:
# p=lambda g:[[1234567890123for x in g[0]]]*3
# p=lambda g:[[g[0][0],g[0][1],g[0][2]]]*3

# idea
# 1234567890123
# hash(x**9)%10
# b'\0?????????'[x]
# b'?'*9[x]*x%10
# x*A%BB//CC%BB
# x*A%BB//CC%BB

# なし
# max_length = 10
# {1: 5, 2: 6, 3: 4, 4: 3, 5: 1, 6: 2, 7: 7, 8: 9, 9: 8}

# close calls
# 1234567890123
# (38&47*x)%11 : [0, 5, 6, 4, 3, 1, 2, 0, 10, 5]
# (38&17*-x)%11: [0, 5, 6, 4, 3, 1, 2, 0, 10, 5]
# -x**6*2%97%10: [0, 5, 6, 4, 3, 1, 2, 4, 4, 4]
# 85%(1-x*8)%11: [0, 5, 6, 4, 3, 1, 2, 8, 3, 9]
# (550&47*x)%11: [0, 5, 6, 4, 3, 1, 2, 0, 10, 5]
# (473|47*x)%11: [0, 5, 6, 4, 3, 1, 2, 0, 10, 5]
# (x*991&70)%13: [0, 5, 6, 4, 3, 1, 2, 0, 12, 5]
# 70*x**5%98%13: [0, 5, 6, 4, 3, 1, 2, 0, 5, 6]
# 90851%9**x%11: [0, 5, 6, 4, 3, 1, 2, 2, 2, 2]

# t = [*enumerate([0,5,6,4,3,1,2,7,9,8])]
# for i in range(99):
#   for j in range(1,99):
#     for k in range(99):
#       for l in (10, 11, 12, 13):
#         for x, v in t:
#           if (x*i%j*k%l) != v:
#             break
#           if x == 9:
#             print((i, j, k, l))

# lambda g:[[*map(b"A564312798".find,g[0])]]*3
# lambda g:[[b'A564312798'[x]for x in g[0]]]*3
# lambda g:[[*map(b"A\x05\x06\x04\x03\x01\x02\x07\x09\x08".find,g[0])]]*3
p=lambda g:[[b'0\x05\x06\x04\x03\x01\x02\x07\x09\x08'[x]for x in g[0]]]*3






