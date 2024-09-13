def selection(arr):
    l = len(arr)
    for i in range(l-1):
        min = arr[i]
        index = i
        for j in range(i,l):
           if arr[j]< min:
            min= arr[j]
            index = j
        arr[index]= arr[i]
        arr[i] = min

    return arr

def main():
    arr= [100,2, 30, 4, 11,30]
    
    index = selection(arr)
    print(index)
        
if __name__ =="__main__":
    main()
