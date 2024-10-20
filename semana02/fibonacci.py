""" Fibonacci """

# 0 1 1 2 3 5 8 13 21 34...
t1, t2 = 0, 1
print(t1, t2, end=' ')
for i in range(10):
    t3 = t1 + t2
    print(t3, end=' ')
    t1, t2 = t2, t3