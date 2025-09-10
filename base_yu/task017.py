# best: 99(jailctf merger) / others: 109(4atj sisyphus luke Seek mukundan), 120(xsot ovs att joking mewheni), 149(duckyluuk), 161(intgrah jimboko awu macaque sammyuri), 164(2F)
# =============================================== 99 ==============================================
# p=lambda g,R=range(21):[[[u[(i%d,j%d)]for j in R]for i in R]for d in range(4,10)if len(u:=dict(m:=[((i%21%d,i//21%d),v)for i,v in enumerate(sum(g,[]))if v]))==len({*m})][0]


# p=lambda g:[u for d in range(4,10)if(u:=[[max(max(g[i%d::d])[j%d::d])for j in range(21)]for i in range(21)])if sum(s in g for s in u)>9][0]
p=lambda g,R=range(21):[u for d in range(4,10)if(u:=[[max(max(g[i%d::d])[j%d::d])for j in R]for i in R])[0]in g or u[1]in g][0]


# def p(g):
#  cor = [d for d in range(4,10)if len(u:=dict(m:=[((i%21%d,i//21%d),v)for i,v in enumerate(sum(g,[]))if v]))==len({*m})][0]
#  for d in range(4,10):
#   u=[[max(max(g[i%d::d])[j%d::d])for j in range(21)]for i in range(21)]
# #    DUMP(u)
# #    DUMP(u[:d])
# #    DUMP(u[d:d+d])
#   print(cor,d,sum(s in g for s in u))
# #   assert (sum(s in g for s in u)>10)==(cor==d)
#   if sum(s in g for s in u)>9:
#    return u
# #   if d==cor:
# #    return u

#    return [[max(g[i%d+d][j%d::d]) for j in range(21)]for i in range(21)]
#    return [[max(g[i%d::d])[j%d+d] for j in range(21)]for i in range(21)]
# def p(g):
#  for d in range(4,10):
#   if len(u:=dict(m:=[((i%21%d,i//21%d),v) for i,v in enumerate(sum(g,[]))if v]))==len({*m}):
#    return [[u[(i%d,j%d)]for j in range(21)]for i in range(21)]







