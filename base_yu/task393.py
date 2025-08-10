# p=lambda g:[[v]for v,_ in __import__("collections").Counter(sum(g,[])).most_common()[1:]]
p=lambda g:[[v]for v in sorted({*sum(g,[])},key=sum(g,[]).count)[2::-1]]
