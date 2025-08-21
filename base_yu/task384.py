# best: 64(luke, 4atj, sisyphus) / others: 66(biz), 68(mukundan), 69(att), 70(natte), 89(dbdr)
# ============================= 64 =============================
p=lambda g,c=2:c and p(sum([[[*s]]*2for s in zip(*g)if sum(s)],[]),c-1)or g
# p=lambda g:len(g[0])%2and p(sum([[[*s]]*2for s in zip(*g)if sum(s)],[]))or g