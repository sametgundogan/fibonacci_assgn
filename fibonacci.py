a = 0
b = 1
res = []

for i in range(10):
    res.append(b)
    a ,b = b, a + b

print(res)

# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
