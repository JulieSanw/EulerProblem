prime = []
n = 2
while n < 2000001:
      a = 2
      flg = True
      while a*a <= n:
            if n%a != 0:
                  a += 1
            else:
                  flg = False
                  a += 1
      if flg == True:
            prime.append(n)
      n +=1

l= len(prime)
sum = 0
for i in range(0,l):
      sum += prime[i]


print(sum)
