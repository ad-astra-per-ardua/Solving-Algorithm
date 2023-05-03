n = int(input())
call = list(map(int, input().split()))

youngsik_fee = 0
minsik_fee = 0

for duration in call:
    youngsik_fee += (duration // 30 + 1) * 10
    minsik_fee += (duration // 60 + 1) * 15

if youngsik_fee < minsik_fee:
    print(f"Y {youngsik_fee}")
elif youngsik_fee > minsik_fee:
    print(f"M {minsik_fee}")
else:
    print(f"Y M {youngsik_fee}")
