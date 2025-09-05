# 0以外の要素を一列に並べる それらはすべて同じ値
# p=lambda j:[[m:=max(s:=sum(j,[]))]*(sum(s)//m)]
# p=lambda j:[[x for x in sum(j,[])if x]]
p=lambda j:[[*filter(int,sum(j,[]))]]
