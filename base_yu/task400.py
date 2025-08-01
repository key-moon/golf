r=range(5)
p=lambda g:[[(t:=sum(g,[]))[~t.index(1)-i*24-j] for j in r]for i in r]