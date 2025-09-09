# best: 94(biz) / others: 97(xsot ovs att joking mewheni), 109(4atj sisyphus luke Seek mukundan), 111(jailctf merger), 120(duckyluuk), 184(MasukenSamba)
# ============================================ 94 ============================================
p=lambda g:[*zip(*[s[(d:=(a:=[min([*s,c].index(c)for s in zip(*g))for c in range(5)])[max(s)]-a[1]):]+s[:d]for s in zip(*g)])]

# def p(g):
#  a=[min([*s,c].index(c)for s in zip(*g))for c in range(5)]
#  return[*zip(*[s[(d:=a[max(s)]-a[1]):]+s[:d]for s in zip(*g)])]

# def p(g):
#  u=[*zip(*g)]
#  a={c:min([*s,c].index(c)for s in u)for c in(0,1,2,4)}
#  return[*zip(*[s[(d:=a[max(s)]-a[1]):]+s[:d]for s in u])]

