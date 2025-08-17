# 345678901234567890123456789012345678901234567890
# p=lambda g:[[v^13*(v in(5,8))for v in s]for s in g]
p=lambda g:[[v^13*(v>v%3>1)for v in s]for s in g]
