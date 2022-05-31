# https://www.runoob.com/python3/python3-99-table.html

for i in range(1, 10):
    for j in range(1, i+1):
        print("{}x{}={}\t".format(j,i,i*j),end=" ")
    print()

for i in range(1, 10):
    for j in range(1, i + 1):
        if i == j:
            print('{1}×{0}={2}'.format(i, j, i * j))
        else:
            print('{1}×{0}={2}'.format(i, j, i * j), end='\t')

