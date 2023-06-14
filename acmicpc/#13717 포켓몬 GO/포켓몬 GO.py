def solve(pokemon_list):
    total = 0
    lists = []

    for poke_idx, pokemon_info in enumerate(pokemon_list):
        pokemon, k, m = pokemon_info[0], pokemon_info[1], pokemon_info[2]
        pokemon_evol_num = 0

        while m >= k:
            m -= k
            m += 2

            pokemon_evol_num += 1
        total += pokemon_evol_num
        lists.append([pokemon, pokemon_evol_num, poke_idx])
    maxi = sorted(lists, key=lambda x: (x[1], -x[2]))[-1][0]
    return total, maxi
if __name__ == "__main__":
    pokemon_list = []

    for _ in range(int(input())):
        pokemon = input()
        k, m = map(int, input().split())
        pokemon_list.append((pokemon, k, m))
    answer = solve(pokemon_list=pokemon_list)

    print(answer[0])
    print(answer[1])