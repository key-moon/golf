# サイクルを発見する（3サイクルか4サイクルかの二択）
# def p(g):
#   if g[:3]==g[3:]:
#     return[[c*2for c in r]for r in g+g[:3]]
#   else:
#     return[[c*2for c in r]for r in g+g[2:5]]
p=lambda g:[[val_cell*2for val_cell in val_row]for val_row in g+g[(g[:3]!=g[3:])*2:][:3]]