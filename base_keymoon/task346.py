# best: 102(luke/sisyphus/Seek, Seek64) / others: 106(mukundan), 112(ovs), 117(kg583), 118(natte), 132(joking+MWI)
# import re;p=lambda g:[[*{*sum(g,[])}-{0,int(re.search(rf"([^0]), \1, \1.{{{len(g[0])*3-5}}}\1, ",str(g)).group(1))}]]
# import re;p=lambda g:[[int(({*(s:=str(g))}-{*" ,0[]",re.search(rf"([^0]), \1, \1.{{{len(g[0])*3-5}}}\1",s).group(1)}).pop())]]
# import re;p=lambda g:[[int(re.search(rf"([^0]), \1, \1.{{{len(g[0])*3-5}}}\1, ((?!\1).)",str(g))[2])]]
# import re;p=lambda g:[[int(re.search(rf"([^0]), \1.{{{len(g[0])*3-5}}}\1, ((?!\1).), \1",str(g))[2])]]
# import re;p=lambda g:[[int(re.search(rf"(, [^0])\1{{2}}.{{{len(g[0])*3-7}}}\1(?!\1), (.)",str(g))[2])]]
# import re;p=lambda g:[[int(re.search(rf"(, [^0])\1{{2}}.{{{len(g[0])*3-7}}}\1(?!\1), .",str(g))[0][-1])]]
# import re;p=lambda g:[[int(re.search(r"(, [^0])\1{2}.{"+str(len(g[0])*3-7)+r"}\1(?!\1), (.)",str(g))[2])]]
# =============================================== 102 ================================================
import re;p=lambda g:[[int(re.search(rf"(, [^0])\1\1.{{{len(g[0])*3-7}}}\1(?!\1), (.)",str(g))[2])]]
