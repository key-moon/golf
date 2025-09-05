# best: 64(att) / others: 66(luke), 72(sisyphus), 74(ovs), 80(joking), 84(mukundan)
# ============================= 64 =============================
# lambda s,c=0:sum([[v*0!=0and p(v,c:=9-sum(s,[]).count(0))or v]*c for v in s],[])
# lambda s,c=0:sum([[v*0!=0and p(v,c:=9-str(s).count("0"))or v]*c for v in s],[])
# lambda s,c=0:sum([[v*0!=0and p(v,c:=len({*str(s)})-5)or v]*c for v in s],[])
# ============================= 64 =============================
p=lambda s:sum([[v*0!=0and p(v+s)or v]*(len({*str(s)})-5)for v in s[:3]],[])
