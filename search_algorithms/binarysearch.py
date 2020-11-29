l = []
n = int(input("Enter no of elements to be added in list : "))
i = 0
while i < n:
    get_num = int(input("Enter Value: "))
    l.append(get_num)
    i += 1
value = int(input("Enter value to be found : "))


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


result = binary_search(l, 0, len(l) - 1, value)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
