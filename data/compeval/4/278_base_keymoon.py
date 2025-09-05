import	re
p=lambda	g,c=-11:g*c	or	p(eval(re.sub('0(?=.{,3}(.{%s})?2.{%s}2)'%(a:=len(g)*3-2,a+3),'3',str([*zip(*g)][::1|c%3%-2]))),c+1)