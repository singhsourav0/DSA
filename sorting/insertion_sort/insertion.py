def insertion_sort(arr):
    for i in range (1, len(arr)):
        key = arr[i]
        j = i-1

        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = key

    return arr    

    
def main():
    arr = [2, 4,1,6,3,7,5]
    
    index = insertion_sort(arr)
    print(index)
        
if __name__ =="__main__":
    main()