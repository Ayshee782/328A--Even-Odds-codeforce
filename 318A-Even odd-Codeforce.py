# Input n and k
n, k = map(int, input().split())

# Count of odd numbers in 1 to n
odd_count = (n + 1) // 2

# Checke if k-th number is in odd or even section
if k <= odd_count:
    # k-th number is the k-th odd number
    print(2 * k - 1)
else:
    # k-th number is from the even numbers
    even_position = k - odd_count
    print(2 * even_position)
