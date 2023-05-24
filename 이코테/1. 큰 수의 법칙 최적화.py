n, m, k = map(int,input().split())
num_list = list(map(int, input().split()))
num_list.sort()
summation = 0

max1 = num_list[n-1]
max2 = num_list[n-2]

attempt = int((m / (k+1)) * k + m % (k + 1))
summation += attempt * max1
summation += (m - attempt) * max2

print(summation)