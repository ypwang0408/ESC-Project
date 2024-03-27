import numpy as np
a = np.zeros((5,5))
b = np.zeros((5,5))

for i in range(5):
    for j in range(5):
        a[i][j] = input()
        b[i][j] = 0

for i in range(5):
    for j in range(5):
        print(a[i][j], end=' ')
    print()
    
print()
print()
    
for i in range(5):
    for j in range(5):
        for m in range(i+1):
            for n in range(j+1):
                b[i][j] += a[m][n]
                
for i in range(5):
    for j in range(5):
        print(b[i][j], end=' ')
    print()