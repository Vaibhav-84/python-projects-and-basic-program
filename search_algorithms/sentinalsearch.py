l = []
n = int(input("Enter no of elements to be added in list : "))
i = 0
while i < n:
    get_num = int(input("Enter Value: "))
    l.append(get_num)
    i += 1
value = int(input("Enter value to be found : "))
l.append(value)


def sentinal(l, value):
    j = 0
    while True:
        if l[j] == value:
            break
        j += 1
    return j


search = sentinal(l, value)
if search < n:
    print("Element Found")
else:
    print("Element not found")
