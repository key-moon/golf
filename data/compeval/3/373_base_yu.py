# p=lambda g:[u:=[g[0][0],g[1][0]]*3,u[::-1]]
# p=lambda g:[u:=(g[0]+g[1])[::6]*3,u[::-1]]
p=lambda g:[u:=sum(g,[])[::6]*3,u[::-1]]