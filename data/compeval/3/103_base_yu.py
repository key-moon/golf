# 345678901234567890123456789
# p=lambda g:[[7**([*zip(*g)][0]!=[*zip(*g)][2])]]
# p=lambda g:[[7**any(s[0]!=s[2]for s in g)]]
p=lambda g:[[7**any(a!=c for a,_,c in g)]]