# best: 57(ox jam) / others: 58(lv1.dev), 58(FuunAgent), 58(jailctf merger), 58(HIMAGINE THE FUTURE.), 59(Code Golf International)
# ========================== 57 =========================
p=lambda g:[([0]*[*s,1].index(v:=max(*s,1))+[v,5]*9)[:len(s)]for s in g]
# p=lambda g:[(c:=0)or[(c:=v+(c and[5,max(s)][c==5]))for v in s]for s in g]

# 00 0
# 0v v
# v0 5
# 50 v
