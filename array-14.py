def second_largest(arr):
    if len(arr) < 2:
        return None  
    arr = list(set(arr))  
    arr.sort(reverse=True)  
    return arr[1]  


arr = [10, 20, 30, 40, 50, 20, 10, 60, 30]
print("Second largest number:", second_largest(arr))
