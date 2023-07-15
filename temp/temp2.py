import random
def generate_test_case(n):
    with open('input.txt', 'w') as f:
        f.write(f"{n}\n")
        for _ in range(n):
            f.write(f"{random.randrange(10000000)}\n")

generate_test_case(5000000)
