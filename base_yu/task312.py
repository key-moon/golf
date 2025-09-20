# best: 44(4atj sisyphus luke Seek mukundan, jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 45(natte), 45(ox jam), 45(duckyluuk), 45(JRKX), 45(MasukenSamba)
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
