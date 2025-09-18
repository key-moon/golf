# best: 39(ox jam, 4atj sisyphus luke Seek mukundan, jailctf merger, intgrah jimboko awu macaque sammyuri, xsot ovs att joking mewheni) / others: 42(natte), 42(duckyluuk), 42(MasukenSamba), 42(dbdr), 42(kabutack)
# lambda g:[[b"\2\4\3"[s.index(5)]]*3for s in g]
# lambda g:[[-s.index(5)%3+2]*3for s in g]
# lambda g:[[hash((*s,))%5+2]*3for s in g]
# lambda g:[[3+s[1]%2-s[0]%2]*3for s in g]
# lambda g:[[hash((*s,1))%1+1]*3for s in g]
# lambda g:[[13+b-a>>2  ]*3for a,b,_ in g]
# ================= 39 ================
p=lambda g:[[-~b&~a^2]*3for a,b,_ in g]

# 1+a&~b^2
# -~a&~b^2
# 2^~a&b+1

#                 ^2 ^3 ^4
# [5, 0, 0] -> 2   0  5  6
# [0, 5, 0] -> 4   6  7  0
# [0, 0, 5] -> 3   1  0  7

# for i in range(-9,20):
#   for alit in ["a", "~a", "-a", "-~a", "~-a"]:
#     for blit in ["b", "~b", "-b", "-~b", "~-b"]:
#       for op in "+-*%&|^":
#         for op2 in "+-*%&|^":
#           for op3 in "+-*%&|^":
#             try:
#               for j in range(-9,20):
#                 f = f"{i}{op}{alit}{op2}{blit}{op3}{j}"
#                 s = {*[eval(f) for a,b in [(5,0),(0,5),(0,0)]]}
#                 if s == {2,3,4}:
#                   print(f)
#             except ZeroDivisionError:
#               pass
