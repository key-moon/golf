# best: 61(luke, kg583) / others: 64(joking), 66(4atj), 67(att), 70(mukundan), 70(duckyluuk)
# ============================ 61 ===========================
p=lambda g:[([0]*[*s,1].index(v:=max(*s,1))+[v,5]*9)[:len(s)]for s in g]
# p=lambda g:[(c:=0)or[(c:=v+(c and[5,max(s)][c==5]))for v in s]for s in g]

# 00 0
# 0v v
# v0 5
# 50 v

