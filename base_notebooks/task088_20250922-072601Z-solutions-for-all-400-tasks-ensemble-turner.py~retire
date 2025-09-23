from collections import*
b=len
i=range
def p(m):
	E=[i for i in m for i in i];k=Counter(E).most_common();k=[C for C in k if C[1]==4][0][0];s,p=b(m),b(m[0]);f=[]
	for a in i(s):
		for C in i(p):
			if m[a][C]==k:f.append([a,C])
	e=min([i[1]for i in f]);u=max([i[1]for i in f]);a=min([i[0]for i in f]);j=max([i[0]for i in f]);m=m[a+1:j];m=[i[e+1:u]for i in m];s,p=b(m),b(m[0])
	for a in i(s):
		for C in i(p):
			if m[a][C]>0:m[a][C]=k
	return m