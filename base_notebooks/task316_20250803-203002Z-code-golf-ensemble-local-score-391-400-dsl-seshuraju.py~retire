def p(m):
 n=3
 
 # Trích xuất các giá trị khác 0 theo thứ tự cột
 v=[]
 for c in range(len(m[0])):
  for r in range(len(m)):
   if m[r][c]:
    v.append(m[r][c])
    break
 
 # Điền thêm số 0 cho đủ kích thước n x n
 v.extend([0]*(n*n-len(v)))
 
 # Định hình lại ma trận theo quy tắc zigzag
 return[v[i*n :(i+1)*n]if i%2==0 else v[i*n :(i+1)*n][::-1]for i in range(n)]
