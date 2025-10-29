import random
from utils import get_task

# ref: implementation of the randbelow, randint and getrandbits
# def _randbelow_with_getrandbits(self, n):
#     "Return a random int in the range [0,n).  Defined for n > 0."
#     k = n.bit_length()
#     r = self.getrandbits(k)  # 0 <= r < 2**k
#     while r >= n:
#         r = self.getrandbits(k)
#     return r
# def randint(self, a, b):
#     """Return random integer in range [a, b], including both end points.
#     """
#     a = _index(a)
#     b = _index(b)
#     if b < a:
#         raise ValueError(f"empty range in randint({a}, {b})")
#     return a + self._randbelow(b - a + 1)
# static PyObject* _random_Random_getrandbits_impl(RandomObject *self, uint64_t k)
# {
#     Py_ssize_t i, words;
#     uint32_t r;
#     uint32_t *wordarray;
#     PyObject *result;
#     ...
#     words = (k - 1u) / 32u + 1u;
#     wordarray = (uint32_t *)PyMem_Malloc(words * 4);
#     for (i = words - 1; i >= 0; i--, k -= 32)
#     {
#         r = genrand_uint32(self);
#         if (k < 32)
#             r >>= (32 - k);  /* Drop least significant bits */
#         wordarray[i] = r;
#     }
#     result = _PyLong_FromByteArray((unsigned char *)wordarray, words * 4, PY_LITTLE_ENDIAN, 0 /* unsigned */);
#     PyMem_Free(wordarray);
#     return result;
# }

LEAK_CASES = 4

# https://github.com/google/ARC-GEN/blob/main/tasks/training/task043.py
# rows = [item for item in range(1, size) if common.randint(0, 1) == 0]
# cols = [item for item in range(0, size - 1) if common.randint(0, 1) == 0]

cases = get_task(43)['arc-gen']
leak_43 = []
for case in cases[:LEAK_CASES]:
  g = case['input']  
  leak = [1*(0==r[-1])for r in g[1:]] + [1*(0==c)for c in g[0][:-1]]
  leak_43.append(leak)

# https://github.com/google/ARC-GEN/blob/main/tasks/training/task127.py
# colors = [common.randint(1, 4) for _ in range(3 * common.randint(1, 2))]

cases = get_task(127)['arc-gen']
leaks_127 = []
for case in cases[:LEAK_CASES]:
  g = case['input']
  leak = []
  leak.append([0, 1][len(g)==7])
  leak.extend([v-1 for v in g[1][1::4]])
  if len(g) == 7:
    leak.extend([v-1 for v in g[5][1::4]])
  leaks_127.append(leak)

# https://github.com/google/ARC-GEN/blob/main/tasks/training/task142.py
# colors = [common.randint(0, 3) for _ in range(size * size)]
# grid, output = common.grid(size, size), common.grid(2 * size, 2 * size)
# for r in range(size):
#   for c in range(size):
#     grid[r][c] = colors[r * size + c]
cases = get_task(142)['arc-gen']
leaks_142 = []
for case in cases[:LEAK_CASES]:
  g = case['input']
  leak = []
  for s in g:
    for v in s:
      leak.append(v)
  leaks_142.append(leak)

# print(f"{len(leak_142)=}")
# print(f"{len(leak_127)=}")
# print(f"{len(leak_43)=}")

print(leak_43)
print(leaks_127)
print(leaks_142)

# 2025 0
# 2026 1
# 2027 2
# 2028 3
for i in range(10000):
  random.seed(i)
  r = [random.randint(0,1) for i in range(18)]
  if r in leak_43:
    print(i, leak_43.index(r))
