def process_test_case(n, a):
    even_numbers = sorted([x for x in a if x % 2 == 0], reverse=True)
    odd_numbers = sorted([x for x in a if x % 2 != 0])
 
    mihai_candies, bianca_candies = sum(even_numbers), sum(odd_numbers)
 
    if mihai_candies > bianca_candies:
        return "YES"
    else:
        return "NO"
 
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = process_test_case(n, a)
    print(result)
