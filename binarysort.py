'''
arr: List of integers denoting the input array
n  : size of the given array

You need to return the sorted binary array
'''
def sortBinaryArray (arr, n):
    j=-1
    for i in range(len(arr)):
        if arr[i]==0:
            j=j+1
            arr[i],arr[j]=arr[j],arr[i]
    return arr  


    # Python program to find sum of 
# all subarrays of array 

# To find sum of all subarrya 
def findSum(arr, n): 
	
	# Sum all array elements 
	sum = 0
	for i in range(n): 
		sum += arr[i] 

	# Result is sum * 2^(n-1) 
	return sum * (1 << (n - 1)) 

# Driver program to test findSum() 
arr = [1, 2] 
n = len(arr) 
print findSum(arr, n)
