# 끔찍하다 끔찍해 혼종이 따로없네 그냥
lists = []
ans = []
for _ in range(9):
    a = int(input())
    lists.append(a)
breaker = False
lists.sort()
for g in range(0,3):
    if breaker:
        break
    for h in range(1,4):
        if breaker:
            break
        if h <= g:
            continue
        for l in range(2,5):
            if breaker:
                break
            if l <= h:
                continue
            for k in range(3,6):
                if breaker:
                    break
                if k <= l:
                    continue
                for j in range(4,7):
                    if breaker:
                        break
                    if j <= k:
                        continue
                    for e in range(5,8):
                        if breaker:
                            break
                        if e <= j:
                            continue
                        for i in range(6,9):
                            if i <= e:
                                continue
                            summation = lists[g] + lists[h] + lists[l] + lists[k] + lists[j] + lists[e] + lists[i]
                            if summation == 100:
                                ans.append(lists[i])
                                ans.append(lists[e])
                                ans.append(lists[j])
                                ans.append(lists[k])
                                ans.append(lists[l])
                                ans.append(lists[h])
                                ans.append(lists[g])
                                breaker = True
                                break


ans.sort()
for i in range(len(ans)):
    print(ans[i])