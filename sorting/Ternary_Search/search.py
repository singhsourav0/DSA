def ternary_search(arr, i, j, key):
    mid1 = i+(j-i)//3
    mid2 = j-(j-1)//3
    if i<=j :
        if arr[mid1]==key:
            return mid1
        
        if arr[mid2]== key:
            return mid2
        
        if key<arr[mid1]:
            return  ternary_search(arr, i, mid1-1, key)       
        elif key>arr[mid2]:
            return  ternary_search(arr, mid2+1, j, key)       
        else :
            return  ternary_search(arr, mid1+1, mid2-1, key)
    else:   
        return -1


def main():
    arr= [100,200, 600, 700, 800, 900, 1000]
    i = 0
    j = len(arr)-1

    key = 900

    index = ternary_search(arr, i, j, key)
    print(index)
        
if __name__ =="__main__":
    main()