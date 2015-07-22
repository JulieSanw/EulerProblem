ans = [ ]
for n in range(100,1000):
       for m in range(n + 1, 1000):
           q = n*m
           p = str(q)
           L = list(p)
           J = list(p)
           L.reverse()
           K = L
           s = ''
           r = ''
           b = 0
           while b<len(K):
               s = s + K[b]
               r = r + J[b]
               b += 1
           if int(s)==int(r):
               ans.append(int(r))
print(max(ans))
