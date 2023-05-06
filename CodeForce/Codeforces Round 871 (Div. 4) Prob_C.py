from typing import List, Tuple

def solve(t: int, test_cases: List[Tuple[int, List[Tuple[int, str]]]]) -> List[int]:
    results = []
    for case in range(t):
        n, books = test_cases[case]
        skill_1 = skill_2 = float('inf')
        both_skills = -1

        for book in books:
            time, skills = book
            time = int(time)
            if skills == "10":
                skill_1 = min(skill_1, time)
            elif skills == "01":
                skill_2 = min(skill_2, time)
            elif skills == "11":
                both_skills = min(both_skills, time) if both_skills != -1 else time

        if both_skills != -1:
            results.append(min(both_skills, skill_1 + skill_2))
        elif skill_1 != float('inf') and skill_2 != float('inf'):
            results.append(skill_1 + skill_2)
        else:
            results.append(-1)

    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    books = [tuple(input().split()) for _ in range(n)]
    test_cases.append((n, books))

results = solve(t, test_cases)
for res in results:
    print(res)
