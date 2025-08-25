# best: 63(luke/sisyphus/Seek) / others: 64(joking+MWI), 64(luke), 64(joking/MWI), 64(att), 66(joking)
# ============================= 63 ============================
p=lambda g:g*0!=0and[p(g:=r)for r in g if r!=g][::2]or g