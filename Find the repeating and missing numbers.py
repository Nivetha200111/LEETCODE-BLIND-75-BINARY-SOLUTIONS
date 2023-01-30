def repeatingAndMissing(arr):
    n = len(arr)
    substitute = [0] * (n+1)
    for i in range(n):
        substitute[arr[i]] += 1
    for i in range(1, n+1):
        if substitute[i] == 2:
            A = i
        elif substitute[i] == 0:
            B = i
    return (A, B)
