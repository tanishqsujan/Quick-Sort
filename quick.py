def partition(A, low, high):
    
    pivot= A[high]
    
    i= low - 1
    
    for j in range(low, high):
        if A[j] <= pivot:
            i= i + 1
            
            (A[i], A[j]) = (A[j], A[i])
     
     #swap the pivot element with the greater element specified by i       
    (A[i + 1], A[high]) = (A[high], A[i + 1])
    
    #return the position from where the partition is done
    return i + 1

#function to perform quick sort
def quicksort(A, low, high):
    if low < high:
        
        #find pivot element such that
        #element which are less are on the left
        #element which are greater are on the right
        
        pi= partition(A, low, high)
        
        #recursive call on the left side
        quicksort(A, low ,pi-1)
        
        #recursive call on the right side
        quicksort(A, pi+1, high)
        
A= [8, 17, 22, 55, 2, 30, 48]
print("Unsorted Array")
print(A)

n= len(A)- 1

quicksort(A, 0, n)

print("Sorted Array")
print(A)
    