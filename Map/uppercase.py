lst = []

n = int(input("Enter no. of Elements in list: "))
for i in range(n):
    x = input(f"Enter element {i} to convert to uppercase: ")
    lst.append(x)
print("Original List:", lst)

# Convert all elements to uppercase using map
res1 = list(map(lambda x: str(x).upper(), lst))
print("Uppercase List:", res1)



#without map we can do so as...
res2 = list(map(str.upper, lst))
print("Without using lambda: ", list(res2))


#Extracting 1st string of all elements from list..
first = map(lambda x: str(x)[0], lst)
print(list(first))


#Length of Each Word:
length = list(map(lambda l: len(l), res2))
print("length of string in list as: ", length)
