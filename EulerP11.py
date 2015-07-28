fo1 = open('P11.txt','r')
t = fo1.readlines()
l = len(t)
fo1.close()
fo2 = open('P11.txt','r')
grid = []
i = 1
for i in range(1,l+1):
      s = fo2.readline()
      slist = s.split()
      grid.append(slist)
fo2.close()

row = len(grid)
col  = len(grid[1])
ngrid = []
for a in range(0,row):
      lrow = []
      for b in range(0,col):
            lrow.append(int(str(grid[a][b])))
      ngrid.append(lrow)

max = 1

for x1 in range(0,row):
      for m1 in range (0,col-3):
            pro = 1
            for n1 in range(m1,m1+4):
                  pro *= ngrid[x1][n1]
            if pro > max:
                  max = pro

for m2 in range(0, col):
      for x2 in range(0, row-3):
            pro = 1
            for n2 in range(x2,x2+4):
                  pro *= ngrid[n2][m2]
            if pro > max:
                  max = pro

for m3 in range(0, col-3):
      for x3 in range(0, row-3):
            pro = 1
            for n3 in range(x3,x3+4):
                  pro *= ngrid[n3][m3+n3-x3]
            if pro > max:
                  max = pro
                  
for m4 in range(3, col):
      for x4 in range(0, row-3):
            pro = 1
            for n4 in range(x4,x4+4):
                  pro *= ngrid[n4][m4-n4+x4]
            if pro > max:
                  max = pro

print(max)
