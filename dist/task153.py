B=range
p=lambda g,z=[0]*10:max(all(sum(u:=[[([z,*g,z][A//576+u]+z)[A//64%9+v]^g[A//8%8+u][A%8+v]for v in B(3)]for u in B(3)],[]))*u for A in B(5760))