import itertools

n = 7
permutations = list(itertools.permutations([i+1 for i in range(n)]))

print(len(permutations))

for permutation in permutations:
    print(' '.join(str(x) for x in permutation))
