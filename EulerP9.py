for a in range (1,334):
      for b in range (1, int((1000-a)/2+1)):
            c = 1000 - a - b
            if a*a + b*b == c*c:
                  print(a*b*c)
                  
