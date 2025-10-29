# best: 93(HIMAGINE THE FUTURE.) / others: 94(Code Golf International), 94(4atj sisyphus luke Seek mukundan), 94(import itertools), 94(jailctf merger), 94(2F)
# ============================================ 93 ===========================================
# p=lambda g:[*zip(*[s[(d:=(a:=[min([*s,c].index(c)for s in zip(*g))for c in range(5)])[max(s)]-a[1]):]+s[:d]for s in zip(*g)])]
# p=lambda g:[*zip(*[s[(d:=(a:={c:sum(g,[]).index(c)//10for c in(0,1,2,4)})[max(s)]-a[1]):]+s[:d]for s in zip(*g)])]
# p=lambda g:[*zip(*[s[(d:=(a:={int(c):str(g).index(c)//32for c in"0124"})[max(s)]-a[1]):]+s[:d]for s in zip(*g)])]
# p=lambda g:[*zip(*[s[(d:=(a:=[str(g).index(c)//32for c in"012,4"])[max(s)]-a[1]):]+s[:d]for s in zip(*g)])]
# p=lambda g:[*zip(*[s[(d:=(f:=str(g).index)(str(max(s)))//32-f("1")//32):]+s[:d]for s in zip(*g)])]
# p=lambda g:[*zip(*[s[(d:=(f:=sum(g,[]).index)(max(s))//10-f(1)//10):]+s[:d]for s in zip(*g)])]
p=lambda g:[*zip(*map(lambda*s:s[(d:=(f:=sum(g,[]).index)(max(s))//10-f(1)//10):]+s[:d],*g))]

# def p(g):
#  a=[min([*s,c].index(c)for s in zip(*g))for c in range(5)]
#  return[*zip(*[s[(d:=a[max(s)]-a[1]):]+s[:d]for s in zip(*g)])]

# def p(g):
#  u=[*zip(*g)]
#  a={c:min([*s,c].index(c)for s in u)for c in(0,1,2,4)}
#  return[*zip(*[s[(d:=a[max(s)]-a[1]):]+s[:d]for s in u])]
