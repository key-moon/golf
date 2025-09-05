import	re
p=lambda	g:eval(re.sub(f"(?<=([1-9]){(C:='.'*(len(g[0])*3+4))})\\1(?={C}\\1)",'8',str(g)))