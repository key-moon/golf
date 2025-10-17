# best: 44(cubbus, 4atj sisyphus luke Seek mukundan, import itertools, jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 45(jonas ryno kg583 kabutack), 45(jacekwl Potatoman nauti), 45(jacekw Potatoman nauti natte), 45(JRK), 45(JRKX)
# =================== 44 ===================
# lambda g:[[(0<v)*s[0]for v in s]for s in g]
# lambda g:[[v%~v%-~s[0]for v in s]for s in g]
# lambda g:[[v and s[0]for v in s]for s in g]
p=lambda g:[[s[0]%2**v for v in s]for s in g]

# mapping = {
#     (0,0): 0, (0,1): 0, (0,2): 0, (0,3): 0, (0,4): 0, (0,6): 0, (0,7): 0, (0,8): 0, (0,9): 0,
#     (5,0): 0, (5,1): 1, (5,2): 2, (5,3): 3, (5,4): 4, (5,6): 6, (5,7): 7, (5,8): 8, (5,9): 9,
#     (1,1): 1, (2,2): 2, (3,3): 3, (4,4): 4, (6,6): 6, (7,7): 7, (8,8): 8, (9,9): 9,
# }

# # 遺跡
# from tqdm import tqdm
# for i in tqdm(range(2,20)):
#   for vlit in ["s", "~s", "-s", "-~s", "~-s"]:
#     for slit in ["v[0]", "~v[0]", "-v[0]", "-~v[0]", "~-v[0]"]:
#       for op in "+-*%&|^":
#         for op2 in "+-*%&|^":
#           for op3 in "+-*%&|^":
#             try:
#               for j in range(0,10):
#                 f = f"{i}{op}{vlit}{op2}{slit}{op3}{j}"
#                 if all([eval(f)==ans for s,v,ans in sum([[(0,[a],0),(a,[a],a),(5,[a],a)] for a in range(1,10)], [])]):
#                   print(f)
#             except ZeroDivisionError:
#               pass

