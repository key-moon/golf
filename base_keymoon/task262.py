# best: 39(cubbus, jacekw Potatoman nauti natte, ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II, Code Golf International, 4atj sisyphus luke Seek mukundan, natte, import itertools, jailctf merger, ox jam, intgrah jimboko awu macaque sammyuri) / others: 40(kambarakun), 40(adakoda), 40(biz), 41(ShadowPrompt Labs), 42(jonas ryno kg583 kabutack)
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
