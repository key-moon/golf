import re
p=lambda g,c=-23:c*g or p(eval(re.sub('(?<=[24], )[^02](?=(.{%d})?, [24])'%~-len(g*3),'4',str([*zip(*g[::-1])]))),c+1)