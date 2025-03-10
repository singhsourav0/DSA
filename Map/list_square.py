my_list = []

Elements = int(input("Enter No. of elements in list: "))

for i in range(0, Elements):
    a= input(f"Enter the Elements of my_list as{i}: ")
    my_list.append(a)


def square(value):
    value = int(value)
    return value**2

square = list(map(square, my_list))
print(square)


#convert into farenite if it calcius:
far = map(lambda C :  (C * 9/5) + 32, square)
print(list(far))