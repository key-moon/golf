# best:30
# 36
# p=lambda g:g[:1]+(g[1:-1]+g[::-1])*2
# 33
# p=lambda g:(g+g[-2::-1])*2+g[:1]
# 30
p=lambda g:(g+g[1:-1])*2+g[:1]
