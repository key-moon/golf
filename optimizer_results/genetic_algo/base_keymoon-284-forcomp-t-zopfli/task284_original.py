B=range
A=len
p=lambda g:(A(u:=[i for i in B(A(g))if any(g[i])])>1)*[[max(g[u[-(i>u[0]+u[-1]>>1)]])*((u[0]+u[-1]>>1<=i<(u[0]+u[-1]>>1)+2)*2<=abs(j-g[u[0]].index(max(g[u[0]])))<=((u[0]+u[-1]>>1)-2<i<(u[0]+u[-1]>>1)+3)*2)*(u[0]<=i<=u[-1])for j in B(A(g[0]))]for i in B(A(g))]or[*zip(*p([*zip(*g)]))]