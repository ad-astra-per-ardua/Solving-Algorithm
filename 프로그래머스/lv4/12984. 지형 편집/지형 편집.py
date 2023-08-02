def solution(land, P, Q):
    blocks = sorted([item for sublist in land for item in sublist])
    total = sum(blocks)
    floor, prev, answer = -1, 0, float('inf')

    for i, block in enumerate(blocks):
        if floor != block:
            floor = block
            added = block * i - prev
            deleted = total - prev - (len(blocks) - i) * block
            cost = added * P + deleted * Q
            if answer > cost:
                answer = cost
        prev += block

    return answer
