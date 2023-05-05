import random
import sys
import psutil
sys.stdin.readline()
sys.setrecursionlimit(10**6)
def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.5f} MB")

def rsc(user_choice, cpu_choice):
    if user_choice == cpu_choice:
        return "비겼음"
    elif (user_choice - cpu_choice) % 3 == 1:
        return "User가 이겼음"
    else:
        return "User가 졌음"


while True:
    a = int(input("0. 종료 1. 가위 2. 바위 3. 보\n"))
    cpu = random.randint(1, 3)

    if a == 0:
        break

    result = rsc(a, cpu)
    print(f"User은 {a}를 내고 cpu는 {cpu}를 내고  {result}")
