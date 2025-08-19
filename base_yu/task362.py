# 3456789012345678901234567890123456789012345678901234567890123456789
# p=lambda g:(k:=sum(g,[]).count(5))and[[v*(v!=5)for v in s[k:]+s[:k]]for s in g[-k:]+g[:-k]]
# p=lambda g:(k:=sum(g,[]).count(5))and[s[k:9]+s[:1]+s[:k]for s in g[-k:]+g[:-k]]
# p=lambda g:(k:=sum(g,[]).count(5))and[s[k:9]+-~k*s[:1]for s in g[-k:]+g[:-k]]
p=lambda g:(k:=str(g).count("5"))and[s[k:9]+-~k*s[:1]for s in g[-k:]+g[:-k]]
# p=lambda g:(k:=sum(g,[]).count(5))and eval(str([s[k:]+s[:k]for s in g[-k:]+g[:-k]]).replace(*"50"))
