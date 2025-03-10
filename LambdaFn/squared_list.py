lst= []

n = int(input("Enter the no. of Elements: "))

for i in range(0, n):
    x = int(input(f"Enter any number as{i}: "))
    lst.append(x)
print(lst)

print(f"Squared list of elements {list(map(lambda x: x ** 2, lst))}")