import	re
p=lambda	g:eval(re.sub(f"(?<=(\\d).{(C:='.'*-~len(g[0])*3)})\\1(?=.{C}\\1)",'0',str(g)))