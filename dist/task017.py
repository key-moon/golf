A=range
p=lambda g:[u for d in A(4,10)if(u:=[[max(max(g[i%d::d])[j%d::d])for j in A(21)]for i in A(21)])if sum(s in g for s in u)>9][0]