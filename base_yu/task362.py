# best: 69(jacekw Potatoman nauti natte, Code Golf International, 4atj sisyphus luke Seek mukundan, natte, import itertools, jailctf merger, ox jam) / others: 74(jacekwl Potatoman nauti), 74(jacekw Potatoman nauti), 74(THUNDER THUNDER), 75(HIMAGINE THE FUTURE.), 76(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# ================================ 69 ===============================
# 3456789012345678901234567890123456789012345678901234567890123456789
# p=lambda g:(k:=sum(g,[]).count(5))and[[v*(v!=5)for v in s[k:]+s[:k]]for s in g[-k:]+g[:-k]]
# p=lambda g:(k:=sum(g,[]).count(5))and[s[k:9]+s[:1]+s[:k]for s in g[-k:]+g[:-k]]
# p=lambda g:(k:=sum(g,[]).count(5))and[s[k:9]+-~k*s[:1]for s in g[-k:]+g[:-k]]
# p=lambda g:(k:=str(g).count("5"))and[s[k:9]+-~k*s[:1]for s in g[-k:]+g[:-k]]
# p=lambda g:(k:=sum(g,[]).count(5))and eval(str([s[k:]+s[:k]for s in g[-k:]+g[:-k]]).replace(*"50"))

def p(g):
 k=str(g).count("5")
 return[s[k:9]+-~k*s[:1]for s in g[-k:]+g[:-k]]
