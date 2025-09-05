# best: 64(luke, 4atj, sisyphus) / others: 65(att), 66(biz), 68(mukundan), 70(natte), 89(dbdr)
# lambda g:len(g[0])%2and p(sum([[[*s]]*2for s in zip(*g)if sum(s)],[]))or g
# lambda g,c=2:c and p(sum([[[*s]]*2for s in zip(*g)if sum(s)],[]),c-1)or g
# lambda g,c=-1:c*g or p(sum([[[*s]]*2for s in zip(*g)if sum(s)],[]),c+1)
#  sum(s)
# {*s}-{0}
# ============================= 64 =============================
p=lambda g,c=-1:c*g or p(sum([[s]*2for s in zip(*g)if 4in s],[]),c+1)
