# p=lambda g:[[v]for v,_ in __import__("collections").Counter(sum(g,[])).most_common()[1:]]
p=lambda g:(G:=sum(g,[]))and[[v]for _,v in sorted((G.count(v),v)for v in{*G})[2::-1]]
