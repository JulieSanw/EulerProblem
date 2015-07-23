a1 = 0
x = 0
for n in range(1,101):
      a1 += n*n
for n in range(1,101):
      x += n
a2 = x*x
ans = a2-a1
print(ans)
