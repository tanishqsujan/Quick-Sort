def partition(A, low, high):
    
    pivot= A[high]
    
    i= low - 1
    
    for j in range(low, high):
        if A[j] <= pivot:
            i= i+1
            (A[i], A[j]) = (A[j], A[i])
    (A[i+1], A[high]) = (A[high], A[i+1])
    return i+1

def quick(A, low, high):
    if low < high:
        
        pi= partition(A, low, high)
        
        quick(A, low, pi-1)
        quick(A, pi+1, high)
        
A= list(map(int, input("Enter elements in Array: ").split()))

n= len(A) - 1
quick(A, 0, n)

print("Sorted Array")
print(A)