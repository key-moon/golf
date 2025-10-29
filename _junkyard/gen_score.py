res = []
for i in range(1, 401):
  res.append(len(open(f"dist/task{i:03}.py", "rb").read()))
print("\n".join(map(str, res)))
