arr = [1, 3, 5, 7, 9]

def minMaxSum(arr):
    arr.sort()
    arr_sum = sum(arr)
    min_sum = arr_sum - arr[4]
    max_sum = arr_sum - arr[0]
    return min_sum, max_sum


print(minMaxSum(arr))




