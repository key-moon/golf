# best: 65(Code Golf International) / others: 67(4atj sisyphus luke Seek mukundan), 67(jailctf merger), 68(ox jam), 69(import itertools), 69(HIMAGINE THE FUTURE.)
# ============================== 65 =============================
p=lambda g:[[sum({*sum(g,s)})-v for v in s if v]for s in g if any(s)]
