# best: 64(att) / others: 66(luke), 72(sisyphus), 74(ovs), 80(joking), 84(mukundan)
# ============================= 64 =============================
# p=lambda s,c=0:sum([[v*0!=0and p(v,c:=9-sum(s,[]).count(0))or v]*c for v in s],[])
# p=lambda s,c=0:sum([[v*0!=0and p(v,c:=9-str(s).count("0"))or v]*c for v in s],[])
p=lambda s,c=0:sum([[v*0!=0and p(v,c:=len({*sum(s,v)})-1)or v]*c for v in s],[])