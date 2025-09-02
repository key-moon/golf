import re
p=lambda g,c=-3:c*g or[*zip(*eval(re.sub("%d, ([^\]0%d])(,.+%d.{34})0"%(d:=max(max(g),key=bool),d,d),r"%d,0\2 \1"%d,str(p(g,c+1))))[::-1])]