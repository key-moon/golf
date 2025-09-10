# best: 65(jailctf merger) / others: 72(4atj sisyphus luke Seek mukundan), 79(xsot ovs att joking mewheni), 80(intgrah jimboko awu macaque sammyuri), 82(HETHAT), 84(natte)
# ============================== 65 =============================
p=lambda g:g*-1and g%5+5or[p(g[i%2-3&i^1])for i in range(len(g))]

# mapping = { 1: 6, 2: 7, 3: 8, 4: 9, 5: 5 }

# len(res)=9 res=''
# len(res)=9 res='x%2-3&x|1'
# len(res)=9 res='x-x%4%3|1'
# len(res)=9 res='x^x%4%3|1'
# mapping = { 0: 1, 1: 1, 2: 1, 3: 3, 4: 5, 5: 5, 6: 5, 7: 7, 8: 9, 9: 9, 10: 9 }
