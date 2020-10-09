def miniMaxSum(arr):
    array_sum = []
    #removes pne element each arr creating list and sum all elements this list em array_sum, LOOP
    for n, m in enumerate(arr):
        copia = arr.copy()
        copia.remove(arr[n])
        array_sum.append(sum(copia))
    #maximum value of array_sum list and minimum value of array_sum list
    max_min = max(array_sum), min(array_sum)

    return print(max_min[1], max_min[0])


#299, 9271
miniMaxSum([7, 69, 2, 221, 8974])

if __name__ == '__main__':
    array = list(map(int,input('Enter a comma-separated list --> ').split(',')))
    miniMaxSum(list(map(int,array)))
    
