# best: 63(Code Golf International, 4atj sisyphus luke Seek mukundan, ox jam, biz) / others: 64(jailctf merger), 64(intgrah jimboko awu macaque sammyuri), 73(import itertools), 74(jacekwl Potatoman nauti), 74(jacekw Potatoman nauti natte)
# ============================= 63 ============================
# lambda s,c=0:sum([[v*0!=0and p(v,c:=9-sum(s,[]).count(0))or v]*c for v in s],[])
# lambda s,c=0:sum([[v*0!=0and p(v,c:=9-str(s).count("0"))or v]*c for v in s],[])
# lambda s,c=0:sum([[v*0!=0and p(v,c:=len({*str(s)})-5)or v]*c for v in s],[])
# ============================= 63 ============================
p=lambda s:sum([[v*0!=0and p(v+s)or v]*(len({*str(s)})-5)for v in s[:3]],[])
