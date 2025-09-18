# best: 111(4atj sisyphus luke Seek mukundan) / others: 112(jailctf merger), 128(xsot ovs att joking mewheni), 161(Yuchen20), 165(jacekwl Potatoman nauti), 178(MasukenSamba)
# ==================================================== 111 ====================================================
# p=lambda g:max((all(y:=sum(x:=[s[l:r]for s in g[u:d]],[])),y.count(2),len(y),x)for r in range(11)for l in range(r)for d in range(11)for u in range(d))[3]
# lambda g:max((all(y:=sum(x:=[s[l:t%11]for s in g[u:t//11]],[])),y.count(2),len(y),x)for t in range(121)for l in range(t%11)for u in range(t//11))[3]


# p=lambda g,A=range:max((all(y:=sum(x:=[s[l:r]for s in g[u:d]],[])),y.count(2),len(y),x)for r in A(11)for l in A(r)for d in A(11)for u in A(d))[3]
# p=lambda g,c=-1:c*g or max([p([*zip(*g[l:r])],c+1)for r in range(11)for l in range(r)],key=lambda g:(all(y:=sum(g,g[0]*0)),y.count(2),len(y),g))
# p=lambda g,c=-1:c*g or min([p([*zip(*g[l:r])],c+1)for r in range(11)for l in range(r)],key=lambda g:("0"in(y:=str(g)),-y.count("2"),-len(y),g))
# p=lambda g,c=-1:c*g or min([("0"in(y:=str(u:=p([*zip(*g[l:r])],c+1))),-y.count("2"),-len(y),u)for r in range(11)for l in range(r)])[3]
p=lambda g,c=-3:c*g or min(("0"in(y:=str(u:=p([*zip(*g[l::-1])],c+1))),-y.count("2"),-len(y),u)for l in range(len(g)))[3]

# def p(g):
#  for r in range(10):
#   for l in range(r):
#    for d in range(10):
#     for u in range(d):
#      y=sum(x:=[s[l:r] for s in g[u:d]],[])
#      -all(y),y.count(2),len(y),x
#  return g
