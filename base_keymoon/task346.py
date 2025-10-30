# best: 55(jacekw Potatoman nauti natte, import itertools) / others: 56(HIMAGINE THE FUTURE.), 58(jailctf merger), 68(Code Golf International), 68(4atj sisyphus luke Seek mukundan), 68(ox jam)
# import re;p=lambda g:[[*{*sum(g,[])}-{0,int(re.search(rf"([^0]), \1, \1.{{{len(g[0])*3-5}}}\1, ",str(g))[1])}]]
# import re;p=lambda g:[[int(({*(s:=str(g))}-{*" ,0[]",re.search(rf"([^0]), \1, \1.{{{len(g[0])*3-5}}}\1",s)[1]}).pop())]]
# import re;p=lambda g:[[int(re.search(rf"([^0]), \1, \1.{{{len(g[0])*3-5}}}\1, ((?!\1).)",str(g))[2])]]
# import re;p=lambda g:[[int(re.search(rf"([^0]), \1.{{{len(g[0])*3-5}}}\1, ((?!\1).), \1",str(g))[2])]]
# import re;p=lambda g:[[int(re.search(rf"(, [^0])\1{{2}}.{{{len(g[0])*3-7}}}\1(?!\1), (.)",str(g))[2])]]
# import re;p=lambda g:[[int(re.search(rf"(, [^0])\1{{2}}.{{{len(g[0])*3-7}}}\1(?!\1), .",str(g))[0][-1])]]
# import re;p=lambda g:[[int(re.search(r"(, [^0])\1{2}.{"+str(len(g[0])*3-7)+r"}\1(?!\1), (.)",str(g))[2])]]
# import re;p=lambda g:[[int(re.search(r"(, [^0])\1\1.{%d}\1(?!\1), (.)"%(len(g[0])*3-7),str(g))[2])]]
# ========================= 55 ========================
p=lambda g:[[min(a:=sum(g+g[1:-3:3],g[3]),key=a.count)]]

# g[0:4]*1+g[1:-1]*2
# g[1:-1]*1+g[1:3]*1
# g[1:-1]*1+g[1:4]*1
# g[1:-1]*2+g[2:4]*2
# sum(g+g[1:3]+g[1:],[])
# sum(g+g[1:-3:3],g[3])
# sum(g+g[1:-2:3],g[3])

# from collections import Counter
# from tqdm import tqdm

# from utils import get_cases


# cases = get_cases(346)
# cntr = Counter()

# sorted_cases = sorted(enumerate(cases), key=lambda x: [75, 89, 136, 266, 61, 14, 223, 80, 35, 194, 118, *range(1000)].index(x[0]))

# for i in range(-4,5):
#   for j in [0]:
#     if i >= j and(i<0>j or i>=0<=j): continue
#     print(cntr)
#     for k in tqdm(range(-4,5)):
#       if k == 0: continue
#       for l in range(-4,5):
#         for c1 in range(4):
#           for c2 in range(4):
#             wa = []
#             for idx, case in sorted_cases:
#               g=case['input']
#               ans = case['output'][0][0]
#               if ans != min(a:=sum(g+g[i::k]*c1,g[l]*c2),key=a.count):
#                 wa.append(idx)
#                 if 2 <= len(wa): continue
#             prob = len(wa) / len(cases)
#             if prob < 0.01:
#               cntr.update(wa)
#               print(f"{prob} {wa}: g[{i}:{j}:{k}]*{c1},g[{l}]*{c2}")
#               if prob == 0:
#                 input("> ")
