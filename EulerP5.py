ans = []
mul = 1
for n in range(0,20):
      ans.append(n+1)
      mul *= (n+1)
for a in range(1,21):
      if (mul/a)%a == 0:
            mul =mul/a
print (mul)
