# best: 71(luke, mukundan) / others: 75(nauti), 75(biz), 76(joking), 81(MeWhenI), 81(kabutack)
# ================================= 71 ================================
# p=lambda g:(u:=[*filter(int,map(max,zip(*g)))]+[0]*9)and[u[:3],u[5:2:-1],u[6:9]]
p=lambda g:[(u:=[*filter(int,map(max,*g))]+[0]*9)[:3],u[5:2:-1],u[6:9]]