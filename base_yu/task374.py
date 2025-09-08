# best: 112(jailctf merger) / others: 119(4atj sisyphus luke Seek mukundan), 123(4atj sisyphus luke Seek), 130(mukundan), 150(xsot ovs att joking mewheni), 155(MasukenSamba)
# ==================================================== 112 =====================================================
p=lambda g,c=23:-c*g or p([*zip(*eval(str(g).replace((c//2*", 5")[2:],(c//2*f",{len({*sum(g,g[0])})*3%5}")[1:])))],c-1)


# def p(g):
#  for c in range(4,24)[::-1]:
# #   g=eval(str(g).replace((c//2*", 5")[2:],(c//2*f",{4**len({*str(g)})%7}")[1:]))
# #   g=[*map(list,zip(*g))]
#   g=eval(str(g).replace((c//2*", 5")[2:],(c//2*f",{len({*sum(g,g[0])})*3%5}")[1:]))
#   g=[*zip(*g)]
#  return g
