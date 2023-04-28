t, m, s = map(int,input().split())
time = int(input())

sec = time % 60  # second
hour = time // 3600 # minute * 60 = hour
min = (time - (hour * 3600)) // 60 # minute

ans_t = t + hour
ans_min = m + min
ans_s = s + sec

while True:
    if ans_s >= 60:
        ans_min += 1
        ans_s -= 60
    if ans_min >= 60:
        ans_t += 1
        ans_min -= 60
    if ans_t >= 24:
        ans_t -= 24
    else:
        break
print(ans_t,ans_min,ans_s)
