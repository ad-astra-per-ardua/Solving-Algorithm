def solution(clockHands):
    length = len(clockHands)

    clockHands = [[4 - el if el else el for el in sublist] for sublist in clockHands]

    def getFixedNum(num):
        while num >= 4:
            num -= 4
        while num < 0:
            num += 4
        return num

    def calculator(arr):
        for i in range(length):
            for j in range(length):
                value = arr[i][j]

                if i+1 < length:
                    arr[i+1][j] -= value

                    if j-1 >= 0: 
                        arr[i+1][j-1] -= value
                    if j+1 < length: 
                        arr[i+1][j+1] -= value

                if i+2 < length:
                    arr[i+2][j] -= value

        return [getFixedNum(el) for el in arr[length-1]]

    def getLastColDiffByHeadIdxValue1(headIndex):
        map_ = [[0]*length for _ in range(length)]

        map_[0][headIndex] = -1
        if headIndex - 1 >= 0: 
            map_[0][headIndex-1] = -1
        if headIndex + 1 < length: 
            map_[0][headIndex+1] = -1

        if length > 1:
            map_[1][headIndex] = -1

        return calculator(map_)

    headerOneValueAffectMap = [getLastColDiffByHeadIdxValue1(idx) for idx in range(length)]

    calculated = calculator([row.copy() for row in clockHands])

    counter = [0]*length
    validHeaders = []

    def increaseCounter():
        nonlocal counter
        counter[-1] += 1

        for i in range(length-1, -1, -1):
            if counter[i] >= 4:
                if i == 0:
                    counter[i] = -1
                    return
                counter[i] = 0
                counter[i-1] += 1

    while True:
        if counter[0] == -1: break
        isValid = True

        for i in range(length):
            targetSum = calculated[i] + sum(cur[i] * counter[idx] for idx, cur in enumerate(headerOneValueAffectMap))

            if targetSum % 4 != 0:
                isValid = False
                break

        if isValid:
            validHeaders.append(counter.copy())

        increaseCounter()

    def validMaps(header):
        map_ = [[0]*length for _ in range(length)]
        map_[0] = header.copy()

        for i in range(length - 1):
            for j in range(length):
                sum_ = map_[i][j]

                if j+1 < length: 
                    sum_ += map_[i][j+1]
                if j-1 >= 0: 
                    sum_ += map_[i][j-1]
                if i-1 >= 0: 
                    sum_ += map_[i-1][j]

                resultValue = getFixedNum(clockHands[i][j] - sum_)

                map_[i+1][j] = resultValue

        return map_

    validMapsList = [validMaps(header) for header in validHeaders]

    return min(
        sum(sum(row) for row in map_)
        for map_ in validMapsList
    )
