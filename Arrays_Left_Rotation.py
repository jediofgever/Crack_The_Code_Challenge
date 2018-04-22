def array_left_rotation(a, n, k):
    myArray = []
    
    for i in range(k):
        insertIt = a[0]
        myArray.append(insertIt)
        del a[0]
    for j in range(len(myArray)):
        a.append(myArray[j])
    return  a 

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
