# best: 63(4atj sisyphus luke Seek mukundan) / others: 64(jailctf merger), 64(xsot ovs att joking mewheni), 71(intgrah jimboko awu macaque sammyuri), 83(HETHAT), 83(jonas ryno kg583)
# ============================= 63 ============================
# p=lambda s,c=0:sum([[v*0!=0and p(v,c:=9-sum(s,[]).count(0))or v]*c for v in s],[])
# p=lambda s,c=0:sum([[v*0!=0and p(v,c:=9-str(s).count("0"))or v]*c for v in s],[])
p=lambda s,c=0:sum([[v*0!=0and p(v,c:=len({*sum(s,v)})-1)or v]*c for v in s],[])
