# =============================================8901234
# 345678901234567890123456789012345678901234567890
# p=lambda g:g[-1:]+[[v and 2for v in s]for s in g[:-1]]
p=lambda g:eval(str(g[-1:]+g[-1:]).replace(*"82"))
# p=lambda g:eval(str((g*2)[len(g)-1:-1]).replace(*"82"))
# p=lambda g:g[-1:]+eval(f"{g[:-1]}".replace(*"82"))

