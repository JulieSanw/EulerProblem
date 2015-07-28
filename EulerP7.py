prime = [1]
n = 2

while len(prime)< 10002:
      a = 2
      flg = True
      while a*a <= n:
            if n%a != 0:
                  a+=1
            else:
                  flg = False
                  a+=1
            
      if flg == True:
            prime.append(n)
      n += 1
      
print(prime[10001])
