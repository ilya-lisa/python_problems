def get_levenshtain_distance(first, second):
    if first == second or len(first) == 0 or len(second) == 0:
        return 0

    v0 = [0] * (len(second) + 1)
    v1 = [0] * (len(second) + 1)

    for i in range(len(v0)):
        v0[i] = i

    for i in range(len(first)):
        v1[0] = i + 1

        for j in range(len(second)):
            cost = 0 if first[i] == second[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)

        for j in range(len(v0)):
            v0[j] = v1[j]

    return v1[len(second)]


with open("/Users/ipatrikeev/pdev/input.txt") as f:
    n_cases = int(f.readline())
    for case in range(n_cases):
        first, second = f.readline().strip().split(' ', 1)
        print(get_levenshtain_distance(first, second), end=' ')
