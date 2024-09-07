#swap without using 3rd variables
def swap(num1, num2):
    num1 = num1+num2
    num2 = num1-num2
    num1 = num1-num2

    return num1, num2

def main():
    a = int(input('enter 1st element'))
    b = int(input('enter 2nd elements'))
    
    index = swap(a, b)
    print(index)
        
if __name__ =="__main__":
    main()
    
    