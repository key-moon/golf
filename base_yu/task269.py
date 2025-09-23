# best: 63(ox jam, 4atj sisyphus luke Seek mukundan) / others: 64(jailctf merger), 71(intgrah jimboko awu macaque sammyuri), 74(jacekw Potatoman nauti), 74(jacekwl Potatoman nauti), 83(JRKX)
# ============================= 63 ============================
# p=lambda s,c=0:sum([[v*0!=0and p(v,c:=9-sum(s,[]).count(0))or v]*c for v in s],[])
# p=lambda s,c=0:sum([[v*0!=0and p(v,c:=9-str(s).count("0"))or v]*c for v in s],[])
# p=lambda s,c=0:sum([[v*0!=0and p(v,c:=len({*str(s)})-5)or v]*c for v in s],[])
# p=lambda g,c=-1:c*g or[*zip(*sum(zip(*[p(g,c+1)]*(len({*str(g)})-5)),()))]
p=lambda g:sum([(k:=len({*str(g)})-5)*[sum(zip(*[s]*k),())]for s in g],[])
