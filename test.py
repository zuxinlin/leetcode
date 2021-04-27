def merge(arr, left, center, right):
    temp = []
    i, j = left, center + 1

    while i <= center and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= center:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    i = left
    for data in temp:
        arr[i] = data
        i += 1


if __name__ == '__main__':
    arr = [1, 1, 3, 4, 6, 1, 2, 3, 5, 7]
    merge(arr, 0, 4, len(arr) - 1)
    print(arr)
