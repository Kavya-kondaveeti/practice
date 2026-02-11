n=7
for i in range(7):
    for j in range(7):
        if  i==0 or j==0 or (i==n//2 and j<4)or (j=4 i<n//2 and i!=0):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
