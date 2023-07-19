def find_noble_integer(A):
    A.sort()
    n = len(A)
    for i in range(n - 1, -1, -1):
        if A[i] == n - i - 1:
            return 1
    return 0
A = list(map(int, input("Enter the elements of the array (space-separated): ").split()))
output = find_noble_integer(A)
print("Output:", output)
