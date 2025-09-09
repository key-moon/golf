B=range
p=lambda g,z=[0]*10:[u for A in B(6400)if all(sum(u:=[[[0,*[z,*g,z][A//640+u],0][A//64%10+v]^g[A//8%8+u][A%8+v]for v in B(3)]for u in B(3)],[]))][0]