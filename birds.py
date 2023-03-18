def tiposAves(arr):
    count = [0,0,0,0,0]
    birds = [5,4,3,2,1]
    a = 0
    for i in arr:
        for j in birds:
            if j == i:
                count[j-1]=count[j-1]+1
    for j in range(4):
        for i in range(4):
            if count[j] > count[i]:
                a = count[j] 
                count[j] = count[i]
                count[i] = a

                a = birds[j]
                birds[j] = birds[i]
                birds[i] = a
    for i in range(4):
        if count[0] == count[i]:
            if birds[0] > birds[i]:
                a = birds[0]
                birds[0] = birds[1]
                birds[1] = a
    print(birds[0])
    return birds[0]

M = [1,4,4,4,5,3,3,5,2,3,4,]
tiposAves(M)
