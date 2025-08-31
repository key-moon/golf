# best: 58(jailctf merger) / others: 68(4atj sisyphus luke Seek), 94(xsot ovs att joking mewheni), 106(mukundan), 117(kg583), 118(natte)
# import re;p=lambda g:[[*{*sum(g,[])}-{0,int(re.search(rf"([^0]), \1, \1.{{{len(g[0])*3-5}}}\1, ",str(g))[1])}]]
# import re;p=lambda g:[[int(({*(s:=str(g))}-{*" ,0[]",re.search(rf"([^0]), \1, \1.{{{len(g[0])*3-5}}}\1",s)[1]}).pop())]]
# import re;p=lambda g:[[int(re.search(rf"([^0]), \1, \1.{{{len(g[0])*3-5}}}\1, ((?!\1).)",str(g))[2])]]
# import re;p=lambda g:[[int(re.search(rf"([^0]), \1.{{{len(g[0])*3-5}}}\1, ((?!\1).), \1",str(g))[2])]]
# import re;p=lambda g:[[int(re.search(rf"(, [^0])\1{{2}}.{{{len(g[0])*3-7}}}\1(?!\1), (.)",str(g))[2])]]
# import re;p=lambda g:[[int(re.search(rf"(, [^0])\1{{2}}.{{{len(g[0])*3-7}}}\1(?!\1), .",str(g))[0][-1])]]
# import re;p=lambda g:[[int(re.search(r"(, [^0])\1{2}.{"+str(len(g[0])*3-7)+r"}\1(?!\1), (.)",str(g))[2])]]
# import re;p=lambda g:[[int(re.search(r"(, [^0])\1\1.{%d}\1(?!\1), (.)"%(len(g[0])*3-7),str(g))[2])]]
# ========================== 58 ==========================
p=lambda g:[[min(a:=sum(g+g[1:3]+g[1:],[]),key=a.count)]]

# g[0:4]*1+g[1:-1]*2
# g[1:-1]*1+g[1:3]*1
# g[1:-1]*1+g[1:4]*1
# g[1:-1]*2+g[2:4]*2

# cases = get_cases(346)
# cntr = Counter()

# sorted_cases = sorted(enumerate(cases), key=lambda x: [75, 89, 136, 266, 61, 14, 223, 80, 35, 194, 118, *range(1000)].index(x[0]))

# for i in range(-4,5):
#   for j in range(-4,5):
#     if i >= j and(i<0>j or i>=0<=j): continue
#     print(cntr)
#     for k in tqdm(range(-4,5)):
#       for l in range(-4,5):
#         if k >= l and(k<0>l or k>=0<=l): continue
#         for c1 in range(4):
#           for c2 in range(4):
#             wa = []
#             for idx, case in sorted_cases:
#               g=case['input']
#               ans = case['output'][0][0]
#               if ans != min(a:=sum(g+g[i:j]*c1+g[k:l]*c2,[]),key=a.count):
#                 wa.append(idx)
#                 if 2 <= len(wa): continue
#             prob = len(wa) / len(cases)
#             if prob < 0.01:
#               cntr.update(wa)
#               print(f"{prob} {wa}: g[{i}:{j}]*{c1}+g[{k}:{l}]*{c2}")
#               if prob == 0:
#                 input("> ")
