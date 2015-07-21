sum = 0
i = 1
n = 1
fib = [0,1,2]
while fib[n] + fib[n+1] < 4000000:
      fib.append(fib[n] + fib[n+1])
      n += 1
while i <= n+1:
      if fib[i]%2 == 0:
            sum += fib[i]
      i +=1
print(sum)
      
 

