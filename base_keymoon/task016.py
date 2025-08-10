# これ43らしい あと15byte縮むらしい 意味わからない
# 58
# p=lambda g:[[hash((x*10288502,1))%10for x in r]for r in g]
# 55
# p=lambda g:[[int("8972134650"[x])for x in r]for r in g]
# p=lambda g:[[8972134650//10**x%10for x in r]for r in g]
# p=lambda g:[[0x8972134650>>4*x&15for x in r]for r in g]
# p=lambda g:[[590324385360>>4*x&15for x in r]for r in g]

p=lambda g:[[590324385360>>4*x&15for x in r]for r in g]

# from itertools import count
# from tqdm import tqdm
# t = [*enumerate([0,5,6,4,3,1,2,7,9,8])]
# print(t)
# for s in tqdm(range(10288500, 102885020)):
#   for s2 in range(100):
#       for i, v in t:
#         if hash((i*s,s2))%10!=v:
#           break
#         if 7 <= i:
#           print(s, i)
#         if i == 9:
#           print(s, s2)
#           input("> ") 
