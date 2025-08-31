# best: 115(jailctf merger) / others: 116(4atj sisyphus luke Seek), 116(sisyphus), 117(xsot ovs att joking mewheni), 117(mukundan), 117(joking)
# ====================================================== 115 ======================================================
import re
p=lambda g:eval(r'(g:=[*zip(*eval(re.sub(r"(([1-9]), \2.{31}\2.{25}(\2.{28})*)0",r"\1\2",str(g)))[::-1])]),'*32)[-1]

# import re
# p=lambda g:eval(r'(g:=eval(re.sub(r"(([1-9]), \2.{31}\2.{25}(\2.{28})*)0",r"\1 \2",str(g)))),')[0]
