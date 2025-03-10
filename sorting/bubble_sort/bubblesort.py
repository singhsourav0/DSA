def bubble_sort(arr):
    l = len(arr)
    for i in range (l-1):
        for j in range (l-1):
          if arr[j]>arr[j+1]:
        #    temp = arr[j]

        #    arr[j]= arr[j+1]
        #    arr[j+1]= temp
            arr[j],arr[j+1] = arr[j+1], arr[j]

    return arr




def main():
    arr= [100,2, 30, 4, 11,30]
    
    index = bubble_sort(arr)
    print(index)
        
if __name__ =="__main__":
    main()