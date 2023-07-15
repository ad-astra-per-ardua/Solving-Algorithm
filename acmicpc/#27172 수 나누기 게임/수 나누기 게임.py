import sys
input = sys.stdin.readline

def main():
    N = int(input())
    size = 1000001
    player = [0]*N
    card = [False]*size
    score = [0]*size
    input_list = list(map(int, input().split()))
    for i in range(N):
        player[i] = input_list[i]
        card[player[i]] = True

    for i in player:
        j = i * 2
        while j < size:
            if card[j]:
                score[i] += 1
                score[j] -= 1
            j += i

    print(' '.join(str(score[num]) for num in player))

if __name__ == "__main__":
    main()
