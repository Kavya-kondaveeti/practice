n=7
for i in range(7):
    for j in range(7):
        if i==j or (i+j)==n-1 or i==n//2 or j==n//2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
