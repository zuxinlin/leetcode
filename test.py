def find_max_multi(arr):
    if not arr or len(arr) < 3:
        return

    result = float('-inf')
    data = []
    n = len(arr)

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                temp = arr[i] * arr[j] * arr[k]
                if temp > result:
                    data = [arr[i], arr[j], arr[k]]
                    result = temp

    return data


def find_max_multi_opt(arr):
    a, b, c = float('-inf'), float('-inf'), float('-inf')
    t1, t2 = 0, 0

    for num in arr:
        if num > a:
            c = b
            b = a
            a = num
        elif num > b:
            c = b
            b = num
        elif num > c:
            c = num

        if num < 0:
            if num < t1:
                t2 = t1
                t1 = num
            elif num < t2:
                t2 = num

    r1 = a * b * c
    r2 = a * t1 * t2

    if r1 > r2:
        return [a, b, c]
    else:
        return [a, t1, t2]


if __name__ == '__main__':
    print(find_max_multi([10, 8, 20, -1]))
    print(find_max_multi([-10, 8, 9, 1, -1]))
    print(find_max_multi([-10, -2, -3, -1]))
    print("===============================")
    print(find_max_multi_opt([10, 8, 20, -1]))
    print(find_max_multi_opt([-10, 8, 9, 1, -1]))
    print(find_max_multi_opt([-10, -2, -3, -1]))
