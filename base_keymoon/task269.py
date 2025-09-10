# best: 63(4atj sisyphus luke Seek mukundan) / others: 64(jailctf merger), 64(xsot ovs att joking mewheni), 71(intgrah jimboko awu macaque sammyuri), 83(HETHAT), 83(jonas ryno kg583)
# ============================= 63 ============================
# lambda s,c=0:sum([[v*0!=0and p(v,c:=9-sum(s,[]).count(0))or v]*c for v in s],[])
# lambda s,c=0:sum([[v*0!=0and p(v,c:=9-str(s).count("0"))or v]*c for v in s],[])
# lambda s,c=0:sum([[v*0!=0and p(v,c:=len({*str(s)})-5)or v]*c for v in s],[])
# ============================= 63 ============================
p=lambda s:sum([[v*0!=0and p(v+s)or v]*(len({*str(s)})-5)for v in s[:3]],[])










